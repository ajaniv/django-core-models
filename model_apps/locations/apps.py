"""
.. module::  model_apps.location.apps
   :synopsis:  Django location application configuration  module.

Django location  application configuration  module.

"""
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class LocationConfig(AppConfig):
    """Django's location application configuration class."""
    name = __package__
    verbose_name = _("Location")
