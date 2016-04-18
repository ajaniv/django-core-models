"""
.. module::  model_apps.core.apps
   :synopsis:  Django core application configuration  module.

Django core  application configuration  module.

"""
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CoreModelsConfig(AppConfig):
    """Django's core application configuration class."""
    name = __package__
    verbose_name = _("Core Models")
