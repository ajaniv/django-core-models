"""
.. module::  config.common.root
   :synopsis:  Django root settings file.

Django root settings file.

"""
from __future__ import unicode_literals
import os
from os import path

VAR_APP_ENV = 'APP_ENV'
LOCAL_ENV = 'LOCAL'
DEV_ENV = 'DEV'
STAGING_ENV = 'STAGING'
PROD_ENV = 'PRODUCTION'
CONFIG_DIR = path.dirname(path.realpath(__file__))
PROJECT_ROOT = path.abspath(path.join(CONFIG_DIR, '../..'))
DB_DIR = path.join(PROJECT_ROOT, 'databases')
LOG_DIR = path.join(PROJECT_ROOT, 'logs')
CURRENT_ENV = os.getenv(VAR_APP_ENV, LOCAL_ENV)
os.environ[VAR_APP_ENV] = CURRENT_ENV
