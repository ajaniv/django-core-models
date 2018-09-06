"""
.. module::  django_core_models.documents.validation
   :synopsis:  documents validation module

*documents* application validation module.

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
    
def document_reference_validation(instance):
    """Validate DocumentReference instance.
    """
    if not (instance.document or instance.url):
        raise ValidationError(_("Document and url are not defined."))

    if instance.document and instance.url:
        raise ValidationError(_("Document and url are both defined."))
