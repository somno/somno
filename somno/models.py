"""
Somno models.

This file is divided into three sections:

1. Lookuplists
2. Concrete definitions of core Opal Models
3. Somno models
"""
from django.db import models as db_models

from opal.core import fields
from opal import models
from opal.core import lookuplists


"""
Section 1: Lookuplists
"""


class AnaestheticDrug(lookuplists.LookupList):
    pass


class AnaestheticDrugType(lookuplists.LookupList):
    pass


class Fluids(lookuplists.LookupList):
    pass


class MaskVent(lookuplists.LookupList):
    pass


class airway(lookuplists.LookupList):
    pass


class CormackLehane(lookuplists.LookupList):
    pass


class Position(lookuplists.LookupList):
    pass


class Induction_type(lookuplists.LookupList):
    pass


class EventType(lookuplists.LookupList):
    pass


class Malampati(lookuplists.LookupList):
    pass


class Dentition(lookuplists.LookupList):
    pass


class ASA(lookuplists.LookupList):
    pass


class PreviousAnaesthetics(lookuplists.LookupList):
    pass


class ProposedProcedure(lookuplists.LookupList):
    """
    An anaesthetic procedure - e.g. Block, Art line
    """


class Surgeon(lookuplists.LookupList):
    """
    A person booked to conduct surgery e.g. Dr Hunter
    """


class Anaesthetist(lookuplists.LookupList):
    """
    A person who conducts an anaesthetic
    """


class Risks(lookuplists.LookupList):
    pass


class Procedure(lookuplists.LookupList):
    """
    A procedure that could be undertaken for an operation
    """


class ProcedureType(lookuplists.LookupList):
    """
    The Broad category of Anaesthetic procedure which we'll perform eg. CVC insertion
    """


class ProcedureName(lookuplists.LookupList):
    """
    The Specific name of the procedure e.g. Subclavian line insertion
    """


class ProcedureDevice(lookuplists.LookupList):
    """
    What we used to perform the procedure e.g. Whittaker needle
    """


class BodySite(lookuplists.LookupList):
    """
    Where bit of the body did we do that procdure on
    """


class ProcedureTechnique(lookuplists.LookupList):
    pass


class ProcedureSterility(lookuplists.LookupList):
    pass


class ProcedureUltrasound(lookuplists.LookupList):
    pass

"""
Section 2: Concrete implementations of core Opal models
"""


class Demographics(models.Demographics):
    pass


class Location(models.Location):
    pass


class Allergies(models.Allergies):
    pass


class Diagnosis(models.Diagnosis):
    pass


class PastMedicalHistory(models.PastMedicalHistory):
    pass


class Treatment(models.Treatment):
    pass


class Investigation(models.Investigation):
    pass


"""
Section 3: Somno models
"""


class GivenDrug(models.PatientSubrecord):
    _sort           = 'datetime'

    drug_name   = fields.ForeignKeyOrFreeText(
        AnaestheticDrug,
        verbose_name="Name"
    )
    drug_type   = fields.ForeignKeyOrFreeText(AnaestheticDrugType)
    dose        = db_models.CharField(max_length=255)
    units       = db_models.CharField(max_length=255, blank=True, null=True)
    datetime    = db_models.DateTimeField(
        blank=True, null=True, verbose_name="Start"
    )

    class Meta:
        verbose_name = "Drug"


class Infusion(models.PatientSubrecord):
    _angular_service = 'InfusionRecord'

    start_time    = db_models.DateTimeField(
        blank=True, null=True, verbose_name="Start"
    )
    stopped_time  = db_models.DateTimeField(blank=True, null=True)
    drug_name     = fields.ForeignKeyOrFreeText(
        AnaestheticDrug, verbose_name="Name"
    )
    drug_type     = fields.ForeignKeyOrFreeText(AnaestheticDrugType)
    rate          = db_models.CharField(blank=True, default="", max_length=255)
    concentration = db_models.CharField(blank=True, null=True, max_length=255)
    units         = db_models.CharField(max_length=255, blank=True, null=True)


class GivenFluids(models.PatientSubrecord):

    fluid = fields.ForeignKeyOrFreeText(Fluids)
    volume = db_models.FloatField(blank=True, null=True)
    unit_number = db_models.CharField(max_length=255, blank=True, null=True)
    given_time    = db_models.DateTimeField(
        blank=True, null=True, verbose_name="Time"
    )

    class Meta:
        verbose_name = "Fluids"


class RemoteAdded(models.PatientSubrecord):
    class Meta:
        abstract = True

    def set_created_by_id(self, incoming_value, user, *args, **kwargs):
        pass

    def set_updated_by_id(self, incoming_value, user, *args, **kwargs):
        pass


class PatientPhysicalAttributes(models.PatientSubrecord):

    _is_singleton = True

    class Meta:
        verbose_name = "Physical Attributes"

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


class Induction(models.EpisodeSubrecord):
    _is_singleton = True

    MaskVent        = fields.ForeignKeyOrFreeText(MaskVent)
    Airway          = fields.ForeignKeyOrFreeText(airway)
    CormackLehane   = fields.ForeignKeyOrFreeText(CormackLehane)
    Size            = db_models.FloatField(blank=True, null=True)
    Description     = db_models.TextField(blank=True, null=True)
    Propofol_dose   = db_models.FloatField(
        blank=True, null=True, default="200"
    )
    Atracurium_dose = db_models.FloatField(blank=True, null=True,)
    Fentanyl_dose   = db_models.FloatField(
        blank=True, null=True, default="100"
    )
    Induction_type  = fields.ForeignKeyOrFreeText(Induction_type)
    Position        = fields.ForeignKeyOrFreeText(Position)


class AnaestheticNote(models.PatientSubrecord):

    _angular_service = 'EventRecord'

    name        = fields.ForeignKeyOrFreeText(EventType)
    description = db_models.TextField(blank=True, null=True)
    datetime    = db_models.DateTimeField(
        blank=True, null=True,
        verbose_name="Time"
    )


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


class AnaestheticPlan(models.EpisodeSubrecord):
    _is_singleton = True

    Proposed_Procedure  = fields.ForeignKeyOrFreeText(ProposedProcedure)
    Procedure_Risks     = db_models.TextField(blank=True, null=True)
    Risks               = fields.ForeignKeyOrFreeText(Risks)


class AnaestheticAssesment(models.EpisodeSubrecord):

    _is_singleton = True

    previous_anaesthetics = fields.ForeignKeyOrFreeText(PreviousAnaesthetics)
    assessment            = db_models.TextField(blank=True, null=True)
    asa                   = fields.ForeignKeyOrFreeText(
        ASA, verbose_name="ASA"
    )
    fasting_status        = db_models.TextField(
        blank=True, null=True, verbose_name="Fasting status"
    )
    smoking_status        = db_models.TextField(
        blank=True, null=True, verbose_name="Smoking status"
    )
    exercise_tolerance    = db_models.TextField(
        blank=True, null=True, verbose_name="Exercise tolerance"
    )
    time_seen             = db_models.DateTimeField(blank=True, null=True,)


class AirwayAssessment(models.EpisodeSubrecord):
    _is_singleton = True

    mouth_opening = db_models.FloatField(
        blank=True, null=True, verbose_name="Mouth opening"
    )
    jaw_protusion = fields.ForeignKeyOrFreeText(
        ASA, verbose_name="Jaw protrusion"
    )
    malampati     = fields.ForeignKeyOrFreeText(Malampati)
    dentition     = fields.ForeignKeyOrFreeText(Dentition)


class DrugHistory(models.EpisodeSubrecord):

    _is_singleton = True

    Medications = db_models.TextField(blank=True, null=True)
    Allergies = db_models.TextField(blank=True, null=True)


class AnaestheticProcedure(models.EpisodeSubrecord):

    Procedure_Type = fields.ForeignKeyOrFreeText(ProcedureType)
    Procedure_Name = fields.ForeignKeyOrFreeText(ProcedureName)
    Device_Used = fields.ForeignKeyOrFreeText(ProcedureDevice)
    Body_Site = fields.ForeignKeyOrFreeText(BodySite)
    Technique = fields.ForeignKeyOrFreeText(ProcedureTechnique)
    Number_Of_Attempts = db_models.FloatField(blank=True, null=True)
    Depth_Of_Space = db_models.FloatField(blank=True, null=True)
    Catheter_Left_In = db_models.FloatField(blank=True, null=True)
    Sterility = fields.ForeignKeyOrFreeText(ProcedureSterility)
    Ultrasound = fields.ForeignKeyOrFreeText(ProcedureUltrasound)
    Drug_Used = fields.ForeignKeyOrFreeText(AnaestheticDrug)
    Drug_Concentration = db_models.FloatField(blank=True, null=True)
    Drug_Dose = db_models.FloatField(blank=True, null=True)
    Procedure_Note = db_models.TextField(blank=True, null=True)
    Time_Done = db_models.DateTimeField(blank=True, null=True)


class OperationDetails(models.EpisodeSubrecord):

    _is_singleton = True

    procedure    = fields.ForeignKeyOrFreeText(Procedure)
    planned_date = db_models.DateField(blank=True, null=True)
    surgeon      = db_models.ManyToManyField(
        Surgeon, related_name='surgeons', blank=True, null=True
    )
    anaesthetist = db_models.ManyToManyField(
        Anaesthetist, related_name='Anaesthetists', blank=True, null=True
    )
