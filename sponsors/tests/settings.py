from __future__ import unicode_literals

CACHES = {
    'default': {'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'},
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'sponsors'
)

ROOT_URLCONF = 'sponsors.tests.urls'

SECRET_KEY = 'asfdasdf'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)


SPONSOR_EXPIRATES = False
SPONSOR_EXPIRE_ON_MONTHS = 12
SPONSOR_LOGO_WIDTH = 200
SPONSOR_LOGO_HEIGHT = None
