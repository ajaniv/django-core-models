"""
.. module::  django_core_models.images.validation
   :synopsis:  images validation module

*images* application validation module.

"""
from __future__ import absolute_import
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError


def image_reference_validation(instance):
    """Validate ImageReference instance.
    """
    if not (instance.image or instance.url):
        raise ValidationError(_("Image and url are not defined."))

    if instance.image and instance.url:
        raise ValidationError(_("Image and url are both defined."))
