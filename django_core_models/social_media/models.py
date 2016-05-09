"""
.. module::  social_media.models
   :synopsis:  social_media application models module.

*social_media* application models module.

"""
from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _
from inflection import humanize, pluralize, underscore

from django_core_utils import fields
from django_core_utils.models import NamedModel, VersionedModel, db_table

_app_label = "social_media"


_email = "Email"
_email_verbose = humanize(underscore(_email))


class Email(VersionedModel):
    """Email model class.
    """
    address = fields.email_field(unique=True)

    class Meta(VersionedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _email)
        verbose_name = _(_email_verbose)
        verbose_name_plural = _(pluralize(_email_verbose))

_email_type = "EmailType"
_email_type_verbose = humanize(underscore(_email_type))


class EmailType(NamedModel):
    """EmailType model class.

    Enable email classification.
    """
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _email_type)
        verbose_name = _(_email_type_verbose)
        verbose_name_plural = _(pluralize(_email_type_verbose))


class SimpleName(VersionedModel):
    """SimpleName model class.

    """
    # Note: MySql does not allow unique char fields to exceed 255
    name = fields.char_field()

    class Meta(VersionedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        abstract = True

    def __str__(self):
        # TODO: in python 2.7 calling super results in recursion
        return '{0} {1.name!s}'.format(
            super(SimpleName, self).__str__(), self)

_formatted_name = "FormattedName"
_formatted_name_verbose = humanize(underscore(_formatted_name))


class FormattedName(SimpleName):
    """FormattedName name model class.

    Specifies the formatted  name fields.
    """

    class Meta(SimpleName.Meta):
        """Model meta class declaration."""
        db_table = db_table(_app_label, _formatted_name)
        verbose_name = _(_formatted_name_verbose)
        verbose_name_plural = _(pluralize(_formatted_name_verbose))

_nickname = "Nickname"
_nickname_verbose = humanize(underscore(_nickname))


class Nickname(SimpleName):
    """Nickname  model class.
    """
    class Meta(SimpleName.Meta):
        """Model meta class declaration."""
        db_table = db_table(_app_label, _nickname)
        verbose_name = _(_nickname_verbose)
        verbose_name_plural = _(pluralize(_nickname_verbose))


_group = "Group"
_group_verbose = humanize(underscore(_group))


class Group(NamedModel):
    """
    Group model class.
    """
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _group)
        verbose_name = _(_group_verbose)
        verbose_name_plural = _(pluralize(_group_verbose))

_instance_messaging_type = "InstantMessagingType"
_instance_messaging_type_verbose = humanize(
    underscore(_instance_messaging_type))


class InstantMessagingType(NamedModel):
    """IInstantMessagingType model class.

    Enable the definition of instant messaging type.
    Sample instant messaging type values include "unknown"
    """
    # @TODO: what are some of the possible instance messaging types?
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _instance_messaging_type)
        verbose_name = _(_instance_messaging_type_verbose)
        verbose_name_plural = _(pluralize(_instance_messaging_type_verbose))

_logo_type = "LogoType"
_logo_type_verbose = humanize(underscore(_logo_type))


class LogoType(NamedModel):
    """LogoType model class.

    Enable logo classification.
    Sample values may include 'unknown'.
    """
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _logo_type)
        verbose_name = _(_logo_type_verbose)
        verbose_name_plural = _(pluralize(_logo_type_verbose))

_name = "Name"
_name_verbose = humanize(underscore(_name))


class Name(VersionedModel):
    """Name model class.

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
        db_table = db_table(_app_label, _name)
        verbose_name = _(_name_verbose)
        verbose_name_plural = _(pluralize(_name_verbose))
        unique_together = ('family_name', 'given_name', 'additional_name')

    @property
    def formatted_additional_name(self):
        return self.additional_name if self.additional_name is not None else ''

    @property
    def full_name(self):
        return '{} {} {}'.format(
            self.given_name, self.family_name, self.formatted_additional_name)

    def __str__(self):
        return '{0} {1.family_name!s} {1.given_name!s}'.format(
            super(Name, self).__str__(), self)

_nickname_type = "NicknameType"
_nickname_type_verbose = humanize(underscore(_nickname_type))


class NicknameType(NamedModel):
    """NicknameType model class.

    Enable nickname classification.
    Sample values may include 'work, 'home', 'unknown'.
    """
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _nickname_type)
        verbose_name = _(_nickname_type_verbose)
        verbose_name_plural = _(pluralize(_nickname_type_verbose))

_phone_type = "PhoneType"
_phone_type_verbose = humanize(underscore(_phone_type))


class PhoneType(NamedModel):
    """PhoneType model class.

    Enable phone type classification.  Values may include "text",
    "fax", "cell", "unknown" """

    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _phone_type)
        verbose_name = _(_phone_type_verbose)
        verbose_name_plural = _(pluralize(_phone_type_verbose))

_photo_type = "PhotoType"
_photo_type_verbose = humanize(underscore(_photo_type))


class PhotoType(NamedModel):
    """PhotoType model class.

    Enable photo classification.
    Sample values may include 'unknown'.
    """
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _photo_type)
        verbose_name = _(_photo_type_verbose)
        verbose_name_plural = _(pluralize(_photo_type_verbose))

_url_type = "UrlType"
_url_type_verbose = humanize(underscore(_url_type))


class UrlType(NamedModel):
    """UrlType model class.

    Enable url classification.
    Sample values may include 'unknown'.
    """
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _url_type)
        verbose_name = _(_url_type_verbose)
        verbose_name_plural = _(pluralize(_url_type_verbose))
