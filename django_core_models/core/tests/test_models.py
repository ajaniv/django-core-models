"""
.. module::  core.models.tests
   :synopsis: core models application models unit test module.

*core models* application models unit test module.
"""
from __future__ import absolute_import, print_function

import logging

from django_core_utils import constants
from django_core_utils.tests.test_util import (NamedModelTestCase,
                                               VersionedModelTestCase)

from ..models import Category
from .factories import (AnnotationModelFactory, CategoryModelFactory,
                        CurrencyModelFactory)

logger = logging.getLogger(__name__)


class AnnotationTestCase(VersionedModelTestCase):
    """Annotation model unit test class.
    """
    def test_annotation_crud(self):
        self.verify_versioned_model_crud(
            factory_class=AnnotationModelFactory)


class CategoryTestCase(NamedModelTestCase):
    """Category model unit test class.
    """
    def test_category_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=CategoryModelFactory,
            get_by_name="name_1")


class TestLoggingConfig(NamedModelTestCase):
    """Logging configuration testcase class.
    """
    def test_name_not_found(self):
        logger.warning('Verify logger filtering')
        name = 'myname'
        with self.assertRaises(Category.DoesNotExist):
            Category.objects.named_instance(name=name)

        self.assertTrue(CategoryModelFactory(name=constants.UNKNOWN))
        self.assertTrue(Category.objects.named_instance(name=name))


class CurrencyTestCase(NamedModelTestCase):
    """Currency model unit test class.
    """

    def test_currency_crud(self):
        currencies = [CurrencyModelFactory(name=name, iso_code=iso_code)
                      for name, iso_code in zip(
                          CurrencyModelFactory.names,
                          CurrencyModelFactory.iso_codes)]
        self.verify_named_instances_crud(
            currencies,
            factory_class=CurrencyModelFactory,
            get_by_name=CurrencyModelFactory.CURRENCY_USD)

    def test_currency_fields(self):
        instance = CurrencyModelFactory(
            name=CurrencyModelFactory.CURRENCY_EURO,
            iso_code=CurrencyModelFactory.ISO_4217_EUR)

        self.verify_instance(instance)
        instance.full_clean()
        self.assertEqual(instance.iso_code,
                         CurrencyModelFactory.ISO_4217_EUR,
                         "currency initialization error")
