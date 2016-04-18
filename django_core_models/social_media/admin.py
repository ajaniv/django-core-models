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

from .forms import FormattedNameAdminForm, NameAdminForm
from .models import (EmailType, FormattedName, Group, InstantMessagingType,
                     LogoType, Name, NicknameType, PhoneType, PhotoType,
                     UrlType)

_formatted_name_fields = (
    ("name",),)


class FormattedNameAdmin(VersionedModelAdmin):
    """
    Formatted name model admin class
    """
    form = FormattedNameAdminForm

    fieldsets = (
        ('Formatted name',
         {'fields': _formatted_name_fields}),
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
    form = NameAdminForm

    fieldsets = (
        ('Name',
         {'fields': _name_fields}),
    ) + VersionedModelAdmin.get_field_sets()


_named_classes = (EmailType, Group,
                  LogoType, InstantMessagingType,
                  NicknameType, PhoneType,
                  PhotoType, UrlType
                  )

for clasz in _named_classes:
    admin_site_register(
        clasz,
        (NamedModelAdmin,),
        named_model_admin_class_attrs(class_name(clasz)))

_other_model_classes = (FormattedName, Name)
_other_admin_classes = (FormattedNameAdmin, NameAdmin,)

for model_class, admin_class in zip(_other_model_classes,
                                    _other_admin_classes):
    admin.site.register(model_class, admin_class)
