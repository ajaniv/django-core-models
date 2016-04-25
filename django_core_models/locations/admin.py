"""
.. module::  location.admin
   :synopsis:  Django location application admin  module.

Django location application admin  module.

"""
from __future__ import absolute_import

from django.contrib import admin

from django_core_models_libs.admin_utils import iso_fields, iso_list_display
from django_core_utils.admin import (NamedModelAdmin, VersionedModelAdmin,
                                     admin_site_register,
                                     named_model_admin_class_attrs)
from python_core_utils.core import class_name

from . import forms
from . import models

DISPLAY_ADDRESS_SIZE = 60
_address_fields = (
    ("label",),
    ("street_address", "post_office_box"),
    ("extended_address",),
    ("city",),
    ("state", "province"),
    ("country",),
    ("postal_code",),
    ("timezone",),
    ("geographic_location",))


class AddressAdmin(VersionedModelAdmin):
    """
    Address model admin class
    """
    form = forms.AddressAdminForm
    list_display = ("id", "label", "get_address",
                    "version", "update_time", "update_user")
    list_display_links = ("id", "get_address", )

    fieldsets = (
        ('Address',
         {'fields': _address_fields}),
    ) + NamedModelAdmin.get_field_sets()

    def get_address(self, instance):
        """return instance address."""
        return str(instance)[:DISPLAY_ADDRESS_SIZE]
    get_address.short_description = "address"


class CountryAdmin(NamedModelAdmin):
    """
    Country model admin class
    """
    form = forms.CountryAdminForm

    list_display = iso_list_display

    fieldsets = (
        ('Country',
         {'fields': iso_fields}),
    ) + NamedModelAdmin.get_field_sets()


def _city_fields():
    return (("name",),
            ("state", "province"),
            ("alias",),
            ("description",),)


class CityAdmin(NamedModelAdmin):
    """
    City model admin class
    """
    form = forms.CityAdminForm

    list_display = ("id", "get_name", "alias", "get_region",
                    "version", "update_time", "update_user")

    fieldsets = (
        ('City',
         {'fields': _city_fields()}),
    ) + NamedModelAdmin.get_field_sets()

    def get_region(self, instance):
        """return instance region."""
        return instance.region
    get_region.short_description = "region"

_geographic_location_fields = (
    ("latitude",),
    ("longitude",),
    ("range",),
    ("unit",),
    ("name",),
    ("alias",),
    ("description",),)


class GeographicLocationAdmin(NamedModelAdmin):
    """
    Geographic location model admin class
    """
    form = forms.GeographicLocationAdminForm
    list_display = ("id", "get_name", "alias", "get_latitude", "get_longitude",
                    "version", "update_time", "update_user")

    fieldsets = (
        ('Geographic location',
         {'fields': _geographic_location_fields}),
    ) + NamedModelAdmin.get_field_sets()

    def _formatted_value(self, value):
        return "{0:9.5f}".format(value)

    def _text(self, value):
        return ("<div style='width:65px;'>" +
                "<div style='text-align:right;white-space:pre'>" +
                value + "</div></div>")

    def get_latitude(self, instance):
        """return latitude."""
        value = self._formatted_value(instance.latitude)
        return self._text(value)
    get_latitude.short_description = "latitude"
    get_latitude.allow_tags = True

    def get_longitude(self, instance):
        """return longitude."""
        value = self._formatted_value(instance.longitude)
        return self._text(value)

    get_longitude.short_description = "longitude"
    get_longitude.allow_tags = True


class LanguageAdmin(NamedModelAdmin):
    """
    Language model admin class
    """
    form = forms.LanguageAdminForm
    list_display = iso_list_display

    fieldsets = (
        ('Language',
         {'fields': iso_fields}),
    ) + NamedModelAdmin.get_field_sets()


_timezone_fields = (
    ("timezone",),
    ("name",),
    ("alias",),
    ("description",),)


class TimezoneAdmin(NamedModelAdmin):
    """
    Timezone model admin class
    """
    form = forms.TimezoneAdminForm
    list_display = ("id", "get_name", "alias", "timezone",
                    "version", "update_time", "update_user")
    fieldsets = (
        ('Timezone',
         {'fields': _timezone_fields}),
    ) + NamedModelAdmin.get_field_sets()


def _region_fields():
    return (("name",),
            ("iso_code",),
            ("country",),
            ("alias",),
            ("description",),)

_region_list_display = ("id", "get_name", "alias", "iso_code", "country",
                        "version", "update_time", "update_user")


class StateAdmin(NamedModelAdmin):
    """
    State model admin class
    """
    form = forms.StateAdminForm
    list_display = _region_list_display

    fieldsets = (
        ('State',
         {'fields': _region_fields()}),
    ) + NamedModelAdmin.get_field_sets()


class ProvinceAdmin(NamedModelAdmin):
    """
    Province model admin class
    """
    form = forms.ProvinceAdminForm
    list_display = _region_list_display

    fieldsets = (
        ('Province',
         {'fields': _region_fields()}),
    ) + NamedModelAdmin.get_field_sets()


_named_classes = (models.AddressType, models.DistanceUnit,
                  models.GeographicLocationType,
                  models.LanguageType,
                  models.TimezoneType,
                  )

for clasz in _named_classes:
    admin_site_register(
        clasz,
        (NamedModelAdmin,),
        named_model_admin_class_attrs(class_name(clasz)))

_other_model_classes = (models.Address, models.City, models.Country,
                        models.GeographicLocation, models.Language,
                        models.Province, models.State,
                        models.Timezone, )
_other_admin_classes = (AddressAdmin, CityAdmin, CountryAdmin,
                        GeographicLocationAdmin, LanguageAdmin,
                        ProvinceAdmin, StateAdmin,
                        TimezoneAdmin, )

for model_class, admin_class in zip(_other_model_classes,
                                    _other_admin_classes):
    admin.site.register(model_class, admin_class)
