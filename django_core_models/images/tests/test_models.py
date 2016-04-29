"""
.. module::  images.test_models
   :synopsis: image application models unit test module.

*image* application models models unit test module.
"""
from __future__ import print_function

import factory

from django_core_utils.tests.factories import NamedModelFactory
from django_core_utils.tests.test_utils import NamedModelTestCase

from ..models import (IMAGE_FORMAT_GIF, IMAGE_FORMATS, ORIENTATION_LANDSCAPE,
                      VISUAL_ORIENTATION, DocumentOrientation, Image,
                      ImageFormat)


class ImageFormatModelFactory(NamedModelFactory):
    """Image format model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = ImageFormat

    name = IMAGE_FORMAT_GIF


class ImageFormatTestCase(NamedModelTestCase):
    """Image format model unit test class.
    """
    def test_image_format_crud(self):
        self.verify_named_model_crud(
            names=IMAGE_FORMATS,
            factory_class=ImageFormatModelFactory,
            get_by_name=IMAGE_FORMAT_GIF)


class DocumentOrientationModelFactory(NamedModelFactory):
    """Document orientation model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = DocumentOrientation

    name = ORIENTATION_LANDSCAPE


class DocumentOrientationTestCase(NamedModelTestCase):
    """Document orientation model unit test class.
    """
    def test_image_format_crud(self):
        self.verify_named_model_crud(
            names=VISUAL_ORIENTATION,
            factory_class=DocumentOrientationModelFactory,
            get_by_name=ORIENTATION_LANDSCAPE)


IMAGE_WIDTH = 128
IMAGE_HEIGHT = 128
FILENAME = 'test.gif'


class ImageFactory(NamedModelFactory):
    """Image  model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = Image

    image = factory.django.ImageField(color='blue',
                                      width=IMAGE_WIDTH,
                                      height=IMAGE_HEIGHT,
                                      filename=FILENAME,
                                      format=IMAGE_FORMAT_GIF)
    image_format = factory.SubFactory(ImageFormatModelFactory)
    image_orientation = factory.SubFactory(DocumentOrientationModelFactory)


class ImageTestCase(NamedModelTestCase):
    """Image model unit test class.
    """
    def test_image_crud(self):
        self.verify_named_model_crud(
            names=("image_1", "image_2"),
            factory_class=ImageFactory,
            get_by_name="image_1")

    def test_image_fields(self):
        instance = ImageFactory()
        self.assertEqual(instance.image_format.name,
                         IMAGE_FORMAT_GIF,
                         "invalid image format")
        self.assertEqual(instance.image_orientation.name,
                         ORIENTATION_LANDSCAPE,
                         "invalid image orientation")
        self.assertEqual(instance.width, IMAGE_WIDTH, "invalid image width")
        self.assertTrue(
            '/media/test_domain/images/test' in instance.image.file.name)

    def test_image_str(self):
        instance = ImageFactory()
        text = str(instance)
        self.assertTrue(text.endswith(
            '{} {}'.format(IMAGE_FORMAT_GIF, ORIENTATION_LANDSCAPE)))
