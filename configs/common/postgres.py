"""
.. module::  config.common.postgres
   :synopsis:  Django postgres settings file.

Django postgres settings file.

"""
import os
from __future__ import unicode_literals
ENV_POSTGRES_NAME = 'POSTGRES_NAME'
ENV_POSTGRES_USER = 'POSTGRES_USER'
ENV_POSTGRES_PASSWORD = 'POSTGRES_PASSWORD'
ENV_POSTGRES_HOST = 'POSTGRES_HOST'
ENV_POSTGRES_PORT = 'POSTGRES_PORT'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ[ENV_POSTGRES_NAME],
        'USER': os.environ[ENV_POSTGRES_USER],
        'PASSWORD': os.environ[ENV_POSTGRES_PASSWORD],
        'HOST': os.environ[ENV_POSTGRES_HOST],
        'PORT': os.environ[ENV_POSTGRES_PORT],
    }
}