"""
.. module::  core.models_organization
   :synopsis:  django-utils core miscellaneous models module

django-utils core miscellaneous models module.

"""

from core.models import app_table_name, db_table_name
from core.models import VersionedModel, NamedModel
from core import fields

from .apps import CoreModelsConfig

_app_label = CoreModelsConfig.name


__all__ = [
    'Group',
    'Name',
    'FormattedName',
    'NicknameType',
    'LogoType',
    'PhotoType',
    'UrlType',
    'PhoneType',
    'EmailType',
    'InstantMessagingType'
    ]


class Group(NamedModel):
    """
    Group model class.
    """
    class Meta(NamedModel.Meta):
        app_label = _app_label
        db_table = app_table_name(_app_label, db_table_name("Group"))


class Name(VersionedModel):
    """Contact name model class.

    Defines the  name attributes.

    """
    class Meta(VersionedModel.Meta):
        app_label = _app_label
        db_table = app_table_name(_app_label, db_table_name("Name"))
        unique_together = ('family_name', 'given_name', 'additional_name')

    family_name = fields.char_field()
    given_name = fields.char_field()
    additional_name = fields.char_field(blank=True, null=True)
    honorific_prefix = fields.char_field(blank=True, null=True)
    honorific_suffix = fields.char_field(blank=True, null=True)

    @property
    def full_name(self):
        return '%s %s %s' % (self.given_name, self.family_name, self.additional_name)


class FormattedName(VersionedModel):
    """Formatted name model class.

    Specifies the formatted  name fields.
    """
    class Meta(VersionedModel.Meta):
        app_label = _app_label
        db_table = app_table_name(_app_label, db_table_name("FormattedName"))

    name = fields.char_field(unique=True)

    def __str__(self):
        return self.name


class NicknameType(NamedModel):
    """Nickname type model class.

    Enable nickname classification.
    Sample values may include 'work, 'home', 'unknown'.
    """
    class Meta(NamedModel.Meta):
        app_label = _app_label
        db_table = app_table_name(_app_label, db_table_name("NicknameType"))

class LogoType(NamedModel):
    """Logo type model class.

    Enable logo classification.
    Sample values may include 'unknown'.
    """
    class Meta(NamedModel.Meta):
        app_label = _app_label
        db_table = app_table_name(_app_label, db_table_name("LogoType"))


class PhotoType(NamedModel):
    """Photo type model class.

    Enable photo classification.
    Sample values may include 'unknown'.
    """
    class Meta(NamedModel.Meta):
        app_label = _app_label
        db_table = app_table_name(_app_label, db_table_name("PhotoType"))


class UrlType(NamedModel):
    """Url type model class.

    Enable url classification.
    Sample values may include 'unknown'.
    """
    class Meta(NamedModel.Meta):
        app_label = _app_label
        db_table = app_table_name(_app_label, db_table_name("UrlType"))


class PhoneType(NamedModel):
    """Phone type model class.

    Enable phone type classification.  Values may include "text",
    "fax", "cell", "unknown" """
    class Meta(NamedModel.Meta):
        app_label = _app_label
        db_table = app_table_name(_app_label, db_table_name("PhoneType"))


class EmailType(NamedModel):
    """Email type model class.

    Enable email classification.
    """
    class Meta(NamedModel.Meta):
        app_label = _app_label
        db_table = app_table_name(_app_label, db_table_name("EmailType"))


class InstantMessagingType(NamedModel):
    """Instant messaging  type model class.

    Enable the definition of instant messaging type.
    Sample instant messaging type values include "unknown"
    """
    # @TODO: what are some of the possible instance messaging types?
    class Meta(NamedModel.Meta):
        app_label = _app_label
        db_table = app_table_name(_app_label,
                                  db_table_name("InstantMessagingType"))
