"""
.. module::  organization.admin
   :synopsis:  Django organization application admin  module.

Django organization application admin  module.

"""
from __future__ import absolute_import

from django.contrib import admin

from django_core_utils.admin import (NamedModelAdmin, admin_site_register,
                                     named_model_admin_class_attrs)
from python_core_utils.core import class_name

from .forms import OrganizationAdminForm, OrganizationUnitAdminForm
from .models import (Organization, OrganizationType, OrganizationUnit, Role,
                     Title)

_organization_fields = (
    ("name",),
    ("organization_type",),
    ("alias",),
    ("description",),)


class OrganizationAdmin(NamedModelAdmin):
    """
    Organization unit model admin class
    """
    form = OrganizationAdminForm

    fieldsets = (
        ('Organization unit',
         {'fields': _organization_fields}),
    ) + NamedModelAdmin.get_field_sets()


_organization_unit_fields = (
    ("name",),
    ("organization",),
    ("alias",),
    ("description",),)


class OrganizationUnitAdmin(NamedModelAdmin):
    """
    Organization unit model admin class
    """
    form = OrganizationUnitAdminForm

    fieldsets = (
        ('Organization unit',
         {'fields': _organization_unit_fields}),
    ) + NamedModelAdmin.get_field_sets()


_named_classes = (OrganizationType,
                  Role, Title,
                  )

for clasz in _named_classes:
    admin_site_register(
        clasz,
        (NamedModelAdmin,),
        named_model_admin_class_attrs(class_name(clasz)))

_other_model_classes = (Organization, OrganizationUnit, )
_other_admin_classes = (OrganizationAdmin, OrganizationUnitAdmin,)

for model_class, admin_class in zip(_other_model_classes,
                                    _other_admin_classes):
    admin.site.register(model_class, admin_class)
