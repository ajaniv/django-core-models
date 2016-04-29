"""
.. module::  django_core_models.core.tests.factories
   :synopsis: core models application unit test factories module.

*core models* application unit test factories module.
"""
from __future__ import absolute_import, print_function

import factory.fuzzy

from django_core_utils.tests.factories import (NamedModelFactory,
                                               VersionedModelFactory)
from django_core_models_libs.factory_utils import ISOMixin

from .. import models

ANNOTATION_LENGTH = 128


class AnnotationModelFactory(VersionedModelFactory):
    """Annotation model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = models.Annotation

    annotation = factory.fuzzy.FuzzyText(length=ANNOTATION_LENGTH)


class CategoryModelFactory(NamedModelFactory):
    """Category model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = models.Category


class CurrencyMixin(ISOMixin):
    """Currency mixin class"""
    CURRENCY_USD = "US Dollar"
    CURRENCY_EURO = "Euro"
    ISO_4217_EUR = "EUR"
    ISO_4217_USD = "USD"
    names = (CURRENCY_USD, CURRENCY_EURO)
    iso_codes = (ISO_4217_USD, ISO_4217_EUR)


class CurrencyModelFactory(CurrencyMixin, NamedModelFactory):
    """Currency model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = models.Currency
        django_get_or_create = ('name', 'iso_code')

    name = factory.Sequence(lambda n: CurrencyMixin.name(n))
    iso_code = factory.Sequence(lambda n: CurrencyMixin.iso_code(n))
