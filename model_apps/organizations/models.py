"""
.. module::  organization.models
   :synopsis:  organization application models module.

*organization* application models module.

"""
from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _
from inflection import humanize, pluralize, underscore

from core_utils import fields
from core_utils.models import NamedModel, db_table

_app_label = "organizations"


_organization_type = "OrganizationType"
_organization_type_verbose = humanize(underscore(_organization_type))


class OrganizationType(NamedModel):
    """Contact organization type model class.

    Allows classification of contact organization.
    Sample values may include "unknown"
    """
    # @TODO: what are some of the possible organization types?
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _organization_type)
        verbose_name = _(_organization_type_verbose)
        verbose_name_plural = _(pluralize(_organization_type_verbose))


_organization = "Organization"
_organization_verbose = humanize(underscore(_organization))


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
        db_table = db_table(_app_label, _organization)
        verbose_name = _(_organization_verbose)
        verbose_name_plural = _(pluralize(_organization_verbose))
        unique_together = ('name', 'organization_type')


_organization_unit = "OrganizationUnit"
_organization_unit_verbose = humanize(underscore(_organization_unit))


class OrganizationUnit(NamedModel):
    """Organization unit model class.
    """
    organization = fields.foreign_key_field(Organization)

    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _organization_unit)
        verbose_name = _(_organization_unit_verbose)
        verbose_name_plural = _(pluralize(_organization_unit_verbose))


_role = "Role"
_role_verbose = humanize(underscore(_role))


class Role(NamedModel):
    """Role model class.

    Capture role attributes.
    """
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _role)
        verbose_name = _(_role_verbose)
        verbose_name_plural = _(pluralize(_role_verbose))
_title = "Title"
_title_verbose = humanize(underscore(_title))


class Title(NamedModel):
    """Title model class.

    Capture title/position attributes.
    Sample values may include "Research Analyst", "unknown"
    """
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _title)
        verbose_name = _(_title_verbose)
        verbose_name_plural = _(pluralize(_title_verbose))
