"""
.. module::  config.dev
   :synopsis:  Django dev environment settings file.

Django  dev environment settings file.

"""
from configuration.common.root import *  # @UnusedWildImport
from configuration.common.django import *  # @UnusedWildImport
from configuration.common.log import *  # @UnusedWildImport
from configuration.common.database import *  # @UnusedWildImport


DEBUG = True
TEMPLATE_DEBUG = True
