"""
..  module:: django_core_models_libs.serializer_utils
    :synopsis: django_core_models serializer utilities  module.

*django_core_models* serializer utilities  module.
"""
from __future__ import absolute_import
from django_core_utils.serializers import NamedModelSerializer

from django_core_utils.models import NamedModel


class ISOSerializer(NamedModelSerializer):
    """Base class iso model serializer class."""

    class Meta(NamedModelSerializer.Meta):
        """Meta class definition."""
        model = NamedModel
        fields = NamedModelSerializer.Meta.fields + ("iso_code",)
