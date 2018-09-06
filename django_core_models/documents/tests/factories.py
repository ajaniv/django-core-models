"""
.. module::  django_core_models.documents.tests.factories
   :synopsis: documents application factories module.

*documents* application unit test factories module.
"""
from __future__ import absolute_import, print_function
import factory
from django_core_utils.tests.factories import (NamedModelFactory,
                                               VersionedModelFactory)
from .. import models




class DocumentFormatModelFactory(NamedModelFactory):
    """Document format model factory class.
    """
    name = "docx"

    class Meta(object):
        """Model meta class."""
        model = models.DocumentFormat


class DocumentOrientationModelFactory(NamedModelFactory):
    """Document orientation model factory class.
    """
    name = models.ORIENTATION_LANDSCAPE

    class Meta(object):
        """Model meta class."""
        model = models.DocumentOrientation


class DocumentModelFactory(NamedModelFactory):
    """Document  model factory class.
    """
    DOCUMENT_FILENAME = 'test.docx'

    document = factory.django.FileField(filename=DOCUMENT_FILENAME, data=b'abcd')
    document_format = factory.SubFactory(DocumentFormatModelFactory)
    document_orientation = factory.SubFactory(DocumentOrientationModelFactory)

    name = "my document"

    class Meta(object):
        """Model meta class."""
        model = models.Document
        
class DocumentReferenceModelFactory(VersionedModelFactory):
    """DocumentReference  model factory class.
    """
    document = factory.SubFactory(DocumentModelFactory)

    class Meta(object):
        """Model meta class."""
        model = models.DocumentReference

class ImageFormatModelFactory(NamedModelFactory):
    """Image format model factory class.
    """
    name = models.IMAGE_FORMAT_GIF

    class Meta(object):
        """Model meta class."""
        model = models.ImageFormat
        

class ImageModelFactory(NamedModelFactory):
    """Image  model factory class.
    """
    IMAGE_WIDTH = 128
    IMAGE_HEIGHT = 128
    IMAGE_FILENAME = 'test.gif'

    image = factory.django.ImageField(color='blue',
                                      width=IMAGE_WIDTH,
                                      height=IMAGE_HEIGHT,
                                      filename=IMAGE_FILENAME,
                                      format=models.IMAGE_FORMAT_GIF)
    image_format = factory.SubFactory(ImageFormatModelFactory)
    image_orientation = factory.SubFactory(DocumentOrientationModelFactory)

    name = "my image"

    class Meta(object):
        """Model meta class."""
        model = models.Image


class ImageReferenceModelFactory(VersionedModelFactory):
    """ImageReference  model factory class.
    """
    image = factory.SubFactory(ImageModelFactory)

    class Meta(object):
        """Model meta class."""
        model = models.ImageReference
