"""
.. module::  image.models
   :synopsis:  image application models module.

*image*  application models module.
"""
from __future__ import absolute_import

import os

from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from inflection import humanize, pluralize, underscore
from utils.image import encode_file

from core_utils import constants, fields
from core_utils.models import NamedModel, NamedModelManager, db_table
from core_utils.utils import current_site

_app_label = "images"

IMAGE_FORMAT_GIF = 'gif'
IMAGE_FORMAT_JPEG = 'jpeg'
IMAGE_FORMAT_PNG = 'png'
IMAGE_FORMAT_UNKNOWN = constants.UNKNOWN
IMAGE_FORMATS = (IMAGE_FORMAT_GIF, IMAGE_FORMAT_JPEG,
                 IMAGE_FORMAT_PNG, IMAGE_FORMAT_UNKNOWN)

ORIENTATION_PORTRAIT = 'Portrait'
ORIENTATION_LANDSCAPE = 'Landscape'
ORIENTATION_UNKNOWN = constants.UNKNOWN
VISUAL_ORIENTATION = (ORIENTATION_PORTRAIT,
                      ORIENTATION_LANDSCAPE,
                      ORIENTATION_UNKNOWN)


_document_orientation = "DocumentOrientation"
_document_orientation_verbose = humanize(underscore(_document_orientation))


class DocumentOrientation(NamedModel):
    """Document orientation model class.
    """
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _document_orientation)
        verbose_name = _(_document_orientation_verbose)
        verbose_name_plural = _(pluralize(_document_orientation_verbose))

_image_format = "ImageFormat"
_image_format_verbose = humanize(underscore(_image_format))


class ImageFormat(NamedModel):
    """Image format model class.
    """
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _image_format)
        verbose_name = _(_image_format_verbose)
        verbose_name_plural = _(pluralize(_image_format_verbose))


class ImageManager(NamedModelManager):
    """
    Ad image manager class
    """
    context_explain = 'This transpired when fetching images for ad units {}'
    format_explain = 'Image of format "{}" has not been found. '

    def images(self, image_formats, ad_units):
        """
        Fetch images for ad units
        """
#         select = {'ad_unit_id': 'omas_ad_unit_2_ad_image.adunit_id'}
#         ad_unit_ids = [ad_unit.id for ad_unit in ad_units]
#         images = AdImage.objects.deferred_filter(
#             image_format__in=image_formats,
#             images__in=ad_unit_ids).extra(
#                 select=select).order_by()
#         if images.count() == 0:
#             formats = [image_format.name for image_format in image_formats]
#             context_explain = self.context_explain.format(ad_unit_ids)
#             format_explain = self.format_explain.format(formats)
#             raise AdServerError(explain_msg(
#                 object_type='images',
#                 context=context_explain,
#                 explanations=[format_explain]))
#         return images


def _image_upload_path(instance, filename):
    site = getattr(instance, 'site', current_site())
    domain_parts = site.domain.split('.')
    base_name = 'unknown'
    # @TODO: revisit the logic below
    if hasattr(settings, 'USE_MEDIA_ROOT'):   # Used under AWS
        media = 'media'
    else:
        media = ''
    for part in domain_parts:
        if 'www' not in part and 'com' not in part:
            base_name = part
            break
    full_path = os.path.join(media, base_name, 'images', filename)
    return full_path

_image = "Image"
_image_verbose = humanize(underscore(_image))


class Image(NamedModel):
    """Image model class.
    """
    image = fields.image_field(upload_to=_image_upload_path,
                               height_field='height',
                               width_field='width')

    image_format = fields.foreign_key_field(ImageFormat)
    image_orientation = fields.foreign_key_field(DocumentOrientation)
    width = fields.small_integer_field(default=0)
    height = fields.small_integer_field(default=0)

    objects = ImageManager()

    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _image)
        verbose_name = _(_image_verbose)
        verbose_name_plural = _(pluralize(_image_verbose))

    def __init__(self, *args, **kwargs):
        super(Image, self).__init__(*args, **kwargs)
        # @TODO: revisit read only text fields
#         self._config_help(('width', 'height', 'image_format'),
#                              ad_image_help_texts)

    def __str__(self):
        return '{0} {1} {2}'.format(
            super(Image, self).__str__(),
            self.image_format.name,
            self.image_orientation.name)

    def encode(self):
        """
        Encode the image
        Defaulting to base64 encoding
        """
        return encode_file(self.image.file)
