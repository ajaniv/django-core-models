"""
.. module::  organization.tests
   :synopsis: organization application models unit test module.

*organization* application models unit test module.
"""

from __future__ import absolute_import, print_function

from django_core_utils.tests.test_utils import NamedModelTestCase

from . import factories


class OrganizationTypeTestCase(NamedModelTestCase):
    """Organization type model unit test class.
    """
    def test_organization_type_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=factories.OrganizationTypeModelFactory,
            get_by_name="name_1")


ORGANIZATION_URI = "http://www.ondalear.com"


class OrganizationTestCase(NamedModelTestCase):
    """Organization model unit test class.
    """
    def test_organization_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=factories.OrganizationModelFactory,
            get_by_name="name_1")

    def test_organiation_uri_field(self):
        instance = factories.OrganizationModelFactory(uri=ORGANIZATION_URI)
        self.assertEqual(instance.uri, ORGANIZATION_URI)


class OrganizationUnitTestCase(NamedModelTestCase):
    """Organization unit model unit test class.
    """
    def test_organization_unit_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=factories.OrganizationUnitModelFactory,
            get_by_name="name_1")


class RoleTestCase(NamedModelTestCase):
    """Role model unit test class.
    """
    def test_role_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=factories.RoleModelFactory,
            get_by_name="name_1")


class TitleTestCase(NamedModelTestCase):
    """Title model unit test class.
    """
    def test_title_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=factories.TitleModelFactory,
            get_by_name="name_1")
