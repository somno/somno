import datetime
import copy
import csv
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.management.base import BaseCommand
from opal import models as omodels
from somno import models

USER = "super"
FILE_LOCATION = "somno/data/example_data.csv"
PATIENT_ID = 1

OBSERVATION_FIELD_NAMES = [
    'bp_systolic',
    'bp_diastolic',
    'pulse',
    'resp_rate',
    'sp02',
    'temperature',
    'datetime'
]

GASES_FIELD_NAMES = [
    'expired_oxygen',
    'inspired_oxygen',
    'expired_aa',
    'expired_carbon_dioxide',
    'datetime'
]

VENTILATION_FIELD_NAMES = [
    'peak_airway_pressure',
    'peep_airway_pressure',
    'tidal_volume',
    'rate',
    'datetime'
]


def serialize_datetime(some_dt):
    input_format = settings.DATETIME_INPUT_FORMATS[0]
    return some_dt.strftime(input_format)


def create_observation(patient, row):
    create_model(models.Observation, patient, row, OBSERVATION_FIELD_NAMES)


def create_gases(patient, row):
    create_model(models.Gases, patient, row, GASES_FIELD_NAMES)


def create_ventilation(patient, row):
    create_model(models.Ventilation, patient, row, VENTILATION_FIELD_NAMES)


def create_model(model_cls, patient, row, fields):
    field_names = model_cls._get_fieldnames_to_serialize()
    unknown_field_names = set(fields) - set(field_names)
    if unknown_field_names:
        raise ValueError("unable to recognise {} for {}".format(
            unknown_field_names, model_cls
        ))
    instance = model_cls()
    instance.patient = patient
    data_to_update = {i: v for i, v in row.items() if i in fields}
    user = User.objects.get(username=USER)
    instance.update_from_dict(data_to_update, user)


class Command(BaseCommand):
    help = "load in some sample data"

    def handle(self, *args, **kwargs):
        now = timezone.now()
        patient, _ = omodels.Patient.objects.get_or_create(id=PATIENT_ID)
        with open(FILE_LOCATION) as fs:
            reader = csv.DictReader(fs)
            for i, row in enumerate(reader):
                start = now - datetime.timedelta(minutes=(20 - i) * 4)
                row_copy = copy.copy(row)
                row_copy["datetime"] = serialize_datetime(start)
                for i, v in row_copy.items():
                    if not v:
                        row_copy[i] = None
                create_observation(patient, row_copy)
                create_gases(patient, row_copy)
                create_ventilation(patient, row_copy)
