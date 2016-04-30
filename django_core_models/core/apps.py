"""
.. module::  django_core_models.core.apps
   :synopsis:  django_core_models  core application configuration  module.

django_core_models core  application configuration  module.

"""
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CoreModelsConfig(AppConfig):
    """Django's core application configuration class."""
    name = __package__
    verbose_name = _("Core Models")
