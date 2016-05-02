"""
..  module:: django_core_models.locations.serializers
    :synopsis: django_core_models location application serializers  module.

*django_core_models* location application serializers module.
"""
from __future__ import absolute_import
import six
from rest_framework import serializers
from django_core_utils.serializers import (NamedModelSerializer,
                                           OptionalNamedModelSerializer,
                                           VersionedModelSerializer)
from django_core_models_libs.serializer_utils import ISOSerializer

from . import models


class AddressTypeSerializer(NamedModelSerializer):
    """AddressType model serializer class."""

    class Meta(NamedModelSerializer.Meta):
        """Meta class definition."""
        model = models.AddressType


class CountrySerializer(ISOSerializer):
    """Country model serializer class."""

    class Meta(ISOSerializer.Meta):
        """Meta class definition."""
        model = models.Country


class CitySerializer(NamedModelSerializer):
    """City model serializer class."""

    class Meta(NamedModelSerializer.Meta):
        """Meta class definition."""
        model = models.City
        fields = NamedModelSerializer.Meta.fields + ("state", "province")


class DistanceUnitSerializer(NamedModelSerializer):
    """DistanceUnit model serializer class."""

    class Meta(NamedModelSerializer.Meta):
        """Meta class definition."""
        model = models.DistanceUnit


class GeographicLocationTypeSerializer(NamedModelSerializer):
    """GeographicLocationType model serializer class."""

    class Meta(NamedModelSerializer.Meta):
        """Meta class definition."""
        model = models.GeographicLocationType


class GeographicLocationSerializer(OptionalNamedModelSerializer):
    """GeographicLocation model serializer class."""

    class Meta(NamedModelSerializer.Meta):
        """Meta class definition."""
        model = models.GeographicLocation
        fields = OptionalNamedModelSerializer.Meta.fields + (
            "latitude", "longitude", "range", "range_unit")


class LanguageTypeSerializer(NamedModelSerializer):
    """LanguageType model serializer class."""

    class Meta(NamedModelSerializer.Meta):
        """Meta class definition."""
        model = models.LanguageType


class LanguageSerializer(ISOSerializer):
    """Language model serializer class."""

    class Meta(ISOSerializer.Meta):
        """Meta class definition."""
        model = models.Language


class TimezoneTypeSerializer(NamedModelSerializer):
    """TimezoneType model serializer class."""

    class Meta(NamedModelSerializer.Meta):
        """Meta class definition."""
        model = models.TimezoneType


class TimezoneSerializer(OptionalNamedModelSerializer):
    """Timezone model serializer class."""
    timezone = serializers.SerializerMethodField()

    class Meta(NamedModelSerializer.Meta):
        """Meta class definition."""
        model = models.Timezone
        fields = OptionalNamedModelSerializer.Meta.fields + ("timezone",)

    def get_timezone(self, obj):
        return six.text_type(obj.timezone)


class RegionSerializer(ISOSerializer):
    """Region model serializer class."""

    class Meta(ISOSerializer.Meta):
        """Meta class definition."""
        model = models.Region
        fields = ISOSerializer.Meta.fields + ("country",)


class ProvinceSerializer(RegionSerializer):
    """Province model serializer class."""

    class Meta(RegionSerializer.Meta):
        """Meta class definition."""
        model = models.Province


class StateSerializer(RegionSerializer):
    """State model serializer class."""

    class Meta(RegionSerializer.Meta):
        """Meta class definition."""
        model = models.State


class AddressSerializer(VersionedModelSerializer):
    """Address model serializer class."""

    class Meta(VersionedModelSerializer.Meta):
        """Meta class definition."""
        model = models.Address
        fields = VersionedModelSerializer.Meta.fields + (
            "label", "post_office_box", "street_address",
            "extended_address", "city", "state", "province",
            "country", "postal_code", "timezone", "geographic_location")
