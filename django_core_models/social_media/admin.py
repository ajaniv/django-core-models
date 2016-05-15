"""
.. module::  social_media.admin
   :synopsis:  Django social_media application admin  module.

Django social_media application admin  module.

"""
from __future__ import absolute_import

from django.contrib import admin

from django_core_utils.admin import (NamedModelAdmin, VersionedModelAdmin,
                                     admin_site_register,
                                     named_model_admin_class_attrs)
from python_core_utils.core import class_name

from . import forms
from . import models


_versioned_field_sets = VersionedModelAdmin.get_field_sets()
_email_fields = (
    ("address",),)


class EmailAdmin(VersionedModelAdmin):
    """
    Email model admin class
    """
    form = forms.EmailAdminForm
    list_display = ("id", "address",
                    "version", "update_time", "update_user")
    list_display_links = ("id", "address",)

    fieldsets = (
        ("Email",
         {"fields": _email_fields}),
    ) + _versioned_field_sets


_formatted_name_fields = (
    ("name",),)


class FormattedNameAdmin(VersionedModelAdmin):
    """
    FormattedName model admin class
    """
    form = forms.FormattedNameAdminForm
    list_display = ("id", "name",
                    "version", "update_time", "update_user")
    list_display_links = ("id", "name",)

    fieldsets = (
        ("Formatted name",
         {"fields": _formatted_name_fields}),
    ) + _versioned_field_sets

_instant_messaging_fields = (
    ("address",),)


class InstantMessagingAdmin(VersionedModelAdmin):
    """
    InstantMessaging model admin class
    """
    form = forms.InstantMessagingAdminForm
    list_display = ("id", "address",
                    "version", "update_time", "update_user")
    list_display_links = ("id", "address",)

    fieldsets = (
        ("Instant messaging",
         {"fields": _instant_messaging_fields}),
    ) + _versioned_field_sets

_name_fields = (
    ("family_name",),
    ("given_name",),
    ("additional_name",),
    ("honorific_prefix",),
    ("honorific_suffix",),)


class NameAdmin(VersionedModelAdmin):
    """
    Name model admin class
    """
    form = forms.NameAdminForm
    list_display = ("id", "family_name", "given_name",
                    "version", "update_time", "update_user")
    list_display_links = ("id", "family_name",)
    fieldsets = (
        ("Name",
         {"fields": _name_fields}),
    ) + _versioned_field_sets

_nickname_fields = (
    ("name",),)


class NicknameAdmin(VersionedModelAdmin):
    """
    Nickname model admin class
    """
    form = forms.NicknameAdminForm
    list_display = ("id", "name",
                    "version", "update_time", "update_user")
    list_display_links = ("id", "name",)

    fieldsets = (
        ("Nickname",
         {"fields": _nickname_fields}),
    ) + _versioned_field_sets

_phone_fields = (
    ("number",),)


class PhoneAdmin(VersionedModelAdmin):
    """
    Phone model admin class
    """
    form = forms.NameAdminForm
    list_display = ("id", "number",
                    "version", "update_time", "update_user")
    list_display_links = ("id", "number",)

    fieldsets = (
        ("Phone",
         {"fields": _phone_fields}),
    ) + _versioned_field_sets


_url_fields = (
    ("address",),)


class UrlAdmin(VersionedModelAdmin):
    """
    Url model admin class
    """
    form = forms.UrlAdminForm
    list_display = ("id", "address",
                    "version", "update_time", "update_user")
    list_display_links = ("id", "address",)

    fieldsets = (
        ("Url",
         {"fields": _url_fields}),
    ) + _versioned_field_sets

_named_classes = (
    models.EmailType, models.Group,
    models.LogoType, models.InstantMessagingType,
    models.NicknameType, models.PhoneType,
    models.PhotoType, models.UrlType)

for clasz in _named_classes:
    admin_site_register(
        clasz,
        (NamedModelAdmin,),
        named_model_admin_class_attrs(class_name(clasz)))

_other_model_classes = (
    models.Email, models.FormattedName,
    models.InstantMessaging, models.Name,
    models.Nickname, models.Phone, models.Url)
_other_admin_classes = (
    EmailAdmin, FormattedNameAdmin,
    InstantMessagingAdmin, NameAdmin,
    NicknameAdmin, PhoneAdmin, UrlAdmin)

for model_class, admin_class in zip(_other_model_classes,
                                    _other_admin_classes):
    admin.site.register(model_class, admin_class)
