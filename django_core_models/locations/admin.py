"""
.. module::  location.admin
   :synopsis:  Django location application admin  module.

Django location application admin  module.

"""
from __future__ import absolute_import

from django.contrib import admin

from django_core_utils.admin import (NamedModelAdmin, VersionedModelAdmin,
                                     admin_site_register,
                                     named_model_admin_class_attrs)
from python_core_utils.core import class_name

from .forms import (AddressAdminForm, CityAdminForm, CountryAdminForm,
                    GeographicLocationAdminForm, LanguageAdminForm,
                    ProvinceAdminForm, StateAdminForm, TimezoneAdminForm)
from .models import (Address, AddressType, City, Country, GeographicLocation,
                     GeographicLocationType, Language, LanguageType, Province,
                     State, Timezone, TimezoneType)

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
    form = AddressAdminForm

    fieldsets = (
        ('Address',
         {'fields': _address_fields}),
    ) + NamedModelAdmin.get_field_sets()

_country_fields = (
    ("name",),
    ("iso_code",),
    ("alias",),
    ("description",),)


class CountryAdmin(NamedModelAdmin):
    """
    Country model admin class
    """
    form = CountryAdminForm

    fieldsets = (
        ('Country',
         {'fields': _country_fields}),
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
    form = CityAdminForm

    fieldsets = (
        ('City',
         {'fields': _city_fields()}),
    ) + NamedModelAdmin.get_field_sets()

_geographic_location_fields = (
    ("latitude",),
    ("longitude",),
    ("name",),
    ("alias",),
    ("description",),)


class GeographicLocationAdmin(NamedModelAdmin):
    """
    Geographic location model admin class
    """
    form = GeographicLocationAdminForm

    fieldsets = (
        ('Geographic location',
         {'fields': _geographic_location_fields}),
    ) + NamedModelAdmin.get_field_sets()


_language_fields = (
    ("name",),
    ("iso_code",),
    ("alias",),
    ("description",),)


class LanguageAdmin(NamedModelAdmin):
    """
    Language model admin class
    """
    form = LanguageAdminForm

    fieldsets = (
        ('Language',
         {'fields': _language_fields}),
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
    form = TimezoneAdminForm

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


class StateAdmin(NamedModelAdmin):
    """
    State model admin class
    """
    form = StateAdminForm

    fieldsets = (
        ('State',
         {'fields': _region_fields()}),
    ) + NamedModelAdmin.get_field_sets()


class ProvinceAdmin(NamedModelAdmin):
    """
    Province model admin class
    """
    form = ProvinceAdminForm

    fieldsets = (
        ('Province',
         {'fields': _region_fields()}),
    ) + NamedModelAdmin.get_field_sets()

_named_classes = (AddressType, LanguageType,
                  GeographicLocationType, TimezoneType,
                  )

for clasz in _named_classes:
    admin_site_register(
        clasz,
        (NamedModelAdmin,),
        named_model_admin_class_attrs(class_name(clasz)))

_other_model_classes = (Address, City, Country,
                        GeographicLocation, Language,
                        Province, State,
                        Timezone, )
_other_admin_classes = (AddressAdmin, CityAdmin, CountryAdmin,
                        GeographicLocationAdmin, LanguageAdmin,
                        ProvinceAdmin, StateAdmin,
                        TimezoneAdmin, )

for model_class, admin_class in zip(_other_model_classes,
                                    _other_admin_classes):
    admin.site.register(model_class, admin_class)
