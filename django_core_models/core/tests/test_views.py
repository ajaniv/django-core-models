"""
.. module::  django_core_models.core.tests.test_views
   :synopsis: core models application views unit test module.

*core models* application views unit test module.
"""
from django_core_utils.tests.api_test_utils import NamdedModelApiTestCase
from . import factories
from .. import models


class IsoApiTestCase(NamdedModelApiTestCase):
    """Base class for named classes with iso field unit tests.
    """
    def post_required_data(self, user=None, site=None):
        """Return named model post request required data."""
        data = super(IsoApiTestCase, self).post_required_data(user, site)
        data.update(dict(iso_code=self.iso_code))
        return data

    def verify_create(self, url, data, model_class,
                      expected_name, expected_iso_code):
        """Verify post request for named model instance creation."""
        response, instance = super(
            IsoApiTestCase, self).verify_create(url, data,
                                                model_class, expected_name)
        self.assertEqual(instance.iso_code, expected_iso_code)
        return response, instance

    def verify_create_defaults(self, data=None):
        """Verify post request will all required arguments.

        Pulls the required parameters from the test class.
        """
        data = data or self.post_required_data()
        return self.verify_create(
            url=self.url_list,
            data=data,
            model_class=self.model_class,
            expected_name=self.name,
            expected_iso_code=self.iso_code)

    def verify_create_defaults_partial(self):
        """Verify post request with partial required arguments.

        Pulls the required parameters from the test class.
        """
        return self.verify_create_defaults(
            data=dict(name=self.name, iso_code=self.iso_code))


class AnnotationApiTestCase(NamdedModelApiTestCase):
    """Annotation API unit test class."""
    name = "my annotation"
    url_list = "annotation-list"
    model_class = models.Annotation
    annotation = "some text"

    def post_required_data(self, user=None, site=None):
        """Return named model post request required data."""
        data = super(AnnotationApiTestCase, self).post_required_data(user,
                                                                     site)
        data.update(dict(annotation=self.annotation))
        return data

    def verify_annotation(self, data=None, expected_name=None):
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
        self.verify_annotation(expected_name=self.name)

    def test_create_annotation_partial(self):
        self.verify_annotation(data=dict(annotation=self.annotation))


class CategoryApiTestCase(NamdedModelApiTestCase):
    """Category API unit test class."""
    name = "Industrials"
    url_list = "category-list"
    model_class = models.Category

    def test_create_category(self):
        self.verify_create_defaults()

    def test_create_category_partial(self):
        self.verify_create_defaults_partial()


class CurrencyApiTestCase(IsoApiTestCase):
    """Currency API unit test class."""
    name = factories.CurrencyMixin.CURRENCY_USD
    iso_code = factories.CurrencyMixin.ISO_4217_USD
    url_list = "currency-list"
    model_class = models.Currency

    def test_create_currency(self):
        self.verify_create_defaults()

    def test_create_currency_partial(self):
        self.verify_create_defaults_partial()
