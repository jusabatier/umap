# -*- coding:utf-8 -*-

"""Base settings shared by all environments"""
# Import global settings to make it easier to extend settings.
from django.conf.global_settings import *   # pylint: disable=W0614,W0401
from django.template.defaultfilters import slugify

#==============================================================================
# Generic Django project settings
#==============================================================================

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SITE_ID = 1
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = 'UTC'
USE_TZ = True
USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', 'English'),
    ('fr', u'Francais'),
    ('it', u'Italiano'),
    ('pt', u'Portuguese'),
    ('nl', u'Dutch'),
    ('es', u'Español'),
    ('fi', u'Finnish'),
    ('de', u'Deutsch'),
    ('da', u'Danish'),
    ('ja', u'Japanese'),
    ('lt', u'Lithuanian'),
    ('cs-cz', u'Czech'),
    ('ca', u'Catalan'),
    ('zh', u'Chinese'),
    ('zh-tw', u'Chinese'),
    ('ru', u'Russian'),
    ('bg', u'Bulgarian'),
    ('vi', u'Vietnamese'),
    ('uk-ua', u'Ukrainian'),
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.gis',

    'leaflet_storage',
    'umap',
    'compressor',
)

# =============================================================================
# Calculation of directories relative to the project module location
# =============================================================================

import os
import umap as project_module

PROJECT_DIR = os.path.dirname(os.path.realpath(project_module.__file__))

# =============================================================================
# Project URLS and media settings
# =============================================================================

ROOT_URLCONF = 'umap.urls'

LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/'

STATIC_URL = '/static/'
MEDIA_URL = '/uploads/'

STATIC_ROOT = os.path.join('static')
MEDIA_ROOT = os.path.join('uploads')

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
)

STATICFILES_FINDERS = (
    'compressor.finders.CompressorFinder',
    # 'npm.finders.NpmFinder',
) + STATICFILES_FINDERS

# =============================================================================
# Templates
# =============================================================================

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.template.context_processors.request',
    'umap.context_processors.feedback_link',
    'umap.context_processors.version',
)

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', TEMPLATE_LOADERS),
)

# =============================================================================
# Middleware
# =============================================================================

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
)

# =============================================================================
# Auth / security
# =============================================================================

AUTHENTICATION_BACKENDS += (
)

# =============================================================================
# Miscellaneous project settings
# =============================================================================
LEAFLET_STORAGE_ALLOW_ANONYMOUS = False
LEAFLET_STORAGE_EXTRA_URLS = {
    'routing': 'http://www.openstreetmap.org/directions?engine=osrm_car&route={lat},{lng}&locale={locale}#map={zoom}/{lat}/{lng}',  # noqa
    'ajax_proxy': '/ajax-proxy/?url={url}'
}
SITE_URL = "http://umap.org"
UMAP_DEMO_SITE = False
MAP_SHORT_URL_NAME = "umap_short_url"
UMAP_USE_UNACCENT = False
UMAP_FEEDBACK_LINK = "http://wiki.openstreetmap.org/wiki/UMap#Feedback_and_help"  # noqa
USER_MAPS_URL = 'user_maps'
MAPQUEST_KEY = 'set me'

# =============================================================================
# Third party app settings
# =============================================================================
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
