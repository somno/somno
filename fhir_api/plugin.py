"""
Plugin definition for the fhir_api Opal plugin
"""
from opal.core import plugins

from fhir_api.urls import urlpatterns


class Fhir_ApiPlugin(plugins.OpalPlugin):
    """
    Main entrypoint to expose this plugin to our Opal application.
    """
    urls = urlpatterns
    javascripts = {
        # Add your javascripts here!
        'opal.fhir_api': [
            # 'js/fhir_api/app.js',
            # 'js/fhir_api/controllers/larry.js',
            # 'js/fhir_api/services/larry.js',
        ]
    }

    def list_schemas(self):
        """
        Return any patient list schemas that our plugin may define.
        """
        return {}

    def roles(self, user):
        """
        Given a (Django) USER object, return any extra roles defined
        by our plugin.
        """
        return {}


