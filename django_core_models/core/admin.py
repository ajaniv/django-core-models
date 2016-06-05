"""
.. module::  django_core_models.core.admin
   :synopsis:  django_core_models core application admin  module.

django_core_models core application admin  module.

"""
from __future__ import absolute_import

from django.contrib import admin

from django_core_models_libs.admin_utils import iso_fields, iso_list_display
from django_core_utils.admin import (NamedModelAdmin, OptionalNamedModelAdmin,
                                     admin_site_register,
                                     named_model_admin_class_attrs)
from python_core_utils.core import class_name

from .forms import AnnotationAdminForm, CurrencyAdminForm
from .models import Annotation, Category, Currency

DISPLAY_ANNOTATION_SIZE = 32

_annotation_fields = (
    ("annotation",),
    ("name",),
    ("alias",),
    ("description",),)


class AnnotationAdmin(OptionalNamedModelAdmin):
    """
    Annotation model admin class
    """
    form = AnnotationAdminForm
    list_display = ("id", "get_name", "get_annotation",
                    "update_time", "update_user")
    list_display_links = ("id", "get_annotation", )
    search_fields = ("get_name", "get_annotation",)
    ordering = ("id",)
    limit_qs_to_request_user = True

    def get_annotation(self, instance):
        """return annotation."""
        return instance.annotation[:DISPLAY_ANNOTATION_SIZE]
    get_annotation.short_description = "annotation"

    fieldsets = (
        ('Annotation',
         {'fields': _annotation_fields}),
    ) + OptionalNamedModelAdmin.get_field_sets()

_currency_fields = (
    ("name",),
    ("iso_code",),
    ("alias",),
    ("description",),)


class CurrencyAdmin(NamedModelAdmin):
    """
    Currency model admin class
    """
    form = CurrencyAdminForm

    list_display = iso_list_display

    fieldsets = (
        ('Currency',
         {'fields': iso_fields}),
    ) + NamedModelAdmin.get_field_sets()

_named_classes = (Category,)

for clasz in _named_classes:
    admin_site_register(
        clasz,
        (NamedModelAdmin,),
        named_model_admin_class_attrs(class_name(clasz)))

_other_model_classes = (Annotation, Currency)
_other_admin_classes = (AnnotationAdmin, CurrencyAdmin)

for model_class, admin_class in zip(_other_model_classes,
                                    _other_admin_classes):
    admin.site.register(model_class, admin_class)
