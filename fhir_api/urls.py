"""
Urls for the fhir_api Opal plugin
"""
from django.conf.urls import url

from fhir_api import views

urlpatterns = [
    # url(pattern, view)
    # (?P<model>[0-9a-z_\-]+)
    # url(r'fhir_patient/<int:patient_id>/<int:episode_id>/<int:hospital_number>/', views.FhirViewSet.as_view()),
    url(
        r"fhir_patient/(?P<patient_id>[0-9a-z_\-]+)/(?P<episode_id>[0-9a-z_\-]+)/(?P<hospital_number>[0-9a-z_\-]+)",
        views.FhirViewSet.as_view(),
    )
]
