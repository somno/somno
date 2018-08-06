import mock
from opal.core.test import OpalTestCase


@mock.patch("einstein_api.models.requests.post")
class SubscribeTestCase(OpalTestCase):
    def setUp(self):
        self.patient, _ = self.new_patient_and_episode_please()

    def test_subscribe_with_einstein_url_success(self, post):
        post.return_value = pass

    def test_subscribe_with_einstein_url_fail(self, post):
        pass

    def test_subscribe_without_einstein_url(self, post):
        pass
