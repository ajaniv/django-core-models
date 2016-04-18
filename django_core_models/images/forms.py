"""
.. module::  image.forms
   :synopsis:  Django image application forms  module.

Django image application forms  module.

"""
from __future__ import absolute_import

from python_core_utils.core import dict_merge
from django_core_utils import forms

from .models import Image
from .text import image_help_texts, image_labels


class ImageAdminForm(forms.NamedModelAdminForm):
    """Image model admin form  class.
    """
    class Meta(forms.VersionedModelAdminForm.Meta):
        """Form meta class."""
        model = Image
        labels = dict_merge(
            forms.NamedModelAdminForm.Meta.labels,
            image_labels)

        help_texts = dict_merge(
            forms.NamedModelAdminForm.Meta.help_texts,
            image_help_texts)
