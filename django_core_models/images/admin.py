"""
.. module::  image.admin
   :synopsis:  Django image application admin  module.

Django image application admin  module.

"""
from __future__ import absolute_import

from django.contrib import admin

from python_core_utils.core import class_name
from django_core_utils.admin import (NamedModelAdmin, admin_site_register,
                                     named_model_admin_class_attrs)


from .forms import ImageAdminForm
from .models import DocumentOrientation, Image, ImageFormat

DISPLAY_IMAGE_SIZE = 40


class ImageAdmin(NamedModelAdmin):
    """
    Image model admin class
    """
    form = ImageAdminForm
    list_display = ("id", "get_name", "get_alias", "get_image",
                    "version", "update_time", "update_user")
    list_display_links = ("id", "get_name", )

    fieldsets = (('Image',
                  {'fields': (("name",),
                   ("image",),
                   ("image_format",),
                   ("image_orientation",),
                   ("width", "height"),
                   ("alias",),
                   ("description",),
                   )}),) + NamedModelAdmin.get_field_sets()

    readonly_fields = NamedModelAdmin.readonly_fields + ("width", "height")

    def get_image(self, instance):
        """return instance image."""
        return str(instance.image)[:DISPLAY_IMAGE_SIZE]
    get_image.short_description = "image"


_named_classes = (DocumentOrientation, ImageFormat, )

for clasz in _named_classes:
    admin_site_register(
        clasz,
        (NamedModelAdmin,),
        named_model_admin_class_attrs(class_name(clasz)))

_other_model_classes = (Image,)
_other_admin_classes = (ImageAdmin,)

for model_class, admin_class in zip(_other_model_classes,
                                    _other_admin_classes):
    admin.site.register(model_class, admin_class)
