"""
..  module:: django_core_models.organizations.serializers
    :synopsis: django_core_models organizations application serializers module.

*django_core_models* organizations application serializers module.
"""
from __future__ import absolute_import

from django_core_utils.serializers import NamedModelSerializer

from . import models


class OrganizationTypeSerializer(NamedModelSerializer):
    """OrganizationType model serializer class."""

    class Meta(NamedModelSerializer.Meta):
        """Meta class definition."""
        model = models.OrganizationType


class OrganizationSerializer(NamedModelSerializer):
    """Organization model serializer class."""

    class Meta(NamedModelSerializer.Meta):
        """Meta class definition."""
        model = models.Organization
        fields = NamedModelSerializer.Meta.fields + (
            "organization_type", "uri")


class OrganizationUnitSerializer(NamedModelSerializer):
    """OrganizationUnit model serializer class."""

    class Meta(NamedModelSerializer.Meta):
        """Meta class definition."""
        model = models.OrganizationUnit
        fields = NamedModelSerializer.Meta.fields + ("organization",)


class RoleSerializer(NamedModelSerializer):
    """Role model serializer class."""

    class Meta(NamedModelSerializer.Meta):
        """Meta class definition."""
        model = models.Role


class TitleSerializer(NamedModelSerializer):
    """Title model serializer class."""

    class Meta(NamedModelSerializer.Meta):
        """Meta class definition."""
        model = models.Title
