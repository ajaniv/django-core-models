"""
.. module::  django_core_models.core.tests.test_views
   :synopsis: core models application views unit test module.

*core models* application views unit test module.
"""

from django_core_utils.tests.api_test_utils import NamdedModelApiTestCase
from django_core_models_libs.test_utils import IsoApiTestCase
from . import factories
from .. import models
from .. import serializers


class AnnotationApiTestCase(NamdedModelApiTestCase):
    """Annotation API unit test class."""
    factory_class = factories.AnnotationModelFactory
    model_class = models.Annotation
    serializer_class = serializers.AnnotationSerializer

    url_list = "annotation-list"
    url_detail = "annotation-detail"

    name = "my annotation"
    annotation = "some text"

    def post_required_data(self, user=None, site=None):
        """Return named model post request required data."""
        data = super(AnnotationApiTestCase, self).post_required_data(user,
                                                                     site)
        data.update(dict(annotation=self.annotation))
        return data

    def verify_create_annotation(self, data=None, expected_name=None):
        data = data or self.post_required_data()
        _, instance = self.verify_create(
            url=self.url_list,
            data=data,
            model_class=self.model_class,
            expected_name=expected_name)
        self.assertEqual(instance.annotation,
                         self.annotation,
                         "annotation creation error")

    def test_create_annotation(self):
        self.verify_create_annotation(expected_name=self.name)

    def test_create_annotation_partial(self):
        self.verify_create_annotation(data=dict(annotation=self.annotation))

    def test_get_annotation(self):
        self.verify_get_defaults()

    def test_put_annotation_partial(self):
        instance = self.create_instance_default()
        data = dict(id=instance.id, annotation=self.annotation)
        self.verify_put(self.url_detail, instance, data, self.serializer_class)

    def test_delete_annotation(self):
        self.verify_delete_default()


class CategoryApiTestCase(NamdedModelApiTestCase):
    """Category API unit test class."""
    factory_class = factories.CategoryModelFactory
    model_class = models.Category
    serializer_class = serializers.CategorySerializer

    url_detail = "category-detail"
    url_list = "category-list"

    name = "Industrials"

    def test_create_category(self):
        self.verify_create_defaults()

    def test_create_category_partial(self):
        self.verify_create_defaults_partial()

    def test_get_category(self):
        self.verify_get_defaults()

    def test_put_category_partial(self):
        instance = self.create_instance_default()
        data = dict(id=instance.id, name=self.name)
        self.verify_put(self.url_detail, instance, data, self.serializer_class)

    def test_delete_category(self):
        self.verify_delete_default()


class CurrencyApiTestCase(IsoApiTestCase):
    """Currency API unit test class."""
    factory_class = factories.CurrencyModelFactory
    model_class = models.Currency
    serializer_class = serializers.CurrencySerializer

    url_list = "currency-list"
    url_detail = "currency-detail"

    iso_code = factories.CurrencyMixin.ISO_4217_USD
    name = factories.CurrencyMixin.CURRENCY_USD

    def test_create_currency(self):
        self.verify_create_defaults()

    def test_create_currency_partial(self):
        self.verify_create_defaults_partial()

    def test_get_currency(self):
        self.verify_get_defaults()

    def test_put_currency_partial(self):
        instance = self.create_instance_default()
        data = dict(id=instance.id, name=self.name, iso_code=self.iso_code)
        self.verify_put(self.url_detail, instance, data, self.serializer_class)

    def test_delete_currency(self):
        self.verify_delete_default()
