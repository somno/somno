"""
Plugin definition for the einstein_api Opal plugin
"""
from opal.core import plugins

from einstein_api.urls import urlpatterns


class Einstein_ApiPlugin(plugins.OpalPlugin):
    """
    Main entrypoint to expose this plugin to our Opal application.
    """
    urls = urlpatterns
    javascripts = {
        # Add your javascripts here!
        'opal.controllers': [
            'js/einstein_api/controllers/pair_monitor.js',
            'js/einstein_api/controllers/unpair_monitor.js',
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
