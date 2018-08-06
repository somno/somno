import json
import datetime
from django.test import override_settings
from rest_framework.reverse import reverse
from rest_framework.test import APIClient
from opal.core.test import OpalTestCase
from einstein_api import models, payload_handler
from somno import models as smodels


class EinsteinObservationTestCase(OpalTestCase):
    TEST_DATA = {
        "monitor_id": "00:09:fb:09:77:bd",
        "observations": [
            {
                "physio_id": "NOM_ECG_CARD_BEAT_RATE",
                "value": 79,
                "unit_code": "NOM_DIM_BEAT_PER_MIN"
            },
            {
                "physio_id": "NOM_RESP_RATE",
                "value": 17,
                "unit_code": "NOM_DIM_RESP_PER_MIN"
            },
            {
                "physio_id": "NOM_ECG_V_P_C_CNT",
                "value": 0,
                "unit_code": "NOM_DIM_BEAT_PER_MIN"
            }
        ],
        "datetime": "2018-08-02T11:52:37.197155"
    }

    def setUp(self):
        request = self.rf.get("/")
        self.url = reverse(
            "einstein_observation-list",
            request=request
        )
        self.client = APIClient()

    @override_settings(EINSTEIN_URL=None)
    def test_post_no_subscription(self):
        response = self.client.post(
            self.url,
            json.dumps(self.TEST_DATA),
            content_type='application/json'
        )
        result = models.PayloadReceived.objects.get()
        self.assertEqual(len(result.data["observations"]), 3)
        self.assertEqual(
            result.data["observations"][0]["physio_id"],
            "NOM_ECG_CARD_BEAT_RATE"
        )

        self.assertEqual(response.status_code, 201)
        self.assertFalse(
            smodels.Observation.objects.exists()
        )

    @override_settings(EINSTEIN_URL=None)
    def test_post_with_subscription(self):
        patient, _ = self.new_patient_and_episode_please()
        dt = payload_handler.str_to_datetime(self.TEST_DATA["datetime"])
        monitor = models.Monitor.objects.create(
            einstein_id="00:09:fb:09:77:bd",
            user_machine_name="Moonraker"
        )
        models.Pairing.objects.create(
            patient=patient,
            monitor=monitor,
            start=dt - datetime.timedelta(hours=1),
            subscription_id=1
        )
        response = self.client.post(
            self.url,
            json.dumps(self.TEST_DATA),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        observation = patient.observation_set.get()
        self.assertEqual(
            observation.pulse, 79
        )

        self.assertEqual(
            observation.datetime, dt
        )
