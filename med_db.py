MED_DB = {
    "ibuprofen": {
        "name": "Ibuprofen",
        "standard_dose_mg": {"adult": 200},
        "interactions": {
            "warfarin": "High – increased bleeding risk (NSAIDs + warfarin).",
            "aspirin": "Moderate – may reduce aspirin cardioprotection; additive GI bleeding risk.",
            "methotrexate": "Moderate – may increase methotrexate toxicity."
        }
    },
    "paracetamol": {
        "name": "Paracetamol (Acetaminophen)",
        "standard_dose_mg": {"adult": 500},
        "interactions": {
            "warfarin": "Moderate — may potentiate anticoagulant effect with chronic high use (monitor INR)."
        }
    },
    "warfarin": {
        "name": "Warfarin",
        "standard_dose_mg": {"adult": 5},
        "interactions": {
            "ibuprofen": "High – increased bleeding risk; avoid concomitant NSAIDs.",
            "aspirin": "High – additive bleeding risk.",
            "amiodarone": "High – potentiates warfarin effect (INR rise).",
            "metronidazole": "High – can increase INR.",
            "trimethoprim-sulfamethoxazole": "High – increases warfarin effect",
            "st_johns_wort": "High – reduces warfarin effect (herbal interaction)."
        }
    },
    "simvastatin": {
        "name": "Simvastatin",
        "standard_dose_mg": {"adult": 20},
        "interactions": {
            "clarithromycin": "High – contraindicated / risk of severe myopathy/rhabdomyolysis.",
            "grapefruit": "High – grapefruit increases statin levels; avoid.",
            "gemfibrozil": "High – increased myopathy risk."
        }
    },
    "atorvastatin": {
        "name": "Atorvastatin",
        "standard_dose_mg": {"adult": 10},
        "interactions": {
            "clarithromycin": "High – CYP3A4 inhibitors increase statin levels; monitor or avoid.",
            "grapefruit": "High – avoid grapefruit juice."
        }
    },
    "rosuvastatin": {
        "name": "Rosuvastatin",
        "standard_dose_mg": {"adult": 10},
        "interactions": {
            "cyclosporine": "High – increases rosuvastatin exposure; dose limits apply.",
            "gemfibrozil": "Moderate – increased myopathy risk."
        }
    },
    "metformin": {"name": "Metformin", "standard_dose_mg": {"adult": 500}, "interactions": {"contrast_media": "High – may increase lactic acidosis risk.", "cimetidine": "Moderate – increases metformin levels.", "alcohol": "Moderate – lactic acidosis risk."}},

    "amoxicillin": {"name": "Amoxicillin", "standard_dose_mg": {"adult": 500}, "interactions": {}},
    "amoxicillin_clavulanic": {"name": "Amoxicillin + Clavulanic Acid (Augmentin)", "standard_dose_mg": {"adult": "500 + 125"}, "interactions": {"warfarin": "Moderate – INR fluctuations.", "allopurinol": "Moderate – rash risk."}},
    "cefuroxime": {"name": "Cefuroxime", "standard_dose_mg": {"adult": 250}, "interactions": {}},
    "cefixime": {"name": "Cefixime", "standard_dose_mg": {"adult": 200}, "interactions": {}},
    "azithromycin": {"name": "Azithromycin", "standard_dose_mg": {"adult": 500}, "interactions": {"statins": "Moderate – increased myopathy risk.", "warfarin": "Moderate – INR elevation."}},
    "clarithromycin": {"name": "Clarithromycin", "standard_dose_mg": {"adult": 250}, "interactions": {"simvastatin": "High – contraindicated.", "atorvastatin": "High – increased toxicity."}},
    "erythromycin": {"name": "Erythromycin", "standard_dose_mg": {"adult": 250}, "interactions": {"warfarin": "High – INR rise.", "theophylline": "Moderate – increases levels."}},
    "doxycycline": {"name": "Doxycycline", "standard_dose_mg": {"adult": 100}, "interactions": {"antacids": "Moderate – reduces absorption.", "iron": "Moderate – reduces absorption."}},
    "levofloxacin": {"name": "Levofloxacin", "standard_dose_mg": {"adult": 500}, "interactions": {"antacids": "High – prevents absorption.", "warfarin": "Moderate – INR changes."}},
    "ciprofloxacin": {"name": "Ciprofloxacin", "standard_dose_mg": {"adult": 500}, "interactions": {"theophylline": "High – toxicity.", "tizanidine": "High – contraindicated.", "warfarin": "Moderate – INR alteration."}},

    "diclofenac": {"name": "Diclofenac", "standard_dose_mg": {"adult": 50}, "interactions": {"warfarin": "High – bleeding.", "ace_inhibitors": "Moderate – renal impairment."}},
    "naproxen": {"name": "Naproxen", "standard_dose_mg": {"adult": 250}, "interactions": {"warfarin": "High – bleeding.", "aspirin": "Moderate – GI risk."}},
    "ketorolac": {"name": "Ketorolac", "standard_dose_mg": {"adult": 10}, "interactions": {"warfarin": "High – severe bleeding.", "NSAIDs": "High – contraindicated together."}},
    "aceclofenac": {"name": "Aceclofenac", "standard_dose_mg": {"adult": 100}, "interactions": {"warfarin": "High – bleeding.", "methotrexate": "Moderate – toxicity risk."}},
    "tramadol": {"name": "Tramadol", "standard_dose_mg": {"adult": 50}, "interactions": {"SSRIs": "High – serotonin syndrome.", "MAOIs": "High – contraindicated."}},

    "cetirizine": {"name": "Cetirizine", "standard_dose_mg": {"adult": 10}, "interactions": {"alcohol": "Moderate – sedation."}},
    "loratadine": {"name": "Loratadine", "standard_dose_mg": {"adult": 10}, "interactions": {}},
    "fexofenadine": {"name": "Fexofenadine", "standard_dose_mg": {"adult": 120}, "interactions": {"fruit_juices": "Moderate – reduces absorption."}},
    "levocetirizine": {"name": "Levocetirizine", "standard_dose_mg": {"adult": 5}, "interactions": {"alcohol": "Moderate – sedation."}},
    "montelukast": {"name": "Montelukast", "standard_dose_mg": {"adult": 10}, "interactions": {}},

    "omeprazole": {"name": "Omeprazole", "standard_dose_mg": {"adult": 20}, "interactions": {"clopidogrel": "High – reduces activation.", "diazepam": "Moderate – increases levels."}},
    "pantoprazole": {"name": "Pantoprazole", "standard_dose_mg": {"adult": 40}, "interactions": {"clopidogrel": "Moderate – reduces activation."}},
    "rabeprazole": {"name": "Rabeprazole", "standard_dose_mg": {"adult": 20}, "interactions": {}},
    "famotidine": {"name": "Famotidine", "standard_dose_mg": {"adult": 20}, "interactions": {}},
    "sucralfate": {"name": "Sucralfate", "standard_dose_mg": {"adult": 1}, "interactions": {"antibiotics": "Moderate – reduced absorption."}},

    "crocin": {"name": "Crocin (Paracetamol)", "standard_dose_mg": {"adult": 500}, "interactions": {"alcohol": "High – liver toxicity.", "warfarin": "Moderate – INR rise."}},
    "disprin": {"name": "Disprin (Aspirin)", "standard_dose_mg": {"adult": 325}, "interactions": {"warfarin": "High – bleeding.", "ibuprofen": "Moderate – reduces cardioprotection."}},
    "dolo_650": {"name": "Dolo 650", "standard_dose_mg": {"adult": 650}, "interactions": {"alcohol": "High – liver toxicity.", "warfarin": "Moderate – INR rise."}},

    "sinarest": {"name": "Sinarest", "standard_dose_mg": {"adult": None}, "interactions": {"alcohol": "High – sedation.", "maoi": "High – hypertensive crisis."}},
    "vicks_action_500": {"name": "Vicks Action 500", "standard_dose_mg": {"adult": None}, "interactions": {"maoi": "High – hypertension.", "caffeine": "Moderate – jitteriness."}},
    "meftal_spas": {"name": "Meftal Spas", "standard_dose_mg": {"adult": None}, "interactions": {"warfarin": "High – bleeding.", "anticholinergics": "Moderate – dryness."}},
    "domperidone": {"name": "Domperidone", "standard_dose_mg": {"adult": 10}, "interactions": {"ketoconazole": "High – QT risk.", "erythromycin": "High – arrhythmia."}},
    "cyclopam": {"name": "Cyclopam", "standard_dose_mg": {"adult": None}, "interactions": {"alcohol": "Moderate – sedation."}},

    "augmentin": {"name": "Augmentin (Amoxicillin + Clavulanic)", "standard_dose_mg": {"adult": "500+125"}, "interactions": {"warfarin": "Moderate – INR fluctuation."}}
,
    "combiflam": {
        "name": "Combiflam (Ibuprofen + Paracetamol)",
        "standard_dose_mg": {"adult": "Ibuprofen 400 + Paracetamol 325"},
        "interactions": {
            "warfarin": "High – ibuprofen increases bleeding risk.",
            "aspirin": "Moderate – NSAID interaction; GI bleeding.",
            "methotrexate": "Moderate – increased toxicity.",
            "alcohol": "Moderate – paracetamol liver toxicity."
        }
    },
    "dextropropoxyphene": {
        "name": "Dextropropoxyphene",
        "standard_dose_mg": {"adult": 65},
        "interactions": {
            "alcohol": "High – respiratory depression.",
            "benzodiazepines": "High – sedation and respiratory suppression."
        }
    },
    "ranitidine": {
        "name": "Ranitidine",
        "standard_dose_mg": {"adult": 150},
        "interactions": {
            "ketoconazole": "Moderate – reduced absorption."
        }
    },
    "insulin": {
        "name": "Insulin",
        "standard_dose_mg": {"adult": None},
        "interactions": {
            "beta_blockers": "Moderate – may mask hypoglycaemia symptoms.",
            "corticosteroids": "Moderate – may increase insulin requirements."
        }
    },
    "antacid": {
        "name": "Antacid",
        "standard_dose_mg": {"adult": None},
        "interactions": {
            "doxycycline": "Moderate – reduced absorption.",
            "fluoroquinolones": "High – binding reduces effect."
        }
    },
    "ORS": {
        "name": "Oral Rehydration Salts",
        "standard_dose_mg": {"adult": None},
        "interactions": {}
    },
    "vitamin_c": {
        "name": "Vitamin C",
        "standard_dose_mg": {"adult": 500},
        "interactions": {}
    },
    "multivitamin": {
        "name": "Multivitamin",
        "standard_dose_mg": {"adult": None},
        "interactions": {
            "iron": "Moderate – reduces absorption."
        }
    },
    "zinc_tablet": {
        "name": "Zinc",
        "standard_dose_mg": {"adult": 50},
        "interactions": {
            "antibiotics": "Moderate – reduces absorption of tetracyclines."
        }
    },
    "betadine_gargle": {
        "name": "Betadine Gargle",
        "standard_dose_mg": {"adult": None},
        "interactions": {}
    },
    "abciximab": {
        "name": "Abciximab",
        "standard_dose_mg": {
            "adult": {
                "loading_dose": "0.25 mg/kg IV bolus 10–60 min before PCI",
                "maintenance_infusion": "0.125 μg/kg/min IV infusion (max 10 μg/min) for 12 hours"
            }
        },
        "interactions": {
            "heparin": "High – Increased bleeding risk when used concomitantly with anticoagulants.",
            "aspirin": "High – Additive antiplatelet activity increases bleeding risk.",
            "clopidogrel": "High – Additive antiplatelet effect; higher bleeding risk.",
            "NSAIDs": "Moderate – May further increase bleeding risk."
        }
    },

    "vomilast": {
        "name": "Vomilast",
        "standard_dose_mg": {
            "adult": {
                "doxylamine_succinate": "10 mg",
                "pyridoxine_hcl": "10 mg",
                "folic_acid": "2.5 mg"
            }
        },
        "interactions": {
            "alcohol": "Moderate – Increased drowsiness and sedation.",
            "MAO_inhibitors": "Moderate – Avoid use with MAO inhibitors."
        }
    },

    "doxylamine": {
        "name": "Doxylamine",
        "standard_dose_mg": {
            "adult": {
                "sleep_or_insomnia": "10–25 mg at bedtime (OTC sleep aid)",
                "pregnancy_nausea_combination": "10–20 mg when combined with pyridoxine as prescribed"
            }
        },
        "interactions": {
            "alcohol": "Moderate – increases sedation and drowsiness when taken with alcohol.", 
            "sedatives_and_antihistamines": "Moderate – additive CNS depression with other sedating drugs (e.g., diphenhydramine, zolpidem).",
            "MAO_inhibitors": "Major – risk of severe sedation if used with MAO inhibitors.",
            "other_antihistamines": "Moderate – may increase drowsiness and dry mouth."
        }
    },
    "pyridoxine": {
        "name": "Pyridoxine (Vitamin B6)",
        "standard_dose_mg": {
            "adult": {
                "RDA": "1.3–2.0 mg/day (varies by age and pregnancy status)",
                "nausea_in_pregnancy": "10–25 mg 3–4 times per day (often used with doxylamine)"
            }
        },
        "interactions": {
            "isoniazid": "Moderate – may increase urinary loss and require supplementation.",
            "levodopa": "Moderate – may reduce levodopa’s effect unless given with a decarboxylase inhibitor.",
            "antiepileptic_drugs": "Moderate – some anti‑seizure medications increase pyridoxine metabolism.",
            "high_doses": "Caution – chronic high doses (>100 mg/day) may cause peripheral neuropathy."
        }
    },
    "folic_acid": {
        "name": "Folic Acid (Vitamin B9)",
        "standard_dose_mg": {
            "adult": {
                "RDA": "0.4 mg (400 mcg) daily for adults, increased to 0.6 mg in pregnancy",
                "pregnancy_support": "0.4–0.8 mg daily to prevent neural tube defects"
            }
        },
        "interactions": {
            "vitamin_B12_deficiency": "Important – may mask B12 deficiency if taken alone in high doses.",
            "high_dose_vitamin_B6": "Possible – high B6 doses can lower folate levels.",
            "anticonvulsants": "Moderate – some seizure medications may reduce folic acid levels."
        }
    },

    "zoclar": {
        "name": "Zoclar",
        "standard_dose_mg": {
            "adult": {
                "zoclar": "Unknown, product specific"
            }
        },
        "interactions": {}
    },

    "gestakind_sr": {
        "name": "Gestakind SR",
        "standard_dose_mg": {
            "adult": {
                "isoxsuprine": "40 mg"
            }
        },
        "interactions": {
            "antihypertensives": "Moderate – additive blood pressure lowering effect.",
            "alcohol": "Moderate – May worsen dizziness or hypotension."
        },
    "azithral_500": {
        "name": "Azithral 500 (Azithromycin)",
        "standard_dose_mg": {"adult": 500},
        "interactions": {
            "warfarin": "Moderate – INR elevation.",
            "QT_drugs": "High – QT prolongation risk.",
            "digoxin": "Moderate – increases levels."
        }
    }
}
}