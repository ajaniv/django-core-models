"""
..  module:: social_media.text
    :synopsis: Django social_media application text  module.

Django social_media application text  module.
"""
from django.utils.translation import ugettext_lazy as _

# flake8: noqa
# required because of pep8 regression in ignoring disable of E123

formatted_name_labels = {
    "name": _("Name"),
    }

formatted_name_help_texts = {
    "name": _("Formatted name."),
    }


name_labels = {
    "additional_name": _("Additional name"),
    "family_name": _("Family name"),
    "given_name": _("Given name"),
    "honorific_prefix": _("Honorific prefix"),
    "honorific_suffix": _("Honorific suffix"),
    }

name_help_texts = {
    "additional_name": _("Additional name."),
    "family_name": _("Family name."),
    "given_name": _("Given name."),
    "honorific_prefix": _("Honorific prefix."),
    "honorific_suffix": _("Honorific suffix."),
    }
