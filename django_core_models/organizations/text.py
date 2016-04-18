"""
..  module:: organization.text
    :synopsis: Django organization application text  module.

Django organization application text  module.
"""
from django.utils.translation import ugettext_lazy as _

# flake8: noqa
# required because of pep8 regression in ignoring disable of E123
organization_labels = {
    "organization_type": _("Organization type"),
    }

organization_help_texts = {
    "organization_type": _("Organization type."),
    }
organization_unit_labels = {
    "organization": _("Organization"),
    }

organization_unit_help_texts = {
    "organization": _("Organization."),
    }
