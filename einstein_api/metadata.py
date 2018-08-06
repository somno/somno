from opal.core import metadata
from einstein_api.models import Monitor


class Monitors(metadata.Metadata):
    slug = 'monitors'

    @classmethod
    def to_dict(klass, *args, **kwargs):
        id_user_machine_name = Monitor.objects.values_list(
            "id", "user_machine_name"
        )
        return dict(monitors={
            i: v for i, v in id_user_machine_name
        })
