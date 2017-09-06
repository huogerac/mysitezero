"""
Local settings

- Run in Debug mode
"""

from .base import *  # noqa

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

DEBUG = True

SECRET_KEY = 'ic$%8u0a(mmosez3vtl(h2aygx772q77uu_f8*wc+hk09qabf7'

ALLOWED_HOSTS = ['*', ]
