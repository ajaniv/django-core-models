"""
.. module::  organization.apps
   :synopsis:  Django organization application configuration  module.

Django organization  application configuration  module.

"""
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class OrganizationConfig(AppConfig):
    """Django's organization application configuration class."""
    name = __package__
    verbose_name = _("Organization")
