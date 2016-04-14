"""
.. module::  core_models.test_other
   :synopsis: core models other unit test module.

*core models* other unit test module.
"""
from __future__ import print_function

import factory.fuzzy

from core_utils.tests.factories import NamedModelFactory, VersionedModelFactory
from core_utils.tests.test_util import (NamedModelTestCase,
                                        VersionedModelTestCase)

from ..models import Annotation, Category

ANNOTATION_LENGTH = 128


class AnnotationModelFactory(VersionedModelFactory):
    """Annotation model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = Annotation

    annotation = factory.fuzzy.FuzzyText(length=ANNOTATION_LENGTH)


class AnnotationTestCase(VersionedModelTestCase):
    """Annotation model unit test class.
    """
    def test_annotation_crud(self):
        self.verify_versioned_model_crud(
            factory_class=AnnotationModelFactory)


class CategoryModelFactory(NamedModelFactory):
    """Category model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = Category


class CategoryTestCase(NamedModelTestCase):
    """Annotation model unit test class.
    """
    def test_category_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=CategoryModelFactory,
            get_by_name="name_1")
