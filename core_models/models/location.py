"""
.. module::  core_models.location
   :synopsis:  core_models location models module

core_modelslocation models module.

"""
from __future__ import absolute_import

from core_utils import fields
from core_utils.models import NamedModel, VersionedModel, db_table

from ..apps import CoreModelsConfig

_app_label = CoreModelsConfig.name


class GeographicLocationType(NamedModel):
    """GeographicLocation type model class.

    Allow GeographicLocation classification.
    Values may include "unknown".
    """
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, "GeographicLocationType")


class GeographicLocation(VersionedModel):
    """Geographic location model class.

    Captures geographic location data.
    """
    # @TODO: Add foreign key to GeographicLocationType?
    latitude = fields.latitude_field()
    longitude = fields.longitude_field()

    class Meta(VersionedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, "GeographicLocation")


class TimezoneType(NamedModel):
    """Timezone type model class.

    Allow timezone classification.
    Values may include "unknown".
    """
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, "TimezoneType")


class Timezone(NamedModel):
    """
    Time zone model class.

    Captures time zone attributes.
    """
    # @TODO: Add foreign key to TimezoneType?
    timezone = fields.timezone_field()

    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, "Timezone")


class LanguageType(NamedModel):
    """Language type model class.

    Allow language classification.
    Values may include "unknown".
    """
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, "ContactLanguageType")


class Language(NamedModel):
    """Language model class.

    Uses 2 characters as per ISO 639-1.
    """
    # @TODO: Add foreign key to LanguageType?
    iso_code = fields.char_field(max_length=2)

    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, "Language")


class Country(NamedModel):
    """Country model class.

    Uses 2 characters as per  ISO 3166.
    """
    ISO_3166_2_US = "US"
    iso_code = fields.char_field(max_length=2)

    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, "Country")

    def is_usa(self):
        return self.iso_code == self.ISO_3166_2_US


class Region(NamedModel):
    """Abstract class for state and province model.

    Uses 3 characters as per ISO 3166.
    """
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        abstract = True
        app_label = _app_label

    # two char country code, "-", three char region code
    iso_code = fields.char_field(max_length=6)
    country = fields.foreign_key_field(Country)


class State(Region):
    """State model class."""
    class Meta(Region.Meta):
        """Model meta class declaration."""
        db_table = db_table(_app_label, "State")


class Province(Region):
    """Province model class."""
    class Meta(Region.Meta):
        """Model meta class declaration."""
        db_table = db_table(_app_label, "Province")


class AddressType(NamedModel):
    """Contract address type model class.

    Allow the categorization of contact address.
    Sample values may include 'unknown'.
    """
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, "AddressType")

POSTAL_CODE_LENGTH = 10


class Address(VersionedModel):
    """Contact address model class.

    Capture the attributes of contact address(s).
    A contact may be associated with 0 or more addresses as follows:
    Contact(1)  -------> ContactAddress(0..*)
    """
    # @TODO: Add foreign key to AddressType?
    class Meta(VersionedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, "Address")
        unique_together = ('city', 'country', 'postal_code', 'state',
                           'province', 'street_address',
                           'extended_address', 'post_office_box')

    # Labe:l allows to override  name specified in contact
    label = fields.char_field(null=True, blank=True)
    post_office_box = fields.char_field(null=True, blank=True)

    # street_address/address line 1: e.g.75 Carol St.
    street_address = fields.char_field(null=True, blank=True)

    # extended_address/address line 2: e.g., apartment or suite number
    extended_address = fields.char_field(null=True, blank=True)
    # locality: (e.g., city)
    city = fields.char_field()
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
        if self.post_office_box is None and self.street_address is None:
            raise ValueError("post_office_box and street_address are none")
        if self.post_office_box and self.street_address:
            raise ValueError("post_office_box and street_address are set")

    def _validate_state_and_province(self):
        if self.state is None and self.province is None:
            raise ValueError("State and province are none")
        if self.state and self.province:
            raise ValueError("State and province are set")

    def _validate_country(self):
        if self.country is not None:
            if self.country.is_usa():
                if self.state is None:
                    raise ValueError("country is USA state is not set")
            else:
                if self.province is None:
                    raise ValueError("country is not USA  province is not set")

    def save(self, *args, **kwargs):
        """Save an instance.
        """
        self._validate_street_and_post_office_box()
        self._validate_state_and_province()
        self._validate_country()

        super(Address, self).save(*args, **kwargs)
