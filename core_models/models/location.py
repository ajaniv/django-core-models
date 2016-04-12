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
    time_zone = fields.time_zone_field()

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
    iso_code = fields.char_field(max_length=2)

    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, "Language")


class Country(NamedModel):
    """Country model class.

    Uses 2 characters as per  ISO 3166.
    """
    iso_code = fields.char_field(max_length=2)

    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, "Country")


class Region(NamedModel):
    """Abstract class for state and province model.

    Uses 3 characters as per ISO 3166.
    """
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        abstract = True
        app_label = _app_label

    iso_code = fields.char_field(max_length=3)
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
    time_zone = fields.foreign_key_field(Timezone, blank=True, null=True)

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
            self.city.name,
            self.region,
            self.postal_code,
            self.country.name)
