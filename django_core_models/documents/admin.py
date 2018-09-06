"""
.. module::  image.admin
   :synopsis:  Django image application admin  module.

Django image application admin  module.

"""
from __future__ import absolute_import

from django.contrib import admin

from python_core_utils.core import class_name
from django_core_utils.admin import (NamedModelAdmin, VersionedModelAdmin,
                                     admin_site_register,
                                     named_model_admin_class_attrs)


from . import forms, models


DISPLAY_IMAGE_SIZE = 40
DISPLAY_DOCUMENT_SIZE = 40

_image_fields = (
    ("name",),
    ("image",),
    ("image_format",),
    ("image_orientation",),
    ("width", "height"),
    ("alias",),
    ("description",),)


class ImageAdmin(NamedModelAdmin):
    """
    Image model admin class
    """
    form = forms.ImageAdminForm
    list_display = ("id", "get_name", "get_alias", "get_image",
                    "version", "update_time", "update_user")
    list_display_links = ("id", "get_name", )
    limit_qs_to_request_user = True

    fieldsets = (
        ("Image",
         {'fields': _image_fields}),) + NamedModelAdmin.get_field_sets()

    readonly_fields = NamedModelAdmin.readonly_fields + ("width", "height")

    def get_image(self, instance):
        """return instance image."""
        return str(instance.image)[:DISPLAY_IMAGE_SIZE]
    get_image.short_description = "image"

_image_reference_fields = (
    ("image",),
    ("url",),)

_versioned_fields = VersionedModelAdmin.get_field_sets()


class ImageReferenceAdmin(VersionedModelAdmin):
    """
    Image reference model admin class
    """
    form = forms.ImageReferenceAdminForm
    list_display = ("id", "image", "url",
                    "version", "update_time", "update_user")
    list_display_links = ("id", "image", )
    limit_qs_to_request_user = True

    fieldsets = (
        ("Image reference",
         {'fields': _image_reference_fields}),) + _versioned_fields
         
_document_fields = (
    ("name",),
    ("document",),
    ("document_format",),
    ("document_orientation",),
    ("alias",),
    ("description",),)


class DocumentAdmin(NamedModelAdmin):
    """
    Document model admin class
    """
    form = forms.DocumentAdminForm
    list_display = ("id", "get_name", "get_alias", "get_document",
                    "version", "update_time", "update_user")
    list_display_links = ("id", "get_name", )
    limit_qs_to_request_user = True

    fieldsets = (
        ("Document",
         {'fields': _document_fields}),) + NamedModelAdmin.get_field_sets()


    def get_document(self, instance):
        """return instance document."""
        return str(instance.image)[:DISPLAY_DOCUMENT_SIZE]
    get_document.short_description = "document"

_document_reference_fields = (
    ("document",),
    ("url",),)

class DocumentReferenceAdmin(VersionedModelAdmin):
    """
    Document reference model admin class
    """
    form = forms.DocumentReferenceAdminForm
    list_display = ("id", "document", "url",
                    "version", "update_time", "update_user")
    list_display_links = ("id", "document", )
    limit_qs_to_request_user = True

    fieldsets = (
        ("Document reference",
         {'fields': _document_reference_fields}),) + _versioned_fields


_named_classes = (models.DocumentOrientation, models.DocumentFormat, models.ImageFormat)

for clasz in _named_classes:
    admin_site_register(
        clasz,
        (NamedModelAdmin,),
        named_model_admin_class_attrs(class_name(clasz)))

_other_model_classes = (models.Document, models.DocumentReference, models.Image, models.ImageReference)
_other_admin_classes = (DocumentAdmin, DocumentReferenceAdmin, ImageAdmin, ImageReferenceAdmin)

for model_class, admin_class in zip(_other_model_classes,
                                    _other_admin_classes):
    admin.site.register(model_class, admin_class)
