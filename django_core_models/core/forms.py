"""
.. module::  core.forms
   :synopsis:  Django core application forms  module.

Django core application forms  module.

"""
from __future__ import absolute_import

from django_core_utils import forms
from python_core_utils.core import dict_merge

from .models import Annotation, Currency
from .text import (annotation_help_texts, annotation_labels,
                   currency_help_texts, currency_labels)


class AnnotationAdminForm(forms.VersionedModelAdminForm):
    """Annotation model form  class.
    """
    class Meta(forms.VersionedModelAdminForm.Meta):
        """Form meta class."""
        model = Annotation
        labels = dict_merge(
            forms.VersionedModelAdminForm.Meta.labels,
            annotation_labels)

        help_texts = dict_merge(
            forms.VersionedModelAdminForm.Meta.help_texts,
            annotation_help_texts)


class CurrencyAdminForm(forms.NamedModelAdminForm):
    """Currency  model admin form class.
    """
    class Meta(forms.NamedModelAdminForm.Meta):
        """Form meta class."""
        model = Currency
        labels = dict_merge(
            forms.NamedModelAdminForm.Meta.labels,
            currency_labels)

        help_texts = dict_merge(
            forms.NamedModelAdminForm.Meta.help_texts,
            currency_help_texts)
