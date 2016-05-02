"""
.. module::  organization.tests
   :synopsis: organization application models unit test module.

*organization* application models unit test module.
"""

from __future__ import print_function

import factory

from django_core_utils.tests.factories import NamedModelFactory
from django_core_utils.tests.test_utils import NamedModelTestCase

from ..models import (Organization, OrganizationType, OrganizationUnit, Role,
                      Title)


class TitleModelFactory(NamedModelFactory):
    """Title model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = Title


class TitleTestCase(NamedModelTestCase):
    """Title model unit test class.
    """
    def test_title_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=TitleModelFactory,
            get_by_name="name_1")


class RoleModelFactory(NamedModelFactory):
    """Role model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = Role


class RoleTestCase(NamedModelTestCase):
    """Role model unit test class.
    """
    def test_role_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=RoleModelFactory,
            get_by_name="name_1")


class OrganizationTypeModelFactory(NamedModelFactory):
    """Organization type model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = OrganizationType


class OrganizationTypeTestCase(NamedModelTestCase):
    """Organization type model unit test class.
    """
    def test_organization_type_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=OrganizationTypeModelFactory,
            get_by_name="name_1")


class OrganizationModelFactory(NamedModelFactory):
    """Organization  model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = Organization

    organization_type = factory.SubFactory(OrganizationTypeModelFactory)

ORGANIZATION_URI = "http://www.ondalear.com"


class OrganizationTestCase(NamedModelTestCase):
    """Organization  model unit test class.
    """
    def test_organization_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=OrganizationModelFactory,
            get_by_name="name_1")

    def test_organiation_uri_field(self):
        instance = OrganizationModelFactory(uri=ORGANIZATION_URI)
        self.assertEqual(instance.uri, ORGANIZATION_URI)


class OrganizationUnitModelFactory(NamedModelFactory):
    """Organization unit model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = OrganizationUnit

    organization = factory.SubFactory(OrganizationModelFactory)


class OrganizationUnitTestCase(NamedModelTestCase):
    """Organization unit  model unit test class.
    """
    def test_organization_unit_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=OrganizationUnitModelFactory,
            get_by_name="name_1")
