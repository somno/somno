from django.db import transaction
from opal.core.pathway import PagePathway, Step

from einstein_api import models


class UnPairMonitor(PagePathway):
    display_name = "Disconnect from monitor"
    slug = "unpair_monitor"
    modal_template = "pathways/modal_only_cancel.html"
    finish_button_text = "Disconnect"
    finish_button_icon = "fa fa-sign-out"

    steps = (
        Step(
            display_name="UnpairMonitor",
            template="pathways/unpair.html",
            step_controller="UnPairMonitorController"
        ),
    )

    @transaction.atomic
    def save(self, data, user=None, patient=None, episode=None):
        pairings = models.Pairing.objects.filter(
            patient=patient,
            stop=None
        )
        for pairing in pairings:
            pairing.unsubscribe()
        return patient, episode


class PairMonitor(PagePathway):
    display_name = "Pair with monitor"
    modal_template = 'pathways/modal_without_patient_header.html'
    slug = "pair_monitor"
    finish_button_text = 'Pair'
    finish_button_icon = ''
    steps = (
        Step(
            model=models.Pairing,
            step_controller="PairMonitorController",
            multiple=False
        ),
    )

    @transaction.atomic
    def save(self, data, user=None, patient=None, episode=None):
        monitor_id = data.pop(
            models.Pairing.get_api_name()
        )[0]["monitor_id"]

        models.Pairing.subscribe(patient.id, monitor_id)
        return patient, episode
