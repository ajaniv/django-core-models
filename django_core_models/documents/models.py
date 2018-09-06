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

from python_core_utils.image import encode_file
from django_core_utils import constants, fields
from django_core_utils.models import (NamedModel, VersionedModel, db_table)
from django_core_utils.utils import current_site
from . import validation

_app_label = "documents"

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


def _upload_path(instance, filename):
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
    return base_name, media

def _image_upload_path(instance, filename):
    """Calculate image upload path.
    """
    base_name, media = _upload_path(instance, filename)
    full_path = os.path.join(media, base_name, 'images', filename)
    return full_path

def _document_upload_path(instance, filename):
    """Calculate document upload path.
    """
    base_name, media = _upload_path(instance, filename)
    full_path = os.path.join(media, base_name, 'documents', filename)
    return full_path

_image = "Image"
_image_verbose = humanize(underscore(_image))


class Image(NamedModel):
    """Image model class.
    """
    # image field
    image = fields.image_field(upload_to=_image_upload_path,
                               height_field='height',
                               width_field='width')

    # image format field (i.e. 'png')
    image_format = fields.foreign_key_field(ImageFormat)
    
    # image orientation field (i.e. portrait, landscape)
    image_orientation = fields.foreign_key_field(DocumentOrientation)
    
    # image width in pixels
    width = fields.small_integer_field(default=0)
    
    # image height in pixels
    height = fields.small_integer_field(default=0)


    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _image)
        verbose_name = _(_image_verbose)
        verbose_name_plural = _(pluralize(_image_verbose))

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

_image_reference = "ImageReference"
_image_reference_verbose = humanize(underscore(_image_reference))


class ImageReference(VersionedModel):
    """ImageReference model class.

    Either image or url fields need to be defined, but not both.
    """
    # image reference
    image = fields.foreign_key_field(Image, blank=True, null=True)
    # url of image if one is not defined
    url = fields.url_field(null=True, blank=True)

    class Meta(VersionedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _image_reference)
        verbose_name = _(_image_reference_verbose)
        verbose_name_plural = _(pluralize(_image_reference_verbose))

    def clean(self):
        super(ImageReference, self).clean()
        validation.image_reference_validation(self)

    def __str__(self):
        return str(self.image) if self.image else self.url

_document_format = "DocumentFormat"
_document_format_verbose = humanize(underscore(_document_format))

class DocumentFormat(NamedModel):
    """Document format model class.
    """
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _document_format)
        verbose_name = _(_document_format_verbose)
        verbose_name_plural = _(pluralize(_document_format_verbose))
        
_document = "Document"
_document_verbose = humanize(underscore(_document))


class Document(NamedModel):
    """Document model class.
    """
    # document field
    document = fields.file_field(upload_to=_document_upload_path)
    
    # document format (i.e. 'docx', 'xlsx')
    document_format = fields.foreign_key_field(DocumentFormat)
    
    # document orientation (i.e 'portrait', 'landscape')
    document_orientation = fields.foreign_key_field(DocumentOrientation)
     

    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _document)
        verbose_name = _(_document_verbose)
        verbose_name_plural = _(pluralize(_document_verbose))

    def __str__(self):
        return '{0} {1} {2}'.format(
            super(Document, self).__str__(),
            self.document_format.name,
            self.document_orientation.name)

_document_reference = "DocumentReference"
_document_reference_verbose = humanize(underscore(_document_reference))


class DocumentReference(VersionedModel):
    """DocumentReference model class.

    Either image or url fields need to be defined, but not both.
    """
    # document foreign key
    document = fields.foreign_key_field(Document, blank=True, null=True)

    # url of document if one is not defined
    url = fields.url_field(null=True, blank=True)

    class Meta(VersionedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _document_reference)
        verbose_name = _(_document_reference_verbose)
        verbose_name_plural = _(pluralize(_document_reference_verbose))

    def clean(self):
        super(ImageReference, self).clean()
        validation.document_reference_validation(self)

    def __str__(self):
        return str(self.document) if self.document else self.url