import json
import streamlit as st
from PIL import Image
import pytesseract
from datetime import datetime
from rapidfuzz import process, fuzz
from med_db import MED_DB
from symptom import symptom_advice

from ollama import Client
ollama = Client()


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def find_medicine(name):
    if not name:
        return None

    cleaned = name.lower().replace("+", " ").replace(",", " ").replace(".", " ").strip()
    names = list(MED_DB.keys())
    match, score, _ = process.extractOne(cleaned, names, scorer=fuzz.WRatio)
    if score >= 80:
        return match
    return None


def check_interactions(medicines):
    results = []

    for med in medicines:
        key = find_medicine(med)
        if not key:
            continue

        interactions = MED_DB[key].get("interactions", {})
        if interactions:
            k, v = next(iter(interactions.items()))
            results.append(f"⚠️ {MED_DB[key]['name']}: {v}")

    return results


def llama_short_warning(lines):
    prompt = f"""
Medicines safety note:

{chr(10).join(lines)}

Summarize into ONE short, clear safety sentence.
No diagnosis. Educational only.
"""
    response = ollama.generate(
        model="llama3",
        prompt=prompt
    )
    return response["response"].strip()


def llama_expand(base_text, user_query):
    prompt = f"""
User symptom: {user_query}
Basic advice: {base_text}

Expand this into a friendly medical guidance paragraph.
Include:
- 2 extra home remedies
- 1 yoga or breathing exercise
- 1 diet suggestion
- 1 warning sign to watch
Keep the tone safe and non-diagnostic.
"""
    response = ollama.generate(
        model="llama3",
        prompt=prompt
    )
    return response["response"].strip()


def extract_medicines_from_image(img):
    text = pytesseract.image_to_string(img)
    found = []

    for word in text.split():
        med = find_medicine(word)
        if med:
            found.append(med)

    return list(set(found)), text


def extract_medicines_with_salts(img):
    text = pytesseract.image_to_string(img)

    prompt = f"""
You are a strict JSON generator.

Extract medicines and their active drug/salt from the prescription.

Rules:
- Output ONLY JSON
- No markdown
- No explanation
- Double quotes only
- If drug unknown, use null

Format:
[
  {{
    "medicine": "string",
    "drug": "string or null"
  }}
]

Text:
{text}
"""
    response = ollama.generate(
        model="llama3",
        prompt=prompt
    )

    raw = response["response"].strip()

    if raw.startswith("```"):
        raw = raw.replace("```json", "").replace("```", "").strip()

    try:
        data = json.loads(raw)
    except Exception:
        st.error("❌ JSON Parsing Failed")
        st.code(raw)
        data = []

    return data, text


if "side_effects" not in st.session_state:
    st.session_state.side_effects = []


def log_side_effect(effect):
    st.session_state.side_effects.append({
        "effect": effect,
        "time": datetime.now().strftime("%d-%m-%Y %H:%M")
    })


def risk_score(symptoms, medicines):
    score = 0

    danger_words = ["chest pain", "blue", "unconscious", "breathless"]
    for d in danger_words:
        if d in symptoms.lower():
            score += 50

    if "ibuprofen" in medicines and "warfarin" in medicines:
        score += 40

    return min(score, 100)


st.set_page_config(page_title="MedSafe AI", layout="wide")
st.title("🩺 MedSafe AI – Intelligent Medicine Safety Assistant")

tabs = st.tabs([
    "💊 Medicine Interaction Checker",
    "📝 Prescription OCR",
    "🤖 Symptom & Doubt Solver",
    "⚠️ Side-Effect Monitor",
    "🚨 Emergency Risk Predictor"
])


with tabs[0]:
    st.header("💊 Medicine Interaction Checker")

    meds = st.text_input(
        "Enter medicines :",
        ""
    )

    if st.button("Check Interactions"):
        med_list = [m.strip() for m in meds.split(",") if m.strip()]

        inter = check_interactions(med_list)

        if inter:
            st.warning("\n".join(inter))
            ai_note = llama_short_warning(inter)
            st.info(f"🤖 AI Note: {ai_note}")
        else:
            st.success("No interaction warnings found.")


with tabs[1]:
    st.header("📝 Extract Medicines From Prescription Image")

    file = st.file_uploader("Upload prescription image", type=["jpg", "png"])

    if file:
        img = Image.open(file)
        st.image(img, caption="Uploaded Prescription", width=400)

        with st.spinner("🔍 Reading prescription..."):
            extracted, raw_text = extract_medicines_with_salts(img)

        st.subheader("💊 Detected Medicines & Drugs")

        if extracted:
            for item in extracted:
                st.write(
                    f"• **{item.get('medicine', 'Unknown')}** "
                    f"→ _{item.get('drug', 'Not specified')}_"
                )
        else:
            st.warning("No medicines detected.")

        with st.expander("📄 Raw OCR Text"):
            st.code(raw_text)


with tabs[2]:
    st.header("🤖 AI Health Assistant")

    query = st.text_area("Describe your symptom:")

    if st.button("Get Advice"):
        symptoms_list = [s.strip() for s in query.replace(" and ", ",").split(",") if s.strip()]
        
        base_advices = []
        for symptom in symptoms_list:
            advice = symptom_advice(symptom)
            base_advices.append(f"{symptom}: {advice}")

        base = "\n\n".join(base_advices)
        st.info("📝 Basic Advice:\n" + base)

        detailed = llama_expand(base, query)
        st.success("🤖 AI Enhanced Advice:\n" + detailed)


with tabs[3]:
    st.header("⚠️ Experience & Side-Effect Monitor")

    age = st.number_input("Enter your age:", min_value=0, max_value=120, value=25, step=1)
    gender = st.selectbox("Select your gender:", ["Male", "Female", "Other"])
    medicine_taken = st.text_input("Enter medicine(s) taken (comma-separated):")
    dose_taken = st.text_input("Enter dose(s) taken (mg, comma-separated if multiple):")
    experience = st.text_area("Describe what you felt after taking the medicine(s):")

    if st.button("Analyze Experience", key="side_effect_analyze"):
        if not medicine_taken or not experience:
            st.warning("Please enter the medicines taken and your experience.")
        else:
            med_list = [m.strip() for m in medicine_taken.split(",") if m.strip()]
            dose_list = [d.strip() for d in dose_taken.split(",")] if dose_taken else []
            user_input = f"Age: {age}, Gender: {gender}, Medicines: {med_list}, Dose: {dose_list}, Experience: {experience}"

            prompt = f"""
You are a medical educational assistant. 

A user reports the following: {user_input}

Generate a short, clear, educational output:
- Give 2 points on what might be causing these experiences.
- Include 1 warning or precaution the user should watch.
- Keep tone informative, not diagnostic, not too short, not too long.
"""

            response = ollama.generate(
                model="llama3",
                prompt=prompt
            )

            st.info(response["response"].strip())


with tabs[4]:
    st.header("🚨 Emergency Risk Predictor")

    s = st.text_area("Describe symptoms:")
    m = st.text_input("Medicines taken:", "ibuprofen, warfarin")

    if st.button("Calculate Risk Score", key="emergency_risk"):
        score = risk_score(s, m)

        st.metric("Emergency Risk Score", f"{score}%")

        if score >= 90:
            level = "LEVEL 7 – CRITICAL RISK"
            msg = "Immediate medical emergency. Call emergency services or rush to the hospital right now."
            st.error(f"🟥 **{level}**\n{msg}")
        elif score >= 75:
            level = "LEVEL 6 – VERY HIGH RISK"
            msg = "Severe symptoms or dangerous medicine combinations detected. Do NOT wait—seek urgent medical care."
            st.error(f"🟧 **{level}**\n{msg}")
        elif score >= 60:
            level = "LEVEL 5 – HIGH RISK"
            msg = "Strong warning signs present. Monitor continuously and get a medical evaluation as soon as possible."
            st.warning(f"🟨 **{level}**\n{msg}")
        elif score >= 45:
            level = "LEVEL 4 – MODERATE RISK"
            msg = "Some risk factors observed. Watch symptoms carefully and consider consulting a doctor."
            st.warning(f"🟨 **{level}**\n{msg}")
        elif score >= 30:
            level = "LEVEL 3 – LOW–MODERATE RISK"
            msg = "Minor concerns detected. Monitor symptoms and follow home-care guidance."
            st.info(f"🟦 **{level}**\n{msg}")
        elif score >= 15:
            level = "LEVEL 2 – LOW RISK"
            msg = "Symptoms appear mild. Maintain hydration and self-monitor."
            st.success(f"🟩 **{level}**\n{msg}")
        else:
            level = "LEVEL 1 – MINIMAL RISK"
            msg = "No significant warning signs detected."
            st.success(f"🟩 **{level}**\n{msg}")

        prompt = f"""
Risk Score: {score}%
Risk Level: {level}

Symptoms: {s}
Medicines: {m}

Explain in 3–4 short lines:
- Why this risk level applies
- One warning sign to watch
Educational only. No diagnosis.
"""

        response = ollama.generate(
            model="llama3",
            prompt=prompt
        )

        st.info("🤖 AI Risk Explanation:\n" + response["response"].strip())
