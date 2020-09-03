# Django settings for somno project.
import os
import sys

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS
AUTOCOMPLETE_SEARCH = True

try:
    import dj_database_url

    DATABASES = {
        "default": dj_database_url.config(
            default="sqlite:///" + PROJECT_PATH + "/opal.sqlite"
        )
    }
except ImportError:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(PROJECT_PATH, "opal.sqlite"),
            "USER": "",
            "PASSWORD": "",
            "HOST": "",
            "PORT": "",
        }
    }

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["localhost", ".herokuapp.com", "127.0.0.1"]

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = "UTC"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en-gb"

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ""

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ""

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(PROJECT_PATH, "assets")

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = "/assets/"

# Additional locations of static files
# STATICFILES_DIRS = (
#     os.path.join(PROJECT_PATH, 'static'),
# )

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    "compressor.finders.CompressorFinder",
)

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'
STATICFILES_DIRS = [
    ('node_modules', '/node_modules'),
]
# Make this unique, and don't share it with anybody.
SECRET_KEY = "foobarbaz"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_PATH, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'opal.context_processors.settings',
                'opal.context_processors.models',
            ],
        },
    }
]


# if DEBUG:
#     TEMPLATE_LOADERS = (
#         'django.template.loaders.filesystem.Loader',
#         'django.template.loaders.app_directories.Loader',
#     )
# else:
#     TEMPLATE_LOADERS = (
#         ('django.template.loaders.cached.Loader', (
#             'django.template.loaders.filesystem.Loader',
#             'django.template.loaders.app_directories.Loader',
#             )),
#     )

MIDDLEWARE = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'opal.middleware.AngularCSRFRename',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'opal.middleware.DjangoReversionWorkaround',
    'reversion.middleware.RevisionMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = "somno.urls"

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = "somno.wsgi.application"

# TEMPLATE_DIRS = (
#     os.path.join(PROJECT_PATH, 'templates'),
# )

# TEMPLATE_CONTEXT_PROCESSORS= (
#     'django.contrib.auth.context_processors.auth',
#     'django.core.context_processors.debug',
#     'django.core.context_processors.i18n',
#     'django.core.context_processors.media',
#     'django.core.context_processors.request',
#     'django.core.context_processors.static',
#     'django.core.context_processors.tz',
#     'django.contrib.messages.context_processors.messages',
#     'opal.context_processors.settings',
#     'opal.context_processors.models',
# )

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework.authtoken',
    'axes',
    'reversion',
    'rest_framework',
    'compressor',
    'somno_theme',
    'opal',
    'opal.core.search',
    'opal.core.pathway',
    'einstein_api',
    'fhir_api',
    'somno',
    'django.contrib.admin',
)

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    )
}

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
        "console": {"level": "INFO", "filters": [], "class": "logging.StreamHandler"},
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
        "einstein_api": {"handlers": ["console"], "level": "INFO", "propagate": True},
    },
}

# Begins custom settings

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

DATE_FORMAT = "d/m/Y"
DATE_INPUT_FORMATS = ["%d/%m/%Y"]
DATETIME_FORMAT = "d/m/Y H:i:s"
DATETIME_INPUT_FORMATS = ["%d/%m/%Y %H:%M:%S"]

CSRF_COOKIE_NAME = "XSRF-TOKEN"
APPEND_SLASH = False

AXES_LOCK_OUT_AT_FAILURE = False
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

EMAIL_BACKEND = os.environ.get(
    "EMAIL_BACKEND", "django.core.mail.backends.smtp.EmailBackend"
)
if not DEBUG:
    EMAIL_HOST_USER = os.environ.get("SENDGRID_USERNAME", "")
    EMAIL_HOST = "smtp.sendgrid.net"
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_PASSWORD = os.environ.get("SENDGRID_PASSWORD", "")
else:
    EMAIL_PORT = 1025
    EMAIL_HOST = "localhost"

# TEST_RUNNER = 'django_test_coverage.runner.CoverageTestSuiteRunner'
COVERAGE_EXCLUDE_MODULES = (
    "somno.migrations",
    "somno.tests",
    "somno.local_settings",
    "opal.migrations",
    "opal.tests",
    "opal.wsgi",
)


# Begins OPAL Settings

OPAL_LOG_OUT_MINUTES = 15
OPAL_LOG_OUT_DURATION = OPAL_LOG_OUT_MINUTES * 60 * 1000
OPAL_FAVICON_PATH = "img/somno.favicon.png"
LOGIN_REDIRECT = "/#/list/today"

# Begins OPAL optional settings
# OPAL_EXTRA_HEADER = ''
# OPAL_EXTRA_APPLICATION = ''

INTEGRATING = False
#
# Uncomment these if you are integrating with other upstream systems via
# Glossolalia (http://github.com/openhealthcare/glossolalia)
#

# OPAL required Django settings you should edit

CONTACT_EMAIL = []
DEFAULT_FROM_EMAIL = "hello@example.com"
DEFAULT_DOMAIN = "http://anaesthetic.com/"

# Begins OPAL Settings you should edit !

OPAL_BRAND_NAME = "Somno"
VERSION_NUMBER = "0.2.0"

# einstein url is the server url that will
# translate the ouput of the monitors
# into json
EINSTEIN_URL = None

# host url, required to subscribe to einstein
HOST_URL = None

try:
    from somno.local_settings import *
except:
    pass
