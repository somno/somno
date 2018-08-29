from dateutil import parser
from django.db.models import Q
from django.utils import timezone
from opal.models import Patient
from einstein_api import models

# what we get given as the heart rate
HEART_RATE = "NOM_ECG_CARD_BEAT_RATE"


def str_to_datetime(datetime_str):
    return timezone.make_aware(parser.parse(datetime_str))


def handle_payload(payload_dict):
    monitor_id = payload_dict["monitor_id"]
    datetime = str_to_datetime(payload_dict["datetime"])
    observations = payload_dict["observations"]
    update_observations(monitor_id, datetime, observations)


def update_observations(monitor_id, datetime, observations):
    """
    An example observation looks like
    {
        "physio_id": "NOM_ECG_CARD_BEAT_RATE",
        "value": 79,
        "unit_code": "NOM_DIM_BEAT_PER_MIN"
    }
    """
    observations = [i for i in observations if i["physio_id"] == HEART_RATE]
    if not observations:
        return

    patient_ids = models.Pairing.objects.filter(
        monitor__einstein_id=monitor_id
    ).filter(
        start__lte=datetime
    ).filter(
        Q(stop__gt=datetime) | Q(stop=None)
    ).values_list("patient_id", flat=True).distinct()

    patients = Patient.objects.filter(id__in=patient_ids)
    # TODO at the moment we handle multiple patients being
    # added to the same monitor. This is never correct

    for patient in patients:
        for observation in observations:
            # we could bulk update but the time being there will
            # only ever be one
            patient.observation_set.create(
                datetime=datetime,
                pulse=observation["value"]
            )
