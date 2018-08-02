from einstein_api import api
from django.conf.urls import url, include

urlpatterns = [
    url(r'einstein_api/v0.1/', include(api.einstein_api_router.urls)),
]
