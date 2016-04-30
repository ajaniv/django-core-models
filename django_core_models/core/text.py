"""
..  module:: django_core_models.core.text
    :synopsis: django_core_models core application text  module.

django_core_models core application text  module.
"""
from django.utils.translation import ugettext_lazy as _

# flake8: noqa
# required because of pep8 regression in ignoring disable of E123

annotation_labels = {
    "annotation": _("Annotation"),
    }

annotation_help_texts = {
    "annotation": _("Text annotation."),
    }

currency_labels = {
    "iso_code": _("ISO code"),
    }

currency_help_texts = {
    "iso_code": _("ISO 4217 currency code."),
    }
