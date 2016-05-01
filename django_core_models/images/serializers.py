"""
..  module:: django_core_models.images.serializers
    :synopsis: django_core_models images application serializers module.

*django_core_models* images application serializers module.
"""
from __future__ import absolute_import
from django_core_utils.serializers import NamedModelSerializer
from drf_extra_fields.fields import Base64ImageField

from . import models


class DocumentOrientationSerializer(NamedModelSerializer):
    """DocumentOrientation model serializer class."""

    class Meta(NamedModelSerializer.Meta):
        """Meta class definition."""
        model = models.DocumentOrientation


class ImageFormatSerializer(NamedModelSerializer):
    """Image format model serializer class."""

    class Meta(NamedModelSerializer.Meta):
        """Meta class definition."""
        model = models.ImageFormat


class ImageSerializer(NamedModelSerializer):
    """Image model serializer class."""

    image = Base64ImageField()

    class Meta(NamedModelSerializer.Meta):
        """Meta class definition."""
        model = models.Image
        fields = NamedModelSerializer.Meta.fields + (
            "image", "image_format",
            "image_orientation", "width", "height")

        read_only_fields = ("width", "height",)
    
    