from django.conf import settings
from opal.core.pathway import PagePathway, Step
from fhirclient import client

settings = {
    'app_id': 'my_web_app',
    'api_base': 'https://r3.smarthealthit.org'
}
smart = client.FHIRClient(settings=settings)
import fhirclient.models.patient as p

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
    patient = p.Patient.read('SMART-PROMs-55', smart.server)
    print (patient.birthDate.isostring)
