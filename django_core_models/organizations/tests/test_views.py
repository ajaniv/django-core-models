"""
.. module::  django_core_models.organizations.tests.test_views
   :synopsis: organizations models application views unit test module.

*organizations*  application views unit test module.
"""
from __future__ import absolute_import, print_function
from django_core_utils.tests.api_test_utils import NamdedModelApiTestCase

from . import factories
from .. import models
from .. import serializers


class OrganizationTypeApiTestCase(NamdedModelApiTestCase):
    """OrganizationType API unit test class."""
    factory_class = factories.OrganizationTypeModelFactory
    model_class = models.OrganizationType
    serializer_class = serializers.OrganizationTypeSerializer

    url_detail = "organization-type-detail"
    url_list = "organization-type-list"

    name = factories.OrganizationTypeModelFactory.name

    def test_create_organization_type(self):
        self.verify_create_defaults()

    def test_create_organization_type_partial(self):
        self.verify_create_defaults_partial()

    def test_get_organization_type(self):
        self.verify_get_defaults()

    def test_put_organization_type_partial(self):
        instance = self.create_instance_default()
        data = dict(id=instance.id, name=self.name)
        self.verify_put(self.url_detail, instance, data, self.serializer_class)

    def test_delete_organization_type(self):
        self.verify_delete_default()


class OrganizationApiTestCase(NamdedModelApiTestCase):
    """Organization API unit test class."""
    factory_class = factories.OrganizationModelFactory
    model_class = models.Organization
    serializer_class = serializers.OrganizationSerializer

    url_detail = "organization-detail"
    url_list = "organization-list"

    name = "General Dynamics"

    def organization_data(self, instance):
        """return organization data"""
        instance = instance or self.factory_class()
        data = dict(organization_type=instance.organization_type.id)
        return data

    def post_required_data(self, ref_instance, user=None, site=None):
        """Return  post request required data."""
        data = super(
            OrganizationApiTestCase, self).post_required_data(user, site)
        data.update(self.organization_data(ref_instance))
        return data

    def verify_create_organization(
            self, ref_instance=None, data=None, expected_name=None):
        """Generate and verify post request for organization creation."""
        data = data or self.post_required_data(ref_instance)
        response, instance = self.verify_create(
            url=self.url_list,
            data=data,
            model_class=self.model_class,
            expected_name=expected_name)

        if ref_instance:
            self.assert_instance_equal(
                ref_instance, instance,
                ("organization_type",))

        return response, instance

    def test_create_organization(self):
        instance = self.create_instance_default()
        self.verify_create_organization(
            ref_instance=instance, expected_name=self.name)

    def test_create_organization_partial(self):
        instance = self.create_instance_default()
        data = self.organization_data(instance)
        data["name"] = self.name
        self.verify_create_organization(
            ref_instance=instance,
            data=data,
            expected_name=self.name)

    def test_get_organization(self):
        self.verify_get_defaults()

    def test_put_organization_partial(self):
        instance = self.create_instance_default()
        data = dict(id=instance.id, name=self.name)
        self.verify_put(self.url_detail, instance, data, self.serializer_class)

    def test_delete_organization(self):
        self.verify_delete_default()


class OrganizationUnitApiTestCase(NamdedModelApiTestCase):
    """Organization unit  API unit test class."""
    factory_class = factories.OrganizationUnitModelFactory
    model_class = models.OrganizationUnit
    serializer_class = serializers.OrganizationUnitSerializer

    url_detail = "organization-unit-detail"
    url_list = "organization-unit-list"

    name = "Advertizing"

    def organization_unit_data(self, instance):
        """return organization unit data"""
        instance = instance or self.factory_class()
        data = dict(organization=instance.organization.id)
        return data

    def post_required_data(self, ref_instance, user=None, site=None):
        """Return post request required data."""
        data = super(
            OrganizationUnitApiTestCase, self).post_required_data(user, site)
        data.update(self.organization_unit_data(ref_instance))
        return data

    def verify_create_organization_unit(
            self, ref_instance=None, data=None, expected_name=None):
        """Generate and verify post request for organization unit creation."""
        data = data or self.post_required_data(ref_instance)
        response, instance = self.verify_create(
            url=self.url_list,
            data=data,
            model_class=self.model_class,
            expected_name=expected_name)

        if ref_instance:
            self.assert_instance_equal(
                ref_instance, instance,
                ("organization",))

        return response, instance

    def test_create_organization_unit(self):
        instance = self.create_instance_default()
        self.verify_create_organization_unit(
            ref_instance=instance, expected_name=self.name)

    def test_create_organization_unit_partial(self):
        instance = self.create_instance_default()
        data = self.organization_unit_data(instance)
        data["name"] = self.name
        self.verify_create_organization_unit(
            ref_instance=instance,
            data=data,
            expected_name=self.name)

    def test_get_organization_unit(self):
        self.verify_get_defaults()

    def test_put_organization_unit_partial(self):
        instance = self.create_instance_default()
        data = dict(id=instance.id, name=self.name)
        self.verify_put(self.url_detail, instance, data, self.serializer_class)

    def test_delete_organization_unit(self):
        self.verify_delete_default()


class RoleApiTestCase(NamdedModelApiTestCase):
    """Role API unit test class."""
    factory_class = factories.RoleModelFactory
    model_class = models.Role
    serializer_class = serializers.RoleSerializer

    url_detail = "role-detail"
    url_list = "role-list"

    name = factories.RoleModelFactory.name

    def test_create_role(self):
        self.verify_create_defaults()

    def test_create_role_partial(self):
        self.verify_create_defaults_partial()

    def test_get_role(self):
        self.verify_get_defaults()

    def test_put_role_partial(self):
        instance = self.create_instance_default()
        data = dict(id=instance.id, name=self.name)
        self.verify_put(self.url_detail, instance, data, self.serializer_class)

    def test_delete_role(self):
        self.verify_delete_default()


class TitleApiTestCase(NamdedModelApiTestCase):
    """Title API unit test class."""
    factory_class = factories.TitleModelFactory
    model_class = models.Title
    serializer_class = serializers.TitleSerializer

    url_detail = "title-detail"
    url_list = "title-list"

    name = factories.TitleModelFactory.name

    def test_create_title(self):
        self.verify_create_defaults()

    def test_create_title_partial(self):
        self.verify_create_defaults_partial()

    def test_get_title(self):
        self.verify_get_defaults()

    def test_put_title_partial(self):
        instance = self.create_instance_default()
        data = dict(id=instance.id, name=self.name)
        self.verify_put(self.url_detail, instance, data, self.serializer_class)

    def test_delete_title(self):
        self.verify_delete_default()
