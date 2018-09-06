"""
.. module::  documents.test_models
   :synopsis: documents application models unit test module.

*documents* application models models unit test module.
"""
from __future__ import absolute_import, print_function

from django_core_utils.tests.test_utils import (NamedModelTestCase,
                                                VersionedModelTestCase)

from ..models import (IMAGE_FORMAT_GIF, IMAGE_FORMATS,
                      ORIENTATION_LANDSCAPE, VISUAL_ORIENTATION)

from . import factories

class DocumentTestCase(NamedModelTestCase):
    """Document model unit test class.
    """
    def test_document_crud(self):
        self.verify_named_model_crud(
            names=("document_1", "document_2"),
            factory_class=factories.DocumentModelFactory,
            get_by_name="document_1")

    def test_document_fields(self):
        instance = factories.DocumentModelFactory()
        self.assertEqual(instance.document_format.name,
                         'docx',
                         "invalid document format")
        self.assertEqual(instance.document_orientation.name,
                         ORIENTATION_LANDSCAPE,
                         "invalid document orientation")
        
        self.assertTrue(
            '/media/test_domain/documents/test' in instance.image.file.name)

    def test_document_str(self):
        instance = factories.DocumentModelFactory()
        text = str(instance)
        self.assertTrue(text.endswith(
            '{} {}'.format('docx', ORIENTATION_LANDSCAPE)))


class DocumentFormatTestCase(NamedModelTestCase):
    """Document format model unit test class.
    """
    def test_document_format_crud(self):
        self.verify_named_model_crud(
            names=('docx',),
            factory_class=factories.DocumentFormatModelFactory,
            get_by_name='docx')


class DocumentOrientationTestCase(NamedModelTestCase):
    """Document orientation model unit test class.
    """
    def test_image_format_crud(self):
        self.verify_named_model_crud(
            names=VISUAL_ORIENTATION,
            factory_class=factories.DocumentOrientationModelFactory,
            get_by_name=ORIENTATION_LANDSCAPE)


class DocumentReferenceTestCase(VersionedModelTestCase):
    """DocumentReference model unit test class.
    """
    def test_document_reference_crud(self):
        self.verify_versioned_model_crud(
            factory_class=factories.DocumentReferenceModelFactory)

    def test_document_reference_url(self):
        url = "http://www.example.com/document.pdf"
        instance = factories.ImageReferenceModelFactory(
            document=None, url=url)
        instance.clean()
        self.assertEqual(instance.url, url)

class ImageFormatTestCase(NamedModelTestCase):
    """Image format model unit test class.
    """
    def test_image_format_crud(self):
        self.verify_named_model_crud(
            names=IMAGE_FORMATS,
            factory_class=factories.ImageFormatModelFactory,
            get_by_name=IMAGE_FORMAT_GIF)



class ImageTestCase(NamedModelTestCase):
    """Image model unit test class.
    """
    def test_image_crud(self):
        self.verify_named_model_crud(
            names=("image_1", "image_2"),
            factory_class=factories.ImageModelFactory,
            get_by_name="image_1")

    def test_image_fields(self):
        instance = factories.ImageModelFactory()
        self.assertEqual(instance.image_format.name,
                         IMAGE_FORMAT_GIF,
                         "invalid image format")
        self.assertEqual(instance.image_orientation.name,
                         ORIENTATION_LANDSCAPE,
                         "invalid image orientation")
        self.assertEqual(instance.width,
                         factories.ImageModelFactory.IMAGE_WIDTH,
                         "invalid image width")
        self.assertTrue(
            '/media/test_domain/images/test' in instance.image.file.name)

    def test_image_str(self):
        instance = factories.ImageModelFactory()
        text = str(instance)
        self.assertTrue(text.endswith(
            '{} {}'.format(IMAGE_FORMAT_GIF, ORIENTATION_LANDSCAPE)))


class ImageReferenceTestCase(VersionedModelTestCase):
    """ImageReference model unit test class.
    """
    def test_image_reference_crud(self):
        self.verify_versioned_model_crud(
            factory_class=factories.ImageReferenceModelFactory)

    def test_image_reference_url(self):
        url = "http://www.example.com/image.gif"
        instance = factories.ImageReferenceModelFactory(
            image=None, url=url)
        instance.clean()
        self.assertEqual(instance.url, url)
