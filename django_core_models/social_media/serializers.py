"""
..  module:: django_core_models.social_medial.serializers
    :synopsis: django_core_models social_medial application serializers module.

*django_core_models* social_medial application serializers module.
"""
from __future__ import absolute_import

from django_core_utils.serializers import (NamedModelSerializer,
                                           VersionedModelSerializer)
from rest_framework import serializers
from . import models


class EmailSerializer(VersionedModelSerializer):
    """Email model serializer class."""

    class Meta(VersionedModelSerializer.Meta):
        """Meta class definition."""
        model = models.Email
        fields = VersionedModelSerializer.Meta.fields + (
            "address",)


class EmailTypeSerializer(NamedModelSerializer):
    """EmailType model serializer class."""

    class Meta(NamedModelSerializer.Meta):
        """Meta class definition."""
        model = models.EmailType


class SimpleNameSerializer(VersionedModelSerializer):
    """SimpleName serializer class."""
    class Meta(VersionedModelSerializer.Meta):
        """Meta class definition."""
        model = models.SimpleName
        fields = VersionedModelSerializer.Meta.fields + (
            "name",)


class FormattedNameSerializer(SimpleNameSerializer):
    """FormattedName model serializer class."""

    class Meta(SimpleNameSerializer.Meta):
        """Meta class definition."""
        model = models.FormattedName


class NicknameSerializer(SimpleNameSerializer):
    """Nickname model serializer class."""

    class Meta(SimpleNameSerializer.Meta):
        """Meta class definition."""
        model = models.Nickname


class GroupSerializer(NamedModelSerializer):
    """Group model serializer class."""

    class Meta(NamedModelSerializer.Meta):
        """Meta class definition."""
        model = models.Group


class InstantMessagingTypeSerializer(NamedModelSerializer):
    """InstantMessagingType model serializer class."""

    class Meta(NamedModelSerializer.Meta):
        """Meta class definition."""
        model = models.InstantMessagingType


class LogoTypeSerializer(NamedModelSerializer):
    """LogoType model serializer class."""

    class Meta(NamedModelSerializer.Meta):
        """Meta class definition."""
        model = models.LogoType


class NameSerializer(VersionedModelSerializer):
    """Name model serializer class."""

    # these field definitions are required because of the unique_together
    # definition on the model field and DRF handling of it.

    additional_name = serializers.CharField(required=False, default='')

    class Meta(VersionedModelSerializer.Meta):
        """Meta class definition."""
        model = models.Name
        fields = VersionedModelSerializer.Meta.fields + (
            "family_name", "given_name", "additional_name",
            "honorific_prefix", "honorific_suffix")


class NicknameTypeSerializer(NamedModelSerializer):
    """NicknameType model serializer class."""

    class Meta(NamedModelSerializer.Meta):
        """Meta class definition."""
        model = models.NicknameType


class PhoneSerializer(VersionedModelSerializer):
    """Phone model serializer class."""

    class Meta(VersionedModelSerializer.Meta):
        """Meta class definition."""
        model = models.Phone
        fields = VersionedModelSerializer.Meta.fields + (
            "number",)


class PhoneTypeSerializer(NamedModelSerializer):
    """PhoneType model serializer class."""

    class Meta(NamedModelSerializer.Meta):
        """Meta class definition."""
        model = models.PhoneType


class PhotoTypeSerializer(NamedModelSerializer):
    """PhotoType model serializer class."""

    class Meta(NamedModelSerializer.Meta):
        """Meta class definition."""
        model = models.PhotoType


class UrlSerializer(VersionedModelSerializer):
    """Url model serializer class."""

    class Meta(VersionedModelSerializer.Meta):
        """Meta class definition."""
        model = models.Url
        fields = VersionedModelSerializer.Meta.fields + (
            "address",)


class UrlTypeSerializer(NamedModelSerializer):
    """UrlType model serializer class."""

    class Meta(NamedModelSerializer.Meta):
        """Meta class definition."""
        model = models.UrlType
