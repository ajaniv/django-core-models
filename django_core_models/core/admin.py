"""
.. module::  core.admin
   :synopsis:  Django core application admin  module.

Django core application admin  module.

"""
from __future__ import absolute_import

from django.contrib import admin

from django_core_utils.admin import (NamedModelAdmin, OptionalNamedModelAdmin,
                                     admin_site_register,
                                     named_model_admin_class_attrs)
from python_core_utils.core import class_name

from .forms import AnnotationAdminForm
from .models import Annotation, Category

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

    def get_annotation(self, instance):
        """return annotation."""
        return instance.annotation[:DISPLAY_ANNOTATION_SIZE]
    get_annotation.short_description = "annotation"

    fieldsets = (
        ('Annotation',
         {'fields': _annotation_fields}),
    ) + OptionalNamedModelAdmin.get_field_sets()


_named_classes = (Category,)

for clasz in _named_classes:
    admin_site_register(
        clasz,
        (NamedModelAdmin,),
        named_model_admin_class_attrs(class_name(clasz)))

_other_model_classes = (Annotation,)
_other_admin_classes = (AnnotationAdmin,)

for model_class, admin_class in zip(_other_model_classes,
                                    _other_admin_classes):
    admin.site.register(model_class, admin_class)
