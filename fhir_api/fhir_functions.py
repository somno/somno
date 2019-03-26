from fhirclient import client
from fhirclient.models import patient as p
from fhirclient.models import fhirsearch as s
from fhirclient.models import medicationrequest as meds
from fhirclient.models import medication as mednames
from fhirclient.models import condition

from opal.models import Patient

"""A collection of functions that update opal models using fhir resources"""

base_settings = {
    "app_id": "my_web_app", 
    "api_base": "https://r3.smarthealthit.org"
}

def update_model(user, patient, information):
    """ updates opal model using bulk_update
    
    patient is the patient you would like to get e.g Patient.objects.get(id=patient_id)
    information is a dictionary in the form:
    {
        "api_name": [{"model_field": data}]
    }
    
    """

    patient.bulk_update(
        information, user, episode=patient.get_active_episode(), force=True
    )


def update_medications(patient, user, server):
    """ updates medications for a patient

    patient: somno patient_id 
    user: opal user object to allow for bulk update
    server: smart server to which query is made 
    """
    smart = client.FHIRClient(settings=base_settings)
    
    current_patient = Patient.objects.get(id=patient_id)

    medications = meds.MedicationRequest.where(
        struct={"subject": patient.id, "status": "active"}
    ).perform_resources(smart.server)

    medlist = []
    for medication in medications:
        medref = medication.as_json()
        med_object = {
            "name": medref["medicationCodeableConcept"]["text"],
            "dosage": medref["dosageInstruction"][0]["text"],
        }
        medlist.append(med_object)

    update_model(user, current_patient, {"drug_history": [{"Medications": medlist}]})


def update_history(patient, user, server):

    past_med_history = s.FHIRSearch(
        condition.Condition, {"subject": patient_smart_number}
    ).perform_resources(smart.server)