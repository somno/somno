from django.contrib import admin
from reversion.admin import VersionAdmin
from einstein_api import models

admin.site.register(models.PayloadReceived)
admin.site.register(models.Monitor, VersionAdmin)
