"""
WSGI config for elcid project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import os

# We defer to a DJANGO_SETTINGS_MODULE already in the environment. This breaks
# if running multiple sites in the same mod_wsgi process. To fix this, use
# mod_wsgi daemon mode with each site in its own daemon process, or use
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "anaesthetic.settings")

from django.core.wsgi import get_wsgi_application

try:
    # Serve static files on Heroku
    from dj_static import Cling
    application = Cling(get_wsgi_application())
except ImportError:
    application = get_wsgi_application()

