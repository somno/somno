"""
somno models.
"""
from datetime import datetime
from django.db import models as db_models
from django.contrib.auth.models import User

from opal.core import fields
from opal import models
from opal.core import lookuplists

class Demographics(models.Demographics): pass
class Location(models.Location): pass
class Allergies(models.Allergies): pass
class Diagnosis(models.Diagnosis): pass
class PastMedicalHistory(models.PastMedicalHistory): pass
class Treatment(models.Treatment): pass
class Investigation(models.Investigation): pass


class AnaestheticDrug(lookuplists.LookupList):
    pass


class AnaestheticDrugType(lookuplists.LookupList):
    pass


class GivenDrug(models.PatientSubrecord):
    _sort           = 'datetime'

    drug_name   = fields.ForeignKeyOrFreeText(AnaestheticDrug)
    drug_type   = fields.ForeignKeyOrFreeText(AnaestheticDrugType)
    dose       = db_models.CharField(max_length=255)
    datetime    = db_models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = "Drug"


class Infusion(models.PatientSubrecord):
    start_time = db_models.DateTimeField(blank=True, null=True)
    stopped_time = db_models.DateTimeField(blank=True, null=True)
    drug_name = fields.ForeignKeyOrFreeText(AnaestheticDrug)
    drug_type = fields.ForeignKeyOrFreeText(AnaestheticDrugType)
    rate = db_models.CharField(blank=True, default="", max_length=255)


class RemoteAdded(models.PatientSubrecord):
    class Meta:
        abstract = True

    def set_created_by_id(self, incoming_value, user, *args, **kwargs):
        pass

    def set_updated_by_id(self, incoming_value, user, *args, **kwargs):
        pass


class PatientPhysicalAttributes(models.PatientSubrecord):
    height       = db_models.FloatField(blank=True, null=True)
    weight       = db_models.FloatField(blank=True, null=True)


class Observation(RemoteAdded):
    _sort           = 'datetime'
    _icon           = 'fa fa-line-chart'
    _list_limit     = 1
    _angular_service = 'ObservationRecord'

    bp_systolic  = db_models.FloatField(blank=True, null=True)
    bp_diastolic = db_models.FloatField(blank=True, null=True)
    pulse        = db_models.FloatField(blank=True, null=True)
    resp_rate    = db_models.FloatField(blank=True, null=True)
    sp02         = db_models.FloatField(blank=True, null=True)
    temperature  = db_models.FloatField(blank=True, null=True)
    datetime     = db_models.DateTimeField()

class MaskVent(lookuplists.LookupList): pass
class airway(lookuplists.LookupList): pass
class CormackLehane(lookuplists.LookupList): pass
class Position(lookuplists.LookupList): pass
class Induction_type(lookuplists.LookupList): pass

class Induction(models.EpisodeSubrecord):
    _is_singleton = True

    MaskVent        = fields.ForeignKeyOrFreeText(MaskVent)
    Airway          = fields.ForeignKeyOrFreeText(airway)
    CormackLehane   = fields.ForeignKeyOrFreeText(CormackLehane)
    Size            = db_models.FloatField(blank=True, null=True)
    Description     = db_models.TextField(blank=True, null=True)
    Propofol_dose   = db_models.FloatField(blank=True, null=True, default="200")
    Atracurium_dose = db_models.FloatField(blank=True, null=True,)
    Fentanyl_dose   = db_models.FloatField(blank=True, null=True, default="100")
    Induction_type  = fields.ForeignKeyOrFreeText(Induction_type)
    Position        = fields.ForeignKeyOrFreeText(Position)


class AnaestheticNote(models.PatientSubrecord):
    Title       = db_models.TextField(blank=True, null=True)
    Description = db_models.TextField(blank=True, null=True)
    datetime    = db_models.DateTimeField(blank=True, null=True)


class Gases(RemoteAdded):
    inspired_carbon_dioxide = db_models.FloatField(blank=True, null=True)
    expired_carbon_dioxide = db_models.FloatField(blank=True, null=True)
    inspired_oxygen = db_models.FloatField(blank=True, null=True)
    expired_oxygen = db_models.FloatField(blank=True, null=True)
    expired_aa = db_models.FloatField(blank=True, null=True)
    datetime = db_models.DateTimeField()


class Ventilation(RemoteAdded):
    mode = db_models.CharField(max_length=255)
    peak_airway_pressure = db_models.FloatField(blank=True, null=True)
    peep_airway_pressure = db_models.FloatField(blank=True, null=True)
    tidal_volume = db_models.FloatField(blank=True, null=True)
    rate = db_models.IntegerField(blank=True, null=True)
    datetime = db_models.DateTimeField()


class Bloods(models.EpisodeSubrecord):
    _is_singleton = True

    Hb = db_models.FloatField(blank=True, null=True)
    Plt = db_models.FloatField(blank=True, null=True)
    WBC = db_models.FloatField(blank=True, null=True)
    INR = db_models.FloatField(blank=True, null=True)
    CRP = db_models.FloatField(blank=True, null=True)

    Urea = db_models.FloatField(blank=True, null=True)
    Creat = db_models.FloatField(blank=True, null=True)
    Na = db_models.FloatField(blank=True, null=True)
    K = db_models.FloatField(blank=True, null=True)


class Malampati(lookuplists.LookupList): pass
class Dentition(lookuplists.LookupList): pass
class FrailtyScale(lookuplists.LookupList): pass
class ASA(lookuplists.LookupList): pass
class PreviousAnaesthetics(lookuplists.LookupList): pass

class ProposedProcedure(lookuplists.LookupList): pass
class Risks(lookuplists.LookupList): pass

class AnaestheticPlan(models.EpisodeSubrecord):
    Proposed_Procedure  = fields.ForeignKeyOrFreeText(ProposedProcedure)
    Procedure_Risks     = db_models.TextField(blank=True, null=True)
    Risks               = fields.ForeignKeyOrFreeText(Risks)


class AnaestheticAssesment(models.EpisodeSubrecord):
    _is_singleton = True

    Malampati   = fields.ForeignKeyOrFreeText(Malampati)
    Dentition   = fields.ForeignKeyOrFreeText(Dentition)
    ASA         = fields.ForeignKeyOrFreeText(ASA)
    Frailty     = fields.ForeignKeyOrFreeText(FrailtyScale)
    previous_anaesthetics = fields.ForeignKeyOrFreeText(PreviousAnaesthetics)

    Assessment  = db_models.TextField(blank=True, null=True)
    General_Risks = db_models.TextField(blank=True, null=True,)
    AdditionalRisks = db_models.TextField(blank=True, null=True)
    TimeSeen = db_models.DateTimeField(blank=True, null=True,)


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
