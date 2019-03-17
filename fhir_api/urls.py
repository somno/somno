"""
Urls for the fhir_api Opal plugin
"""
from django.conf.urls import url

from fhir_api import views

urlpatterns = [
    # url(pattern, view)
    url(r'fhir_patient/', views.FhirViewSet.as_view()),
]