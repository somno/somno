import json
import datetime
from unittest import mock
from django.test import override_settings
from django.utils import timezone
from opal.core.test import OpalTestCase
from einstein_api import models
from einstein_api import exceptions


class AbstractPairingTestCase(OpalTestCase):
    def setUp(self):
        self.patient, _ = self.new_patient_and_episode_please()
        self.monitor = models.Monitor.objects.create(
            user_machine_name="Goldfrapp",
            einstein_id="1234243234342"
        )
        self.now = timezone.now()


@mock.patch("einstein_api.models.requests")
@mock.patch("einstein_api.models.timezone")
@mock.patch.object(models.logger, "info")
class PairingSubscribeTestCase(AbstractPairingTestCase):
    def setUp(self):
        super(PairingSubscribeTestCase, self).setUp()
        self.response = mock.MagicMock()
        self.response.status_code = 201
        self.response.content = json.dumps(
            dict(subscription_id=1)
        )

    @override_settings(EINSTEIN_URL="http://someurl.com")
    def test_subscribe_with_einstein_url_success(self, info, timezone, requests):
        requests.post.return_value = self.response
        timezone.now.return_value = self.now
        models.Pairing.subscribe(self.patient.id, self.monitor.id)
        requests.post.assert_called_once_with(
            "http://someurl.com/monitor/1234243234342/subscribe"
        )
        pairing = models.Pairing.objects.get()
        self.assertEqual(
            pairing.patient_id, self.patient.id
        )
        self.assertEqual(
            pairing.start, self.now
        )
        self.assertIsNone(pairing.stop)
        self.assertEqual(pairing.monitor.id, self.monitor.id)
        self.assertEqual(pairing.subscription_id, 1)
        self.assertFalse(info.called)

    @override_settings(EINSTEIN_URL="http://someurl.com")
    def test_subscribe_with_einstein_url_fail(self, info, timezone, requests):
        self.response.status_code = 500
        requests.post.return_value = self.response
        timezone.now.return_value = self.now
        with self.assertRaises(exceptions.EinsteinError) as ee:
            models.Pairing.subscribe(self.patient.id, self.monitor.id)

        self.assertEqual(
            str(ee.exception), "unable to subscribe to {} {} with 500".format(
                self.monitor.id, self.monitor.user_machine_name
            )
        )
        self.assertFalse(info.called)

    @override_settings(EINSTEIN_URL=None)
    def test_subscribe_without_einstein_url(self, info, timezone, requests):
        requests.post.return_value = self.response
        timezone.now.return_value = self.now
        models.Pairing.subscribe(self.patient.id, self.monitor.id)
        pairing = models.Pairing.objects.get()
        self.assertEqual(
            pairing.patient_id, self.patient.id
        )
        self.assertEqual(
            pairing.start, self.now
        )
        self.assertIsNone(pairing.stop)
        self.assertEqual(pairing.monitor.id, self.monitor.id)
        self.assertEqual(pairing.subscription_id, 1)
        self.assertFalse(requests.post.called)
        info.assert_called_once_with(
            'Unable to find einstein_api url, not posting'
        )


@mock.patch("einstein_api.models.requests")
@mock.patch("einstein_api.models.timezone")
@mock.patch.object(models.logger, "info")
class PairingUnsubscribeTestCase(AbstractPairingTestCase):
    def setUp(self):
        super(PairingUnsubscribeTestCase, self).setUp()
        self.response = mock.MagicMock()
        self.response.status_code = 200
        self.pairing = models.Pairing.objects.create(
            monitor=self.monitor,
            start=self.now - datetime.timedelta(1),
            subscription_id=1,
            patient=self.patient,
        )

    @override_settings(EINSTEIN_URL="http://someurl.com")
    def test_unsubscribe_with_einstein_url(self, info, timezone, requests):
        timezone.now.return_value = self.now
        requests.delete.return_value.status_code = 200
        self.pairing.unsubscribe()

        self.assertEqual(requests.delete.call_count, 1)
        pairing = models.Pairing.objects.get(id=self.pairing.id)
        self.assertEqual(pairing.stop, self.now)

    @override_settings(EINSTEIN_URL="http://someurl.com")
    def test_unsubscribe_with_einstein_url_and_error(
        self, info, timezone, requests
    ):
        timezone.now.return_value = self.now
        requests.delete.return_value.status_code = 500

        with self.assertRaises(exceptions.EinsteinError) as ee:
            self.pairing.unsubscribe()

        pairing = models.Pairing.objects.get(id=self.pairing.id)
        self.assertIsNone(pairing.stop)

    @override_settings(EINSTEIN_URL=None)
    def test_unsubscribe_without_einstein_url(
        self, info, timezone, requests
    ):
        timezone.now.return_value = self.now
        self.pairing.unsubscribe()
        info.assert_called_once_with(
            "Unable to find einstein_api url, not unsubcribing"
        )
        pairing = models.Pairing.objects.get(id=self.pairing.id)
        self.assertEqual(pairing.stop, self.now)
        self.assertFalse(requests.delete.called)
