"""
.. module::  django_core_models.images.tests.test_views
   :synopsis: images models application views unit test module.

*images* application views unit test module.
"""
from __future__ import absolute_import, print_function
import six
from django_core_utils.tests.api_test_utils import (NamedModelApiTestCase,
                                                    VersionedModelApiTestCase)
from python_core_utils.image import encode_file
from . import factories
from .. import models
from .. import serializers


class DocumentOrientationApiTestCase(NamedModelApiTestCase):
    """DocumentOrientation API unit test class."""
    factory_class = factories.DocumentOrientationModelFactory
    model_class = models.DocumentOrientation
    serializer_class = serializers.DocumentOrientationSerializer

    url_detail = "document-orientation-detail"
    url_list = "document-orientation-list"

    name = factories.DocumentOrientationModelFactory.name

    def test_create_document_orientation(self):
        self.verify_create_defaults()

    def test_create_document_orientation_partial(self):
        self.verify_create_defaults_partial()

    def test_get_document_orientation(self):
        self.verify_get_defaults()

    def test_put_document_orientation_partial(self):
        self.verify_put_partial()

    def test_delete_document_orientation(self):
        self.verify_delete_default()


class ImageFormatApiTestCase(NamedModelApiTestCase):
    """ImageFormat API unit test class."""
    factory_class = factories.ImageFormatModelFactory
    model_class = models.ImageFormat
    serializer_class = serializers.ImageFormatSerializer

    url_detail = "image-format-detail"
    url_list = "image-format-list"

    name = factories.ImageFormatModelFactory.name

    def test_create_image_format(self):
        self.verify_create_defaults()

    def test_create_image_format_partial(self):
        self.verify_create_defaults_partial()

    def test_get_image_format(self):
        self.verify_get_defaults()

    def test_put_image_format_partial(self):
        self.verify_put_partial()

    def test_delete_image_format(self):
        self.verify_delete_default()


class ImageApiTestCase(NamedModelApiTestCase):
    """Image API unit test class."""
    factory_class = factories.ImageModelFactory
    model_class = models.Image
    serializer_class = serializers.ImageSerializer

    url_detail = "image-detail"
    url_list = "image-list"

    # Factory name is used in reference image
    # and cannot be used.
    name = "api-test-image"

    def encode_image(self, file_name):
        # @TODO: revisit this implementation
        image_file = open(file_name, 'rb')
        encoded_data = encode_file(image_file)
        if six.PY3:
            encoded_data_str = str(encoded_data, encoding='ascii')
        else:
            encoded_data_str = str(encoded_data)
        return encoded_data_str

    def image_data(self, instance):
        instance = instance or self.factory_class()

        encoded_data = self.encode_image(instance.image.file.name)
        data = dict(image_format=instance.image_format.id,
                    image_orientation=instance.image_orientation.id,
                    image=encoded_data)
        return data

    def post_required_data(self, ref_instance, user=None, site=None):
        """Return named model post request required data."""
        data = super(ImageApiTestCase, self).post_required_data(user, site)
        data.update(self.image_data(ref_instance))
        return data

    def verify_create_image(self, ref_instance=None,
                            data=None, expected_name=None):
        """Generate post request for image creation."""
        data = data or self.post_required_data(ref_instance)
        response, instance = self.verify_create(
            url=self.url_list,
            data=data,
            model_class=self.model_class,
            expected_name=expected_name)

        if ref_instance:
            self.assert_instance_equal(
                ref_instance, instance,
                ("image_format", "image_orientation", "height", "width"))
        return response, instance

    def test_create_image(self):
        instance = self.create_instance_default()
        self.verify_create_image(ref_instance=instance,
                                 expected_name=self.name)

    def test_create_image_partial(self):
        instance = self.create_instance_default()
        data = self.image_data(instance)
        data["name"] = self.name
        self.verify_create_image(ref_instance=instance,
                                 data=data,
                                 expected_name=self.name)

    def test_get_image(self):
        # Local file storeage image location is different from server
        self.verify_get_defaults(excluded=["image"])

    def test_put_image_partial(self):
        instance = self.create_instance_default()
        data = self.image_data(instance)
        data.update(dict(id=instance.id, name=self.name))
        self.verify_put(
            self.url_detail, instance, data, self.serializer_class, ["image"])

    def test_delete_image(self):
        self.verify_delete_default()


class ImageReferenceApiTestCase(VersionedModelApiTestCase):
    """ImageReference api test cases class."""
    factory_class = factories.ImageReferenceModelFactory
    model_class = models.ImageReference
    serializer_class = serializers.ImageReferenceSerializer

    url_detail = "image-reference-detail"
    url_list = "image-reference-list"

    image_url = "http://www.example.com/image.gif"

    def image_reference_data(self, instance):
        """return image reference data"""
        instance = instance or self.factory_class()
        data = dict(image=instance.image.id)
        return data

    def post_required_data(self, ref_instance, user=None, site=None):
        """Return named model post request required data."""
        data = super(
            ImageReferenceApiTestCase, self).post_required_data(user, site)
        data.update(self.image_reference_data(ref_instance))
        return data

    def verify_create_image_reference(
            self, ref_instance=None,
            data=None, attrs=None):
        """Generate post request for image reference creation."""
        data = data or self.post_required_data(ref_instance)

        response, instance = self.verify_create(
            url_name=self.url_list,
            data=data,
            model_class=self.model_class)

        attrs = attrs or ("image", )
        if ref_instance:
            self.assert_instance_equal(ref_instance, instance, attrs)

        return response, instance

    def test_create_image_reference(self):
        instance = self.create_instance_default()
        self.verify_create_image_reference(
            ref_instance=instance)

    def test_create_image_reference_partial(self):
        instance = self.create_instance_default()
        data = self.image_reference_data(instance)
        self.verify_create_image_reference(
            ref_instance=instance,
            data=data)

    def test_get_image_reference(self):
        self.verify_get_defaults()

    def test_put_image_reference_partial(self):
        instance = self.create_instance_default()
        data = dict(id=instance.id, image=None, url=self.image_url)
        self.verify_put(self.url_detail, instance, data, self.serializer_class)

    def test_delete_image_reference(self):
        self.verify_delete_default()
