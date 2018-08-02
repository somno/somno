from django.db import models
from jsonfield import JSONField


class PayloadReceived(models.Model):
    created = models.DateTimeField(auto_now=True)
    data = JSONField()
