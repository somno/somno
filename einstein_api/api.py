from rest_framework.response import Response
from rest_framework import status, viewsets
from opal.core.api import OPALRouter

from einstein_api import models
from einstein_api import payload_handler


class EinsteinPayloadViewSet(viewsets.ViewSet):
    base_name = 'einstein_observation'

    def create(self, request):
        obs = models.PayloadReceived(data=request.data)
        payload_handler.handle_payload(request.data)
        obs.save()
        return Response(
            {}, status=status.HTTP_201_CREATED
        )


einstein_api_router = OPALRouter()
einstein_api_router.register(
    EinsteinPayloadViewSet.base_name, EinsteinPayloadViewSet
)
