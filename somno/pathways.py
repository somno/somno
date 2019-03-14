from opal.core.pathway import PagePathway, Step
from somno import models
# import json


# from fhirclient import client

settings = {
    'app_id': 'my_web_app',
    'api_base': 'https://r3.smarthealthit.org'
}
# smart = client.FHIRClient(settings=settings)
# import fhirclient.models.patient as p
# import fhirclient.models.medicationrequest as meds
# import fhirclient.models.medication as mednames
# import fhirclient.models as fhirmodels


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


class AnaestheticDetailsPathway(PagePathway):
    display_name = 'Anaesthetic details'
    slug         = 'details'
    template     = 'pathways/anaesthetic_details.html'
    steps        = [
        Step(
            model=models.OperationDetails,
            base_template="pathways/preop_step_base_template.html"
        )
    ]
