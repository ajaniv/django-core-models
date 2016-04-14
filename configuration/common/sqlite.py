"""
.. module::  config.common.sqlite
   :synopsis:  Django sqlite settings file.

Django sqlite settings file.

"""
from __future__ import unicode_literals
import os

from configuration.common.root import DB_DIR
from utils.core import mkdir


mkdir(DB_DIR)
SQLITE_DB_NAME = 'db.sqlite3'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DB_DIR, SQLITE_DB_NAME),
    }
}
