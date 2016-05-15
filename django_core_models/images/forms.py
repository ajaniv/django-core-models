"""
.. module::  image.forms
   :synopsis:  Django image application forms  module.

Django image application forms  module.

"""
from __future__ import absolute_import

from python_core_utils.core import dict_merge
from django_core_utils import forms

from . import models, text


class ImageAdminForm(forms.NamedModelAdminForm):
    """Image model admin form  class.
    """
    class Meta(forms.VersionedModelAdminForm.Meta):
        """Form meta class."""
        model = models.Image
        labels = dict_merge(
            forms.NamedModelAdminForm.Meta.labels,
            text.image_labels)

        help_texts = dict_merge(
            forms.NamedModelAdminForm.Meta.help_texts,
            text.image_help_texts)


class ImageReferenceAdminForm(forms.NamedModelAdminForm):
    """ImageReference model admin form  class.
    """
    class Meta(forms.VersionedModelAdminForm.Meta):
        """Form meta class."""
        model = models.ImageReference
        labels = dict_merge(
            forms.NamedModelAdminForm.Meta.labels,
            text.image_reference_labels)

        help_texts = dict_merge(
            forms.NamedModelAdminForm.Meta.help_texts,
            text.image_reference_help_texts)
