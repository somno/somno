from django.conf import settings
from opal.core.pathway import PagePathway, Step
from fhirclient import client

settings = {
    'app_id': 'my_web_app',
    'api_base': 'https://r3.smarthealthit.org'
}
smart = client.FHIRClient(settings=settings)
import fhirclient.models.patient as p
import fhirclient.models.medicationrequest as meds
import fhirclient.models.medication as mednames
import fhirclient.models as fhirmodels

from somno import models


class DrugPathway(PagePathway):
    display_name = "Induction Drugs"
    slug = "induction_drugs"
    steps = (Step(
        template="pathways/induction_drugs.html",
        display_name="blah",
        icon="fa fa icon",
        step_controller="InductionDrugController"
    ),)


class InfusionPathway(PagePathway):
    display_name = "Infusion Pathway"
    slug = "infusion_pathway"
    steps = (
        Step(
            template="pathways/new_infusions.html",
            display_name="New Infusions",
            step_controller="NewInfusionsController",
            model=models.Infusion
        ),
    )


class PreOpPathway(PagePathway):
    display_name = "Pre Op"
    slug         = "preop"
    template     = "pathways/preop.html"

    steps = [
        Step(
            model=models.PatientPhysicalAttributes,
            base_template="pathways/preop_step_base_template.html"
        ),
        Step(
            model=models.AnaestheticAssesment,
            base_template="pathways/preop_step_base_template.html"
        ),
        Step(
            model=models.DrugHistory,
            base_template="pathways/preop_step_base_template.html"
        ),
        Step(
            model=models.AirwayAssessment,
            base_template="pathways/preop_step_base_template.html"
        ),
        Step(
            model=models.Bloods,
            base_template="pathways/preop_step_base_template.html"
        ),
        Step(
            model=models.AnaestheticPlan,
            base_template="pathways/preop_step_base_template.html"
        )
    ]

    def redirect_url(self, **kwargs):
        return settings.LOGIN_REDIRECT

class FhirPathway(PagePathway):
    display_name = "Smart Fhir"
    slug = "fhir"
    steps = [Step(
        model=models.DrugHistory,
        base_template="pathways/preop_step_base_template.html"
    )]

    print ("FHIR!!!!")
    patient = p.Patient.read('2c4c5104-6d23-4c0a-97e9-bd229fc3559c', smart.server)
    print (patient)

    print ("medications")
    search = meds.MedicationRequest.where(struct={'subject': '2c4c5104-6d23-4c0a-97e9-bd229fc3559c', 'status': 'active'})
    medications = search.perform_resources(smart.server)
    for medication in medications:
        medref = medication.medicationReference.reference
        print (medref)
        # med = mednames.read(medref, smart.server)
