"""
.. module::  django_core_models_libs.test_utils
   :synopsis:  django_core_models test utilities  module.

django_core_models test utilities  module.

"""
from django_core_utils.tests.api_test_utils import NamdedModelApiTestCase


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
