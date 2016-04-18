"""
.. module::  demographics.apps
   :synopsis:  Django demographics application configuration  module.

Django demographics application configuration  module.

"""
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class DemographicsConfig(AppConfig):
    """Django's  demographics application configuration class."""
    name = __package__
    verbose_name = _("Demographics")
