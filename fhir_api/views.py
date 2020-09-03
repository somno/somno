"""
Views for the fhir_api Opal Plugin
"""
import pprint
from django.views.generic.base import RedirectView
from django.shortcuts import redirect
from opal.models import Patient, UserProfile

from fhirclient import client
import fhirclient.models.patient as p
import fhirclient.models.fhirsearch as s
import fhirclient.models.medicationrequest as meds
from fhirclient.models import medication as mednames
from fhirclient.models import condition


class FhirViewSet(RedirectView):

    template_name = "modals/test_fhir.html"

    def get_redirect_url(self, patient_id, episode_id, hospital_number):

        patient_smart_number = "smart-8888804"
        settings = {"app_id": "my_web_app", "api_base": "https://r3.smarthealthit.org"}

        smart = client.FHIRClient(settings=settings)

        patient = s.FHIRSearch(p.Patient, {"_id": patient_smart_number}).perform(
            smart.server
        )
        json_pt = patient.as_json()

        patient = json_pt["entry"][0]["resource"]
        patient_object = {
            "birthdate": patient["birthDate"],
            "first_name": patient["name"][0]["given"][0],
            "surname": patient["name"][0]["family"],
        }

        medications = meds.MedicationRequest.where(
            struct={"subject": patient_smart_number, "status": "active"}
        ).perform_resources(smart.server)
        medlist = []
        for medication in medications:
            medref = medication.as_json()
            med_object = {
                "drug": medref["medicationCodeableConcept"]["text"],
                "dose": medref["dosageInstruction"][0]["text"],
            }
            medlist.append(med_object)

        past_med_history = s.FHIRSearch(
            condition.Condition, {"subject": patient_smart_number}
        ).perform_resources(smart.server)
        pmh = []
        for past_history in past_med_history:
            disease = past_history.code.as_json()
            pmh.append(
                {
                    "condition": disease["coding"][0]["display"]
                }
            )
            
        current_patient = Patient.objects.get(id=patient_id)
        current_episode = current_patient.get_active_episode()

        current_patient.bulk_update(
            {
                "demographics": [{"hospital_number": hospital_number}],
                "treatment": medlist,
                "past_medical_history": pmh,
            },
            self.request.user,
            episode=current_episode,
            force=True,
        )

        old_url = "/pathway/#/preop/{}/{}".format(patient_id, episode_id)
        return old_url
