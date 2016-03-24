"""
.. module::  core.models_misc
   :synopsis:  django-utils core demographics models module

django-utils core organization models module.

"""

from core.models import app_table_name, db_table_name
from core.models import NamedModel
from core import fields

from .apps import CoreModelsConfig

_app_label = CoreModelsConfig.name

__all__ = [
    'Title',
    'Role',
    'Organization',
    'OrganizationType',
    'OrganizationUnit'
    ]


class Title(NamedModel):
    """Title model class.

    Capture title/position attributes.
    Sample values may include "Research Analyst", "unknown"
    """
    class Meta(NamedModel.Meta):
        app_label = _app_label
        db_table = app_table_name(_app_label, db_table_name("Title"))


class Role(NamedModel):
    """Role model class.

    Capture role attributes.
    """
    class Meta(NamedModel.Meta):
        app_label = _app_label
        db_table = app_table_name(_app_label, db_table_name("Role"))


class OrganizationType(NamedModel):
    """Contact organization type model class.

    Allows classification of contact organization.
    Sample values may include "unknown"
    """
    # @TODO: what are some of the possible organization types?
    class Meta(NamedModel.Meta):
        app_label = _app_label
        db_table = app_table_name(_app_label,
                                  db_table_name("OrganizationType"))


class Organization(NamedModel):
    """Organization model class.

    Capture organization attributes.
    """
    # @TODO: handle the ability to return organization units for organization
    class Meta(NamedModel.Meta):
        app_label = _app_label
        db_table = app_table_name(_app_label, db_table_name("Organization"))
        unique_together = ('name', 'organization_type')

    organization_type = fields.foreign_key_field(OrganizationType)

    # defined to support Member relationship, see VCARD RFC 6350
    uri = fields.uri_field(blank=True, null=True)


class OrganizationUnit(NamedModel):
    """Organization unit model class.
    """
    class Meta(NamedModel.Meta):
        app_label = _app_label
        db_table = app_table_name(_app_label,
                                  db_table_name("OrganizationUnit"))

    organization = fields.foreign_key_field(Organization)
