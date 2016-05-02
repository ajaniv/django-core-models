"""
..  module:: django_core_models.demographics.serializers
    :synopsis: django_core_models demographics application serializers module.

*django_core_models* demographics application serializers module.
"""
from __future__ import absolute_import
from django_core_utils.serializers import NamedModelSerializer

from . import models


class AgeSerializer(NamedModelSerializer):
    """Age model serializer class."""

    class Meta(NamedModelSerializer.Meta):
        """Meta class definition."""
        model = models.Age


class ChildCountSerializer(NamedModelSerializer):
    """Child count model serializer class."""

    class Meta(NamedModelSerializer.Meta):
        """Meta class definition."""
        model = models.ChildCount


class DemographicRegionSerializer(NamedModelSerializer):
    """Demographic region model serializer class."""

    class Meta(NamedModelSerializer.Meta):
        """Meta class definition."""
        model = models.DemographicRegion


class EducationLevelSerializer(NamedModelSerializer):
    """Education level region model serializer class."""

    class Meta(NamedModelSerializer.Meta):
        """Meta class definition."""
        model = models.EducationLevel


class EthnicitySerializer(NamedModelSerializer):
    """Ethnicity model serializer class."""

    class Meta(NamedModelSerializer.Meta):
        """Meta class definition."""
        model = models.Ethnicity


class GenderSerializer(NamedModelSerializer):
    """Gender model serializer class."""

    class Meta(NamedModelSerializer.Meta):
        """Meta class definition."""
        model = models.Gender


class HouseholdSizeSerializer(NamedModelSerializer):
    """HouseholdSize model serializer class."""

    class Meta(NamedModelSerializer.Meta):
        """Meta class definition."""
        model = models.HouseholdSize


class IncomeSerializer(NamedModelSerializer):
    """Income model serializer class."""

    class Meta(NamedModelSerializer.Meta):
        """Meta class definition."""
        model = models.Income
