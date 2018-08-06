import requests
import settings


class EinsteinException(Exception):
    pass


def get_url(einstein_id):
    return "http://{}/monitor/{}/subscribe".format(
        settings.EINSTEIN_URL, einstein_id
    )


def subscribe(einstein_id):
    if not settings.EINSTEIN_URL:
        return
    url = get_url(einstein_id)
    response = requests.post(url, data={})
    if response.status_code > 300:
        raise EinsteinException(
            "post to {} was rejected with {}".format(
                url, response.status_code
            )
        )
