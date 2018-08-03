from django.db import models as db_models
from opal import models
from jsonfield import JSONField


class PayloadReceived(db_models.Model):
    created = db_models.DateTimeField(auto_now=True)
    data = JSONField()

    class Meta:
        verbose_name_plural = "Payloads Received"


class Monitor(db_models.Model):
    user_machine_name = db_models.CharField(max_length=256, unique=True)
    einstein_id = db_models.CharField(max_length=256, unique=True)

    def __str__(self):
        return "{} - {}".format(self.user_machine_name, self.einstein_id)


class MonitorPatientPairing(models.PatientSubrecord):
    start = db_models.DateTimeField(blank=True, null=True)
    stop = db_models.DateTimeField(blank=True, null=True)
    monitor = db_models.ForeignKey(Monitor)

    def monitor_options(self):
        return Monitor.objects.all()
