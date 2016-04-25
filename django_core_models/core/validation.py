"""
.. module::  core.validation
   :synopsis:  core validation module

*core* application validation module.

"""
from __future__ import absolute_import

import pycountry
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from django_core_models_libs.validation_utils import (check_instance,
                                                      invalid_iso,
                                                      invalid_name)


def currency_validation(instance):
    """Perform currency validation.
    """

    entity = "Currency"
    check_instance(entity, instance)
    try:
        official = pycountry.currencies.get(letter=instance.iso_code)
    except KeyError:
        raise ValidationError(
            _(invalid_iso(entity)),
            params={'value': instance.iso_code})

    if official.name != instance.name:
        raise ValidationError(
            _(invalid_name(entity)),
            params={'value': instance.name,
                    'expected': official.name})
