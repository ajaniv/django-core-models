"""
.. module::  django_core_models.images.validation
   :synopsis:  images validation module

*images* application validation module.

"""
from __future__ import absolute_import
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError


def image_validation(image, url):
    """Validate ContactImage association image and url.
    """
    if not (image or url):
        raise ValidationError(_("Image and url are none."))
