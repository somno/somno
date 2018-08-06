from opal.core.test import OpalTestCase


class TestCase(OpalTestCase):
    def setUp(self):
      self.patient, _ = self.new_patient_and_episode_please()

    def test_subscribe(self):
