from django.db import transaction
from django.utils import timezone
from django.conf import settings

from opal.core.pathway import PagePathway, Step

from einstein_api import models


class UnPairMonitor(PagePathway):
    display_name = "Unpair with monitor"
    slug = "unpair_monitor"
    modal_template = "pathways/modal_only_cancel.html"
    finish_button_text = "Unpair"
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
        patient.monitorpatientpairing_set.filter(stop=None).update(
            stop=timezone.now()
        )
        return patient, episode


class PairMonitor(PagePathway):
    display_name = "Pair with monitor"
    slug = "pair_monitor"
    steps = (
        Step(
            model=models.MonitorPatientPairing,
            step_controller="PairMonitorController",
            multiple=False
        ),
    )

    @transaction.atomic
    def save(self, data, user=None, patient=None, episode=None):
        to_save = data.pop(models.MonitorPatientPairing.get_api_name())[0]
        to_save["patient_id"] = patient.id
        to_save["start"] = timezone.now().strftime(
            settings.DATETIME_INPUT_FORMATS[0]
        )

        monitor_patient_pairing = models.MonitorPatientPairing()
        monitor_patient_pairing.update_from_dict(
            to_save, user
        )
        return patient, episode
