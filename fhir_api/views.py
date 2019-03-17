"""
Views for the fhir_api Opal Plugin
"""
from django.views.generic import TemplateView

from fhirclient import client
import fhirclient.models.patient as p
import fhirclient.models.fhirsearch as s

class FhirViewSet(TemplateView):

    template_name = "modals/test_fhir.html"

    def get_context_data(request):
        settings = {
            'app_id': 'my_web_app',
            'api_base': 'https://r3.smarthealthit.org'
        }

        smart = client.FHIRClient(settings=settings)
        
        patient = s.FHIRSearch(p.Patient, {'_id': 'smart-7777701'}).perform(smart.server)
        # patient = p.Patient.where(struct={'_id': 'smart-77777701'}).perform_resources(smart.server)
        json_pt = patient.as_json()
        context = {
            "patient": json_pt["entry"]
        }
        print(dir(patient))
        return context