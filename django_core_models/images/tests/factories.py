"""
.. module::  django_core_models.images.tests.factories
   :synopsis: images application factories module.

*images* application unit test factories module.
"""
from __future__ import absolute_import, print_function
import factory
from django_core_utils.tests.factories import (NamedModelFactory,
                                               VersionedModelFactory)
from .. import models


class DocumentOrientationModelFactory(NamedModelFactory):
    """Document orientation model factory class.
    """
    name = models.ORIENTATION_LANDSCAPE

    class Meta(object):
        """Model meta class."""
        model = models.DocumentOrientation


class ImageFormatModelFactory(NamedModelFactory):
    """Image format model factory class.
    """
    name = models.IMAGE_FORMAT_GIF

    class Meta(object):
        """Model meta class."""
        model = models.ImageFormat


IMAGE_WIDTH = 128
IMAGE_HEIGHT = 128
FILENAME = 'test.gif'


class ImageModelFactory(NamedModelFactory):
    """Image  model factory class.
    """
    image = factory.django.ImageField(color='blue',
                                      width=IMAGE_WIDTH,
                                      height=IMAGE_HEIGHT,
                                      filename=FILENAME,
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
