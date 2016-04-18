"""
.. module::  model_apps.core.forms
   :synopsis:  Django core application forms  module.

Django core application forms  module.

"""
from __future__ import absolute_import

from utils.core import dict_merge

from core_utils import forms

from .models import Annotation
from .text import annotation_help_texts, annotation_labels


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
