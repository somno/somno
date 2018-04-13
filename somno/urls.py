from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

from opal.urls import urlpatterns as opatterns

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += opatterns
