"""
.. module::  model_apps.core.admin
   :synopsis:  Django core application admin  module.

Django core application admin  module.

"""
from __future__ import absolute_import

from django.contrib import admin
from utils.core import class_name

from core_utils.admin import (NamedModelAdmin, VersionedModelAdmin,
                              admin_site_register,
                              named_model_admin_class_attrs)

from .forms import AnnotationAdminForm
from .models import Annotation, Category


class AnnotationAdmin(VersionedModelAdmin):
    """
    Annotation model admin class
    """
    form = AnnotationAdminForm

    fieldsets = (('Annotation',
                  {'fields': (('annotation',),)
                   }),) + VersionedModelAdmin.get_field_sets()


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
