"""
.. module::  location.models
   :synopsis:  location models module

*location* application models module.

"""
from __future__ import absolute_import
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from inflection import humanize, pluralize, underscore

from django_core_utils import fields
from django_core_utils.models import (NamedModel, OptionalNamedModel,
                                      VersionedModel, db_table)

_app_label = "locations"

# @TODO: Should validations move to separate module?
# @TODO: Should error messages be translated


def state_and_province_validation(state, province):
    """Validate state and province.
    """
    if state is None and province is None:
        raise ValidationError("State and province are none.")
    if state and province:
        raise ValidationError("State and province are set.")


def country_validation(country, state, province):
    """Validate country."""
    if country is not None:
        if country.is_usa():
            if state is None:
                raise ValidationError("Country is USA and state is not set.")
            underlying_country = state.country
        else:
            if province is None:
                raise ValidationError(
                    "Country is not USA and province is not set.")
            underlying_country = province.country
        if country != underlying_country:
            raise ValidationError(
                    "State/province country improperly configured.")


def street_and_post_office_box_validation(post_office_box, street_address):
    """Validate street and post office box"""
    if not (post_office_box or street_address):
        raise ValidationError("post_office_box and street_address not set")
    if post_office_box and street_address:
        raise ValidationError("post_office_box and street_address are set")

_country = "Country"
_country_verbose = humanize(underscore(_country))


class Country(NamedModel):
    """Country model class.

    Uses 2 characters as per  ISO 3166.
    """
    ISO_3166_2_US = "US"
    iso_code = fields.char_field(max_length=2)

    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _country)
        verbose_name = _(_country_verbose)
        verbose_name_plural = _(pluralize(_country_verbose))

    def is_usa(self):
        return self.iso_code == self.ISO_3166_2_US


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
    latitude = fields.latitude_field()
    longitude = fields.longitude_field()

    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _geographic_location)
        verbose_name = _(_geographic_location_verbose)
        verbose_name_plural = _(pluralize(_geographic_location_verbose))

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
    iso_code = fields.char_field(max_length=2)

    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _language)
        verbose_name = _(_language_verbose)
        verbose_name_plural = _(pluralize(_language_verbose))


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


class Region(NamedModel):
    """Abstract class for state and province model.

    Uses 3 characters as per ISO 3166.
    """
    # two char country code, "-", three char region code
    iso_code = fields.char_field(max_length=6)
    country = fields.foreign_key_field(Country)

    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        abstract = True
        app_label = _app_label


_province = "Province"
_province_verbose = humanize(underscore(_province))


class Province(Region):
    """Province model class."""
    class Meta(Region.Meta):
        """Model meta class declaration."""
        db_table = db_table(_app_label, _province)
        verbose_name = _(_province_verbose)
        verbose_name_plural = _(pluralize(_province_verbose))


_state = "State"
_state_verbose = humanize(underscore(_state))


class State(Region):
    """State model class."""
    class Meta(Region.Meta):
        """Model meta class declaration."""
        db_table = db_table(_app_label, _state)
        verbose_name = _(_state_verbose)
        verbose_name_plural = _(pluralize(_state_verbose))

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

    def _validate_country(self):
        country_validation(self.country, self.state, self.province)

    def save(self, *args, **kwargs):
        """Save an instance.
        """
        state_and_province_validation(self.state, self.province)

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
        return self.state if self.state else self.province

    @property
    def street_or_post_office_box(self):
        """Return region."""
        return (self.street_address
                if self.street_address else self.post_office_box)

    def __str__(self):
        return '{0} {1} {2} {3} {4} {5}'.format(
            super(Address, self).__str__(),
            self.street_or_post_office_box,
            self.city,
            self.region.name,
            self.postal_code,
            self.country.name)

    def _validate_street_and_post_office_box(self):
        street_and_post_office_box_validation(self.post_office_box,
                                              self.street_address)

    def _validate_state_and_province(self):
        state_and_province_validation(self.state, self.province)

    def _validate_country(self):
        country_validation(self.country, self.state, self.province)

    def full_clean(self, exclude=None, validate_unique=True):
        super(Address, self).full_clean(exclude=None, validate_unique=True)
        self._validate_street_and_post_office_box()
        self._validate_state_and_province()
        self._validate_country()

    def save(self, *args, **kwargs):
        """Save an instance.
        """
        super(Address, self).save(*args, **kwargs)
