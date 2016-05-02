"""
.. module::  location.models
   :synopsis:  location models module

*location* application models module.

"""
from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _
from inflection import humanize, pluralize, underscore

from django_core_utils import fields
from django_core_utils.models import (NamedModel, OptionalNamedModel,
                                      VersionedModel, db_table)

from . import validation

_app_label = "locations"

_country = "Country"
_country_verbose = humanize(underscore(_country))


class Country(NamedModel):
    """Country model class.

    Uses 2 characters as per  ISO 3166.
    """
    ISO_3166_2_US = "US"
    iso_code = fields.char_field(max_length=2, unique=True)

    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _country)
        verbose_name = _(_country_verbose)
        verbose_name_plural = _(pluralize(_country_verbose))

    def is_usa(self):
        return self.iso_code == self.ISO_3166_2_US

    def clean(self):
        """Perform cross field validation.
        """
        super(Country, self).clean()
        validation.country_validation(self)

_distance_unit = "DistanceUnit"
_distance_unit_verbose = humanize(underscore(_distance_unit))


class DistanceUnit(NamedModel):
    """Distance unit model class.

    Designed for values such as meter, yard, mile, kilometer
    """
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _distance_unit)
        verbose_name = _(_distance_unit_verbose)
        verbose_name_plural = _(pluralize(_distance_unit_verbose))

_geographic_location_type = "GeographicLocationType"
_geographic_location_type_verbose = humanize(
    underscore(_geographic_location_type))


class GeographicLocationType(NamedModel):
    """GeographicLocation type model class.

    Allow GeographicLocation classification.
    Values may include "unknown".
    """
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _geographic_location_type)
        verbose_name = _(_geographic_location_type_verbose)
        verbose_name_plural = _(pluralize(_geographic_location_type_verbose))

_geographic_location = "GeographicLocation"
_geographic_location_verbose = humanize(
    underscore(_geographic_location))


class GeographicLocation(OptionalNamedModel):
    """Geographic location model class.

    Captures geographic location data.
    """
    # @TODO: Add foreign key to GeographicLocationType?
    GEO_RANGE_MAX_DIGITS = 5
    GEO_RANGE_DECIMAL_PLACES = 2
    GEO_RANGE_DEFAULT = 10.0

    latitude = fields.latitude_field(default=None)
    longitude = fields.longitude_field(default=None)
    range = fields.decimal_field(
        blank=True, null=True,
        default=None,
        max_digits=GEO_RANGE_MAX_DIGITS,
        decimal_places=GEO_RANGE_DECIMAL_PLACES)
    range_unit = fields.foreign_key_field(DistanceUnit, blank=True, null=True)

    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _geographic_location)
        verbose_name = _(_geographic_location_verbose)
        verbose_name_plural = _(pluralize(_geographic_location_verbose))

    def __str__(self):
        value = "{0:9.5f} {1:9.5f}".format(self.latitude, self.longitude)
        return value

    def clean(self):
        """Perform cross field validation.
        """
        super(GeographicLocation, self).clean()
        validation.geographic_location_validation(self)

_language_type = "LanguageType"
_language_type_verbose = humanize(underscore(_language_type))


class LanguageType(NamedModel):
    """Language type model class.

    Allow language classification.
    Values may include "unknown".
    """
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _language_type)
        verbose_name = _(_language_type_verbose)
        verbose_name_plural = _(pluralize(_language_type_verbose))

_language = "Language"
_language_verbose = humanize(underscore(_language))


class Language(NamedModel):
    """Language model class.

    Uses 2 characters as per ISO 639-1.
    """
    # @TODO: Add foreign key to LanguageType?
    iso_code = fields.char_field(max_length=2, unique=True)

    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _language)
        verbose_name = _(_language_verbose)
        verbose_name_plural = _(pluralize(_language_verbose))

    def clean(self):
        """Perform cross field validation.
        """
        super(Language, self).clean()
        validation.language_validation(self)


_timezone_type = "TimezoneType"
_timezone_type_verbose = humanize(underscore(_timezone_type))


class TimezoneType(NamedModel):
    """Timezone type model class.

    Allow timezone classification.
    Values may include "unknown".
    """
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _timezone_type)
        verbose_name = _(_timezone_type_verbose)
        verbose_name_plural = _(pluralize(_timezone_type_verbose))

_timezone = "Timezone"
_timezone_verbose = humanize(underscore(_timezone))


class Timezone(OptionalNamedModel):
    """
    Time zone model class.

    Captures time zone attributes.
    """
    # @TODO: Add foreign key to TimezoneType?
    timezone = fields.timezone_field()

    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _timezone)
        verbose_name = _(_timezone_verbose)
        verbose_name_plural = _(pluralize(_timezone_verbose))

    def __str__(self):
        return '{0}'.format(self.timezone)


class Region(NamedModel):
    """Abstract class for state, province, county model.

    Uses 3 characters as per ISO 3166.
    """
    # two char country code, "-", three char region code
    iso_code = fields.char_field(max_length=6, unique=True)
    country = fields.foreign_key_field(Country)

    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        abstract = True
        app_label = _app_label


_province = "Province"
_province_verbose = humanize(underscore(_province))


class Province(Region):
    """Province model class.

    Also used for countries  where county is an administration unit."""
    class Meta(Region.Meta):
        """Model meta class declaration."""
        db_table = db_table(_app_label, _province)
        verbose_name = _(_province_verbose)
        verbose_name_plural = _(pluralize(_province_verbose))

    def clean(self):
        """Perform cross field validation.
        """
        super(Province, self).clean()
        validation.province_validation(self)


_state = "State"
_state_verbose = humanize(underscore(_state))


class State(Region):
    """State model class."""
    class Meta(Region.Meta):
        """Model meta class declaration."""
        db_table = db_table(_app_label, _state)
        verbose_name = _(_state_verbose)
        verbose_name_plural = _(pluralize(_state_verbose))

    def clean(self):
        """Perform cross field validation.
        """
        super(State, self).clean()
        validation.state_validation(self)

_city = "City"
_city_verbose = humanize(underscore(_city))


class City(NamedModel):
    """City model class.

    In this context, city is 'stand alone' and not embedded within address.
    """
    state = fields.foreign_key_field(State, blank=True, null=True)
    province = fields.foreign_key_field(Province, blank=True, null=True)

    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _city)
        verbose_name = _(_city_verbose)
        verbose_name_plural = _(pluralize(_city_verbose))

    def clean(self):
        """Perform cross field validation.
        """
        super(City, self).clean()
        validation.state_and_province_validation(self.state, self.province)

    @property
    def region(self):
        """Return region."""
        return self.state if self.state else self.province

    def save(self, *args, **kwargs):
        """Save an instance.
        """
        super(City, self).save(*args, **kwargs)

_address_type = "AddressType"
_address_type_verbose = humanize(underscore(_address_type))


class AddressType(NamedModel):
    """Contract address type model class.

    Allow the categorization of contact address.
    Sample values may include 'unknown'.
    """
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _address_type)
        verbose_name = _(_address_type_verbose)
        verbose_name_plural = _(pluralize(_address_type_verbose))

POSTAL_CODE_LENGTH = 10
STREET_ADDRESS_LENGTH = 255
EXTENDED_ADDRESS_LENGTH = 255
CITY_LENGTH = 255

_address = "Address"
_address_verbose = humanize(underscore(_address))


class Address(VersionedModel):
    """Contact address model class.

    Capture the attributes of contact address(s).
    A contact may be associated with 0 or more addresses as follows:
    Contact(1)  -------> ContactAddress(0..*)
    """
    # Labe:l allows to override  name specified in contact
    label = fields.char_field(null=True, blank=True)
    post_office_box = fields.char_field(max_length=32, null=True, blank=True)

    # street_address/address line 1: e.g.75 Carol St.
    street_address = fields.char_field(max_length=STREET_ADDRESS_LENGTH,
                                       null=True, blank=True)

    # extended_address/address line 2: e.g., apartment or suite number
    extended_address = fields.char_field(max_length=EXTENDED_ADDRESS_LENGTH,
                                         null=True, blank=True)
    # locality: (e.g., city)
    # note that it is not a foreign key to City - this needs to be revisited
    city = fields.char_field(max_length=CITY_LENGTH)
    # region:  (e.g., state or province)
    state = fields.foreign_key_field(State, blank=True, null=True)
    province = fields.foreign_key_field(Province, blank=True, null=True)

    country = fields.foreign_key_field(Country, blank=False)
    postal_code = fields.char_field(max_length=POSTAL_CODE_LENGTH)

    # time_zone: allow the capture of time zone per address
    timezone = fields.foreign_key_field(Timezone, blank=True, null=True)

    # geographic_location: allow the capture of geo location per address
    geographic_location = fields.foreign_key_field(GeographicLocation,
                                                   blank=True, null=True)

    # @TODO: Add foreign key to AddressType?
    class Meta(VersionedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _address)
        unique_together = ('street_address', 'city', 'postal_code',
                           'country', 'state', 'province',
                           'extended_address', 'post_office_box')
        verbose_name = _(_address_verbose)
        verbose_name_plural = _(pluralize(_address_verbose))

    @property
    def region(self):
        """Return region."""
        return (self.state
                if self.state else self.province)

    @property
    def street_or_post_office_box(self):
        """Return region."""
        return (self.street_address
                if self.street_address else self.post_office_box)

    def __str__(self):
        return '{0} {1} {2} {3} {4}'.format(
            self.street_or_post_office_box,
            self.city,
            self.region.display_name,
            self.postal_code,
            self.country.display_name)

    def clean(self):
        """Perform cross field validation.
        """
        super(Address, self).clean()
        validation.street_and_post_office_box_validation(self.post_office_box,
                                                         self.street_address)
        validation.post_office_box_validation(self.country,
                                              self.post_office_box)
        validation.state_and_province_validation(self.state, self.province)
        validation.country_state_province_validation(
            self.country, self.state, self.province)
        validation.postal_code_validation(self.country, self.postal_code)
