"""
..  module:: django_core_models.core.serializers
    :synopsis: django_core_models core application serializers  module.

*django_core_models* core application serializers module.
"""
from __future__ import absolute_import
from django_core_utils.serializers import (NamedModelSerializer,
                                           OptionalNamedModelSerializer)

from . import models


class AnnotationSerializer(OptionalNamedModelSerializer):
    """Versioned model serializer class."""

    class Meta(OptionalNamedModelSerializer.Meta):
        """Meta class definition."""
        model = models.Annotation
        fields = OptionalNamedModelSerializer.Meta.fields + ("annotation",)


class CategorySerializer(NamedModelSerializer):
    """Category model serializer class."""

    class Meta(NamedModelSerializer.Meta):
        """Meta class definition."""
        model = models.Category


class CurrencySerializer(NamedModelSerializer):
    """Currency model serializer class."""

    class Meta(NamedModelSerializer.Meta):
        """Meta class definition."""
        model = models.Currency
        fields = NamedModelSerializer.Meta.fields + ("iso_code",)
