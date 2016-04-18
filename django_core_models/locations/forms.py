"""
.. module::  location.forms
   :synopsis:  Django location application forms  module.

Django location application forms  module.

"""
from __future__ import absolute_import

from django_core_utils import forms
from python_core_utils.core import dict_merge

from .models import (Address, City, Country, GeographicLocation, Language,
                     Province, Region, State, Timezone)
from .text import (address_help_texts, address_labels, city_help_texts,
                   city_labels, country_help_texts, country_labels,
                   geographic_location_help_texts, geographic_location_labels,
                   language_help_texts, language_labels, region_help_texts,
                   region_labels, timezone_help_texts, timezone_labels)


class AddressAdminForm(forms.VersionedModelAdminForm):
    """Address model admin form  class.
    """
    class Meta(forms.VersionedModelAdminForm.Meta):
        """Form meta class."""
        model = Address
        labels = dict_merge(
            forms.NamedModelAdminForm.Meta.labels,
            address_labels)

        help_texts = dict_merge(
            forms.NamedModelAdminForm.Meta.help_texts,
            address_help_texts)


class CityAdminForm(forms.NamedModelAdminForm):
    """City  model admin form class.
    """
    class Meta(forms.NamedModelAdminForm.Meta):
        """Form meta class."""
        model = City
        labels = dict_merge(
            forms.NamedModelAdminForm.Meta.labels,
            city_labels)

        help_texts = dict_merge(
            forms.NamedModelAdminForm.Meta.help_texts,
            city_help_texts)


class CountryAdminForm(forms.NamedModelAdminForm):
    """Country  model admin form class.
    """
    class Meta(forms.NamedModelAdminForm.Meta):
        """Form meta class."""
        model = Country
        labels = dict_merge(
            forms.NamedModelAdminForm.Meta.labels,
            country_labels)

        help_texts = dict_merge(
            forms.NamedModelAdminForm.Meta.help_texts,
            country_help_texts)


class GeographicLocationAdminForm(forms.NamedModelAdminForm):
    """Geographic location model admin form  class.
    """
    class Meta(forms.NamedModelAdminForm.Meta):
        """Form meta class."""
        model = GeographicLocation
        labels = dict_merge(
            forms.NamedModelAdminForm.Meta.labels,
            geographic_location_labels)

        help_texts = dict_merge(
            forms.NamedModelAdminForm.Meta.help_texts,
            geographic_location_help_texts)


class LanguageAdminForm(forms.NamedModelAdminForm):
    """Language  model admin form class.
    """
    class Meta(forms.NamedModelAdminForm.Meta):
        """Form meta class."""
        model = Language
        labels = dict_merge(
            forms.NamedModelAdminForm.Meta.labels,
            language_labels)

        help_texts = dict_merge(
            forms.NamedModelAdminForm.Meta.help_texts,
            language_help_texts)


class TimezoneAdminForm(forms.NamedModelAdminForm):
    """Timezone  model admin form class.
    """
    class Meta(forms.NamedModelAdminForm.Meta):
        """Form meta class."""
        model = Timezone
        labels = dict_merge(
            forms.NamedModelAdminForm.Meta.labels,
            timezone_labels)

        help_texts = dict_merge(
            forms.NamedModelAdminForm.Meta.help_texts,
            timezone_help_texts)


class RegionAdminForm(forms.NamedModelAdminForm):
    """Region  model admin form class.
    """
    class Meta(forms.NamedModelAdminForm.Meta):
        """Form meta class."""
        model = Region
        labels = dict_merge(
            forms.NamedModelAdminForm.Meta.labels,
            region_labels)

        help_texts = dict_merge(
            forms.NamedModelAdminForm.Meta.help_texts,
            region_help_texts)


class ProvinceAdminForm(RegionAdminForm):
    """Province model admin form class.
    """
    class Meta(RegionAdminForm.Meta):
        """Form meta class."""
        model = Province


class StateAdminForm(RegionAdminForm):
    """State model admin form class.
    """
    class Meta(RegionAdminForm.Meta):
        """Form meta class."""
        model = State
