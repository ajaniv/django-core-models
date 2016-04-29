"""
.. module::  django_core_models_libs.validation_utils
   :synopsis:  django_core_models validation utilities  module.

django_core_models validation utilities  module.

"""
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def invalid_iso(entity):
    """Generate invalid iso template."""
    base = "is an invalid %s iso code" % entity
    return "%(value)s " + base


def invalid_name(entity):
    """Generate invalid name template."""
    base = "is an invalid %s name." % entity
    return "%(value)s " + base + "  Expected %(expected)s."


def check_instance(entity, instance):
    if instance is None:
        raise ValidationError(_("%s is not defined." % entity))
