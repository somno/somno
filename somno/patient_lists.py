"""
Defining OPAL PatientLists
"""
from opal import core
from opal.models import Episode
from opal.core.patient_lists import TaggedPatientList
from somno import models


class AllPatientsList(core.patient_lists.PatientList):
    display_name = 'All Patients'

    schema = [
        models.Demographics,
        models.Diagnosis,
        models.Treatment
    ]

    def get_queryset(self):
        return Episode.objects.all()


class Theatre1(TaggedPatientList):
    display_name = "Theatre 1"
    tag = "theatre_1"

    schema = [
        models.Demographics,
        models.Diagnosis,
        models.Treatment
    ]


class Theatre2(TaggedPatientList):
    display_name = "Theatre 2"
    tag = "theatre_2"

    schema = [
        models.Demographics,
        models.Diagnosis,
        models.Treatment
    ]


class TodaysList(core.patient_lists.PatientList):
    display_name = "Today's list"
    slug = 'today'

    template_name = "patient_lists/layouts/table_list.html"

    schema = [
        core.patient_lists.Column(
            title="name",
            template_path="patient_lists/name_column.html"
        ),
        core.patient_lists.Column(
            title="hosp",
            template_path="patient_lists/hospital_number_column.html"
        ),
        core.patient_lists.Column(
            title="dob",
            template_path="patient_lists/dob_column.html"
        ),
        core.patient_lists.Column(
            title="links",
            template_path="patient_lists/links_column.html"
        )
    ]

    def get_queryset(self, **kwargs):
        return Episode.objects.all()
