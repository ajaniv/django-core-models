"""
.. module::  configs.common.django
   :synopsis:  Django  settings file.


Django settings for django_core_models project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
from .root import PROJECT_ROOT, DEBUG

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
BASE_DIR = PROJECT_ROOT

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'ubd(v=i$@^plvy!-yyo*&@xi!y0514r4wkjp49k+e@r&*)7u-_'
ENV_SECRET_KEY = 'DJANGO_SECRET_KEY'
SECRET_KEY = os.environ[ENV_SECRET_KEY]

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True


ALLOWED_HOSTS = []


# Application definition
BASIC_DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    ]

EXTENDED_DJANGO_APPS = [
    'rest_framework',
    ]

CUSTOM_APPS = [
    'django_core_models.core.apps.CoreModelsConfig',
    'django_core_models.demographics.apps.DemographicsConfig',
    'django_core_models.images.apps.ImageConfig',
    'django_core_models.locations.apps.LocationConfig',
    'django_core_models.organizations.apps.OrganizationConfig',
    'django_core_models.social_media.apps.SocialMediaConfig',
    ]

INSTALLED_APPS = BASIC_DJANGO_APPS + EXTENDED_DJANGO_APPS + CUSTOM_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_core_models_settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': DEBUG,
        },
    },
]

WSGI_APPLICATION = 'django_core_models_settings.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators
VALIDATOR_PATH = 'django.contrib.auth.password_validation.'
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': VALIDATOR_PATH + 'UserAttributeSimilarityValidator',
    },
    {
        'NAME': VALIDATOR_PATH + 'MinimumLengthValidator',
    },
    {
        'NAME': VALIDATOR_PATH + 'CommonPasswordValidator',
    },
    {
        'NAME': VALIDATOR_PATH + 'NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
SITE_ID = 1
