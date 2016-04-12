"""
.. module::  core.models_organization
   :synopsis:  django-utils core miscellaneous models module

django-utils core miscellaneous models module.

"""
from __future__ import absolute_import

from core_utils import fields
from core_utils.models import NamedModel, VersionedModel, db_table

from ..apps import CoreModelsConfig

_app_label = CoreModelsConfig.name


class Group(NamedModel):
    """
    Group model class.
    """
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, "Group")


class Name(VersionedModel):
    """Contact name model class.

    Defines the  name attributes.

    """
    family_name = fields.char_field()
    given_name = fields.char_field()
    additional_name = fields.char_field(blank=True, null=True)
    honorific_prefix = fields.char_field(blank=True, null=True)
    honorific_suffix = fields.char_field(blank=True, null=True)

    class Meta(VersionedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, "Name")
        unique_together = ('family_name', 'given_name', 'additional_name')

    @property
    def formatted_additional_name(self):
        return self.additional_name if self.additional_name is not None else ''

    @property
    def full_name(self):
        return '{} {} {}'.format(
            self.given_name, self.family_name, self.formatted_additional_name)


class FormattedName(VersionedModel):
    """Formatted name model class.

    Specifies the formatted  name fields.
    """
    name = fields.char_field(unique=True)

    class Meta(VersionedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, "FormattedName")

    def __str__(self):
        # TODO: in python 2.7 calling super results in recursion
        return '{0} {1.name!s}'.format(
            super(FormattedName, self).__str__(), self)


class NicknameType(NamedModel):
    """Nickname type model class.

    Enable nickname classification.
    Sample values may include 'work, 'home', 'unknown'.
    """
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, "NicknameType")


class LogoType(NamedModel):
    """Logo type model class.

    Enable logo classification.
    Sample values may include 'unknown'.
    """
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, "LogoType")


class PhotoType(NamedModel):
    """Photo type model class.

    Enable photo classification.
    Sample values may include 'unknown'.
    """
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, "PhotoType")


class UrlType(NamedModel):
    """Url type model class.

    Enable url classification.
    Sample values may include 'unknown'.
    """
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, "UrlType")


class PhoneType(NamedModel):
    """Phone type model class.

    Enable phone type classification.  Values may include "text",
    "fax", "cell", "unknown" """
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, "PhoneType")


class EmailType(NamedModel):
    """Email type model class.

    Enable email classification.
    """
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, "EmailType")


class InstantMessagingType(NamedModel):
    """Instant messaging  type model class.

    Enable the definition of instant messaging type.
    Sample instant messaging type values include "unknown"
    """
    # @TODO: what are some of the possible instance messaging types?
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, "InstantMessagingType")
