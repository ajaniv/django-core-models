"""
..  module:: location.text
    :synopsis: Django location application text  module.

Django location application text  module.
"""
from django.utils.translation import ugettext_lazy as _

# flake8: noqa
# required because of pep8 regression in ignoring disable of E123
address_labels = {
    "country": _("Country"),
    "city": _("City"),
    "extended_address": _("Extended street address"),
    "geographic_lcoation": _("Geographic location"),
    "label": _("Label"),
    "postal_code": _("Postal code"),
    "post_office_box": _("Post office box"),
    "province": _("Province"),
    "state": _("State"),
    "street_address": _("Street address"),
    "timezone": _("Timezone"),
    }

address_help_texts = {
    "country": _("Country."),
    "city": _("City."),
    "extended_street_address": _("Extended street address."),
    "geographic_lcoation": _("Geographic location."),
    "label": _("Label."),
    "postal_code": _("Postal code."),
    "post_office_box": _("Post office box."),
    "province": _("Province."),
    "state": _("State."),
    "street_address": _("Street address."),
    "timezone": _("Timezone."),
    }

city_labels = {
    "province": _("Province"),
    "state": _("State"),
    }

city_help_texts = {
    "province": _("Province."),
    "state": _("State."),
    }

country_labels = {
    "iso_code": _("ISO code"),
    }

country_help_texts = {
    "iso_code": _("ISO 3166-1 alpha-2."),
    }

geographic_location_labels = {
    "latitude": _("Latitude"),
    "longitude": _("Longitude"),
    "range": _("Range"),
    "range_unit": _("Unit"),
    }

geographic_location_help_texts = {
    "latitude": _("Latitude."),
    "longitude": _("Longitude."),
    "range": _("Range in unit."),
    "range_unit": _("Distance unit."),
    }

language_labels = {
    "iso_code": _("ISO code"),
    }

language_help_texts = {
    "iso_code": _("ISO code."),
    }

region_labels = {
    "country": _("Country"),
    "iso_code": _("ISO code"),
    }

region_help_texts = {
    "country": _("Country."),
    "iso_code": _("ISO code."),
    }

timezone_labels = {
    "timezone": _("Timezone"),
    }

timezone_help_texts = {
    "timezone": _("Timezone."),
    }
