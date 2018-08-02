from django.contrib import admin
from reversion.admin import VersionAdmin
from somno import models

admin.site.register(models.Monitor, VersionAdmin)
