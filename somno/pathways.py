from opal.core.pathway import PagePathway, Step
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
