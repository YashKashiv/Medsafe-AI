def symptom_advice(symptom: str) -> str:
    symptom = symptom.lower()

    if any(key in symptom for key in ["chest pain", "pressure in chest"]):
        return (
            "⚠️ **Chest Pain – Emergency Symptom**\n"
            "- Could be heart-related, lungs, or gastric issues.\n"
            "- Avoid exertion, sit upright, stay calm.\n"
            "- Perform slow breathing (4 sec inhale, 6 sec exhale).\n"
            "- Do NOT take random painkillers.\n"
            "👉 **Seek immediate medical attention.**"
        )

    if any(key in symptom for key in ["shortness of breath", "breathless", "difficulty breathing"]):
        return (
            "⚠️ **Breathing Difficulty – Severe Symptom**\n"
            "- Sit upright, loosen tight clothing.\n"
            "- Take slow, deep breaths.\n"
            "- Try pursed-lip breathing.\n"
            "- Avoid lying down flat.\n"
            "👉 **Emergency care required immediately.**"
        )

    if any(key in symptom for key in ["severe bleeding", "heavy bleeding"]):
        return (
            "⚠️ **Severe Bleeding**\n"
            "- Apply firm pressure with a clean cloth.\n"
            "- Elevate the bleeding area above heart level.\n"
            "- Keep the person calm and still.\n"
            "- Don’t remove the cloth if blood soaks—add more layers.\n"
            "👉 **Call emergency services NOW.**"
        )


    if "fever" in symptom:
        return (
            "🌡️ **Fever Detected**\n"
            "- Drink warm water or ORS frequently.\n"
            "- Paracetamol 500–650 mg may reduce fever.\n"
            "- Wear light clothing and rest.\n"
            "- Do gentle deep-breathing to relax the body.\n"
            "- Yoga: *Balasana (Child’s pose)* and *Viparita Karani*.\n"
            "- If lasts > 3 days or > 102°F → see a doctor."
        )

    if "headache" in symptom:
        return (
            "🤕 **Headache**\n"
            "- Drink water; dehydration is a common cause.\n"
            "- Rest your eyes away from screens.\n"
            "- Apply a cold compress on forehead.\n"
            "- Yoga: *Shavasana*, *Pranayama*, *Neck rotations*.\n"
            "- If sudden, severe or with vision issues → get checked."
        )

    if "migraine" in symptom:
        return (
            "💫 **Migraine Symptoms**\n"
            "- Sit in a dark, quiet room.\n"
            "- Drink water or ORS.\n"
            "- Cold patch on head helps reduce throbbing.\n"
            "- Yoga: *Bhramari Pranayama*, *Yoga Nidra*.\n"
            "- Avoid loud sounds and bright lights."
        )

    if any(key in symptom for key in ["vomit", "nausea"]):
        return (
            "🤢 **Vomiting / Nausea**\n"
            "- Drink small sips of ORS or ginger water.\n"
            "- Avoid heavy, oily foods.\n"
            "- Eat banana or dry toast.\n"
            "- Yoga: *Vajrasana* after meals.\n"
            "- Persistent vomiting → electrolytes test recommended."
        )

    if "cough" in symptom:
        return (
            "😷 **Cough (Dry or Wet)**\n"
            "- Steam inhalation recommended.\n"
            "- Honey + warm water helps soothe throat.\n"
            "- Avoid cold drinks.\n"
            "- Yoga: *Anulom-Vilom*, *Kapalbhati* (if no fever).\n"
            "- If blood in cough or > 2 weeks → doctor needed."
        )

    if any(key in symptom for key in ["cold", "runny nose", "sneezing"]):
        return (
            "🤧 **Cold / Sneezing / Runny Nose**\n"
            "- Drink warm liquids like soup or kadha.\n"
            "- Try saline nasal drops.\n"
            "- Take steam inhalation.\n"
            "- Yoga: *Jal Neti*, *Anulom-Vilom*.\n"
            "- Usually resolves in 3–5 days."
        )

    if any(key in symptom for key in ["diarrhea", "loose motion"]):
        return (
            "🚰 **Diarrhea / Loose Motion**\n"
            "- ORS is mandatory—frequent sips.\n"
            "- Avoid milk, spicy food, and raw salads.\n"
            "- Eat curd + rice or banana.\n"
            "- Yoga: *Pawanmuktasana* and gentle walking.\n"
            "- If dehydration signs → doctor visit recommended."
        )

    if any(key in symptom for key in ["stomach pain", "abdominal pain"]):
        return (
            "🍽️ **Stomach Pain**\n"
            "- Could be gas, acidity, or infection.\n"
            "- Drink warm water or ajwain water.\n"
            "- Avoid fried/spicy foods.\n"
            "- Yoga: *Pawanmuktasana*, *Cat-Cow pose*.\n"
            "- Sharp pain on right side → urgent evaluation needed."
        )

    if any(key in symptom for key in ["body pain", "body ache", "fatigue"]):
        return (
            "💤 **Body Ache / Fatigue**\n"
            "- Rest well and hydrate.\n"
            "- Take a warm shower to relax muscles.\n"
            "- Light stretching helps.\n"
            "- Yoga: *Child’s pose*, *Seated forward bend*.\n"
            "- Could be viral—monitor for fever."
        )

    if any(key in symptom for key in ["sore throat", "throat pain"]):
        return (
            "🗣️ **Sore Throat**\n"
            "- Warm salt-water gargles twice daily.\n"
            "- Honey + turmeric milk helps.\n"
            "- Avoid cold beverages.\n"
            "- Yoga: *Ujjayi Pranayama*.\n"
            "- If white patches → may need doctor check."
        )

    if any(key in symptom for key in ["back pain", "lower back pain", "backpain"]):
        return (
            "🧍 **Back Pain**\n"
            "- Apply hot compress.\n"
            "- Avoid long sitting hours.\n"
            "- Do gentle stretching.\n"
            "- Yoga: *Bhujangasana*, *Cat-Cow*, *Bridge pose*.\n"
            "- If pain radiates to legs → possible nerve issue."
        )

    if "neck pain" in symptom:
        return (
            "🧘‍♂️ **Neck Pain**\n"
            "- Avoid looking down at mobile for long.\n"
            "- Do slow neck rotations.\n"
            "- Warm compress helps.\n"
            "- Yoga: *Chin tucks*, *Shoulder rolls*.\n"
            "- Persistent stiffness → consider physiotherapy."
        )

    if any(key in symptom for key in ["dizziness", "lightheaded"]):
        return (
            "🌀 **Dizziness / Lightheadedness**\n"
            "- Sit or lie down immediately.\n"
            "- Drink water or ORS (dehydration common).\n"
            "- Check if you skipped meals.\n"
            "- Yoga: *Deep breathing*, avoid fast movements.\n"
            "- Recurring episodes → check BP & sugar."
        )

    if any(key in symptom for key in ["rash", "itch", "itching"]):
        return (
            "🟤 **Skin Rash / Itching**\n"
            "- Keep area clean & dry.\n"
            "- Apply calamine lotion.\n"
            "- Avoid scratching.\n"
            "- Use mild soap & cool showers.\n"
            "- If spreading → may be allergy or infection."
        )

    if "ear pain" in symptom:
        return (
            "👂 **Ear Pain**\n"
            "- Warm compress over ear helps.\n"
            "- Avoid inserting earbuds or oil.\n"
            "- Sometimes due to wax buildup.\n"
            "- Yoga: jaw stretches for ear pressure relief.\n"
            "- Persistent pain → needs medical check."
        )

    if any(key in symptom for key in ["eye pain", "red eye", "red eyes", "eyes pain"]):
        return (
            "👁️ **Eye Pain / Redness**\n"
            "- Wash eyes with clean cold water.\n"
            "- Avoid rubbing eyes.\n"
            "- Reduce screen brightness.\n"
            "- Yoga: *Palming*, *Eye rotations*.\n"
            "- Vision changes → urgent evaluation needed."
        )

    if any(key in symptom for key in ["acidity", "heartburn", "acid reflux"]):
        return (
            "🔥 **Acidity / Heartburn**\n"
            "- Drink cold milk or coconut water.\n"
            "- Avoid tea, coffee, spicy foods.\n"
            "- Eat small meals.\n"
            "- Yoga: *Vajrasana* after meals.\n"
            "- Severe persistent symptoms → check for GERD."
        )

    if "anxiety" in symptom:
        return (
            "😟 **Anxiety / Stress**\n"
            "- Practice slow breathing (box breathing).\n"
            "- Listen to calming music.\n"
            "- Journaling helps release thoughts.\n"
            "- Yoga: *Shavasana*, *Anulom-Vilom*.\n"
            "- Persistent anxiety → consider therapy."
        )

    if "joint pain" in symptom:
        return (
            "🦵 **Joint Pain**\n"
            "- Apply warm compress.\n"
            "- Gentle stretching & movement.\n"
            "- Omega-3 rich foods help inflammation.\n"
            "- Yoga: *Trikonasana*, *Vrikshasana*.\n"
            "- Swelling or redness → get examined."
        )

    if any(key in symptom for key in ["insomnia", "cant sleep", "sleep problem"]):
        return (
            "🌙 **Insomnia / Sleep Trouble**\n"
            "- Avoid screens 1 hour before bed.\n"
            "- Drink warm milk or chamomile tea.\n"
            "- Keep room dark and cool.\n"
            "- Yoga: *Yoga Nidra*, *Pranayama*.\n"
            "- Chronic insomnia → sleep specialist check."
        )

    return (
        "❓ **Symptom not fully recognized.**\n"
        "Try describing it with more details like duration, intensity, and any triggers.\n"
        "If symptoms worsen, consult a healthcare professional."
    )
