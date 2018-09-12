from opal.core import metadata


class DrugTypes(metadata.Metadata):
    slug = 'drug_type'

    @classmethod
    def to_dict(klass, *args, **kwargs):
        return {
            "drug_type": {
                "Antiemetic drug": [
                    "Dexametasone", "Ondansetron", "Granisetron", "Cyclizine",
                    "Metoclopramide"
                ],
                "Induction agent drug": [
                    "Propofol", "Thiopentone", "Etomidate", "Ketamine"
                ],
                "Hypnotic drug": [
                    "Midazolam", "Diazepam", "Lorazepam"
                ],
                "Hypnotic antagonist drug": [
                    "Flumazenil"
                ],
                "Neuromuscular blocking drug": [
                    "Atracurium", "Mivacurium", "Cisatracurium", "Rocuronium",
                    "Vecuronium"
                ],
                "Neuromuscular blocking drug antagonist": [
                    "Neostigmine with glycopyrrolate", "Sugammadex",
                    "Neostigmine"
                ],
                "Depolarizing neuromuscular blocking drug": ["Suxamethonium"],
                "Opioid drug": [
                    "Morphine", "Fentanyl", "Remifentanil", "Alfentanil",
                ],
                "Opioid antagonist": ["Naloxone"],
                "Vasopressor drug": [
                    "Metaraminol", "Phenylephrine", "Noradrenaline",
                    "Adrenaline", "Ephedrine"
                ],
                "Local anaesthetics drug": [
                    "Bupivicaine", "Lidocaine", "Levobupivicaine", "Prilocaine"
                ],
                "Anticholinergic drug": ["Glycopyrrolate", "Atropine"],
                "Other drug agents": [
                    "Cefuroxime", "Metronidazole", "Gentamicin", "Co-amoxiclav"
                ],
            }
        }
class Risks(metadata.Metadata):
    slug = 'risks'

    @classmethod
    def to_dict(klass, *args, **kwargs):
        return {
                "Risks": {
                    "General Anaesthetic": [
                        "PONV", "Dental Damage", "Sore Throat", "Awareness 1:20,000", "Anaphylaxis 1:10,000"
                    ],
                    "Neuraxial Blockade": [
                        "Failure", "PDPH", "Haematoma", "Infection", "Shivering", "Nerve Injury", "Itching"
                    ],
                    "Nerve Block": [
                        "Failure", "Bleeding", "Infection", "Nerve Injury", "Itching"
                    ],
                    "Sedation": [
                        "Awareness", "Discomfort"
                    ],
                    "Central Venous Access": [
                        "Pneumothorax", "Nerve Injury", "Bleeding"
                    ],
                    "Other": [
                        "Arterial Line", "Transfusion", "Intesive Care", "HDU", "Blindness", "Pressure Sore", "Congitive Dysfunction"
                    ],
                }
        }
