from opal.core import detail


class AnaestheticReadings(detail.PatientDetailView):
    order = 1
    name = 'anaesthetic_reading'
    display_name = 'Anaesthetic Chart'
    # title = 'Anaesthetic Readings'
    template   = 'somno/detail/reading_detail.html'


class PreopAssessment(detail.PatientDetailView):
    order = 2
    name    = 'preop_assessment'
    display_name    = 'Pre Op Assessment'
    template        = 'somno/detail/preopassessment.html'
