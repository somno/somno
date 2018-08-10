import requests
import json
import logging
from django.conf import settings
from django.db import models as db_models
from django.utils import timezone
from jsonfield import JSONField
from opal import models
from einstein_api.exceptions import EinsteinError


logger = logging.getLogger('einstein_api')


class PayloadReceived(db_models.Model):
    created = db_models.DateTimeField(auto_now=True)
    data = JSONField()

    class Meta:
        verbose_name_plural = "Payloads Received"


class Monitor(db_models.Model):
    user_machine_name = db_models.CharField(max_length=256, unique=True)
    einstein_id = db_models.CharField(
        max_length=256, unique=True
    )

    def __str__(self):
        return "{} - {}".format(self.user_machine_name, self.einstein_id)


class Pairing(models.PatientSubrecord):
    start = db_models.DateTimeField(blank=True, null=True)
    stop = db_models.DateTimeField(blank=True, null=True)
    monitor = db_models.ForeignKey(Monitor)
    subscription_id = db_models.IntegerField(unique=True)

    def monitor_options(self):
        return Monitor.objects.all()

    @property
    def new_subscription_url(self):
        return "{}/monitor/{}/subscribe".format(
            settings.EINSTEIN_URL, self.monitor.einstein_id
        )

    @property
    def existing_subscription_url(self):
        return "{}/monitor/{}/subscribe/{}".format(
            settings.EINSTEIN_URL,
            self.monitor.einstein_id,
            self.subscription_id
        )

    @classmethod
    def subscribe(cls, patient_id, monitor_id):
        pairing = cls()
        pairing.patient_id = patient_id

        pairing.monitor = Monitor.objects.get(
            id=monitor_id
        )

        if not settings.EINSTEIN_URL:
            logger.info("Unable to find einstein_api url, not posting")
            if cls.objects.exists():
                sub_id = cls.objects.last().id + 1
            else:
                sub_id = 1
            pairing.subscription_id = sub_id
        else:
            result = requests.post(pairing.new_subscription_url)
            if not result.status_code == 201:
                err_str = 'unable to subscribe to {} {} with {}'.format(
                    pairing.monitor.id,
                    pairing.monitor.user_machine_name,
                    result.status_code
                )
                raise EinsteinError(err_str)
            contents = json.loads(result.content)
            if not contents["subscription_id"]:
                raise EinsteinError(
                    "unable to find subscription id from {}".format(
                        result.content
                    )
                )
            pairing.subscription_id = json.loads(result.content)[
                "subscription_id"
            ]
        pairing.start = timezone.now()
        pairing.save()
        return pairing

    def unsubscribe(self):
        if not settings.EINSTEIN_URL:
            logger.info("Unable to find einstein_api url, not unsubcribing")
            self.stop = timezone.now()
        else:
            result = requests.delete(self.existing_subscription_url)
            if result.status_code not in (200, 204,):
                raise EinsteinError("Unable to delete {}".format(str(self)))
            self.stop = timezone.now()
        self.save()
