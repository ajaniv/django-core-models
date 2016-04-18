"""
.. module::  model_apps.social_media.forms
   :synopsis:  Django social_media application forms  module.

Django social_media application forms  module.

"""
from __future__ import absolute_import

from utils.core import dict_merge

from core_utils import forms

from .models import FormattedName, Name
from .text import (formatted_name_help_texts, formatted_name_labels,
                   name_help_texts, name_labels)


class FormattedNameAdminForm(forms.VersionedModelAdminForm):
    """Formatted name  model admin form  class.
    """
    class Meta(forms.VersionedModelAdminForm.Meta):
        """Form meta class."""
        model = FormattedName
        labels = dict_merge(
            forms.VersionedModelAdminForm.Meta.labels,
            formatted_name_labels)

        help_texts = dict_merge(
            forms.VersionedModelAdminForm.Meta.help_texts,
            formatted_name_help_texts)


class NameAdminForm(forms.VersionedModelAdminForm):
    """Name model admin form  class.
    """
    class Meta(forms.VersionedModelAdminForm.Meta):
        """Form meta class."""
        model = Name
        labels = dict_merge(
            forms.VersionedModelAdminForm.Meta.labels,
            name_labels)

        help_texts = dict_merge(
            forms.VersionedModelAdminForm.Meta.help_texts,
            name_help_texts)
