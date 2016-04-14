"""
.. module::  core.models_misc
   :synopsis:  django-utils core demographics models module

django-utils core organization models module.

"""
from __future__ import absolute_import

from core_utils import fields
from core_utils.models import NamedModel, db_table

from ..apps import CoreModelsConfig

_app_label = CoreModelsConfig.name


class Title(NamedModel):
    """Title model class.

    Capture title/position attributes.
    Sample values may include "Research Analyst", "unknown"
    """
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, "Title")


class Role(NamedModel):
    """Role model class.

    Capture role attributes.
    """
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, "Role")


class OrganizationType(NamedModel):
    """Contact organization type model class.

    Allows classification of contact organization.
    Sample values may include "unknown"
    """
    # @TODO: what are some of the possible organization types?
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, "OrganizationType")


class Organization(NamedModel):
    """Organization model class.

    Capture organization attributes.
    """
    # @TODO: handle the ability to return organization units for organization
    organization_type = fields.foreign_key_field(OrganizationType)

    # defined to support Member relationship, see VCARD RFC 6350
    uri = fields.uri_field(blank=True, null=True)

    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, "Organization")
        unique_together = ('name', 'organization_type')


class OrganizationUnit(NamedModel):
    """Organization unit model class.
    """
    organization = fields.foreign_key_field(Organization)

    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, "OrganizationUnit")
