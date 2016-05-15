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


_email_fields = (
    ("address",),)


class EmailAdmin(VersionedModelAdmin):
    """
    Email model admin class
    """
    form = forms.EmailAdminForm

    fieldsets = (
        ('Email',
         {'fields': _email_fields}),
    ) + VersionedModelAdmin.get_field_sets()


_formatted_name_fields = (
    ("name",),)


class FormattedNameAdmin(VersionedModelAdmin):
    """
    FormattedName model admin class
    """
    form = forms.FormattedNameAdminForm

    fieldsets = (
        ('Formatted name',
         {'fields': _formatted_name_fields}),
    ) + VersionedModelAdmin.get_field_sets()

_instant_messaging_fields = (
    ("address",),)


class InstantMessagingAdmin(VersionedModelAdmin):
    """
    InstantMessaging model admin class
    """
    form = forms.InstantMessagingAdminForm

    fieldsets = (
        ('Instant messaging',
         {'fields': _instant_messaging_fields}),
    ) + VersionedModelAdmin.get_field_sets()

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

    fieldsets = (
        ('Name',
         {'fields': _name_fields}),
    ) + VersionedModelAdmin.get_field_sets()


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
    models.Email, models.FormattedName, models.InstantMessaging, models.Name,)
_other_admin_classes = (
    EmailAdmin, FormattedNameAdmin, InstantMessagingAdmin, NameAdmin,)

for model_class, admin_class in zip(_other_model_classes,
                                    _other_admin_classes):
    admin.site.register(model_class, admin_class)
