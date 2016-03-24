"""
.. module::  core_models.location
   :synopsis:  core_models location models module

core_modelslocation models module.

"""

from core.models import app_table_name, db_table_name
from core import fields
from core.models import NamedModel, VersionedModel

from .apps import CoreModelsConfig

_app_label = CoreModelsConfig.name

__all__ = [
    'GeographicLocationType',
    'GeographicLocation',
    'TimezoneType',
    'Timezone',
    'LanguageType',
    'Language',
    'Country',
    'Region',
    'State',
    'Province',
    'AddressType',
    'Address'
    ]


class GeographicLocationType(NamedModel):
    """GeographicLocation type model class.

    Allow GeographicLocation classification.
    Values may include "unknown".
    """
    class Meta(NamedModel.Meta):
        app_label = _app_label
        db_table = app_table_name(_app_label,
                                  db_table_name("GeographicLocationType"))


class GeographicLocation(VersionedModel):
    """Geographic location model class.

    Captures geographic location data.
    """
    class Meta(VersionedModel.Meta):
        app_label = _app_label
        db_table = app_table_name(_app_label,
                                  db_table_name("GeographicLocation"))
    latitude = fields.latitude_field()
    longitude = fields.longitude_field()


class TimezoneType(NamedModel):
    """Timezone type model class.

    Allow timezone classification.
    Values may include "unknown".
    """
    class Meta(NamedModel.Meta):
        app_label = _app_label
        db_table = app_table_name(_app_label,
                                  db_table_name("TimezoneType"))


class Timezone(NamedModel):
    """
    Time zone model class.

    Captures time zone attributes.
    """
    class Meta(NamedModel.Meta):
        app_label = _app_label
        db_table = app_table_name(_app_label, db_table_name("Timezone"))

    time_zone = fields.time_zone_field()


class LanguageType(NamedModel):
    """Language type model class.

    Allow language classification.
    Values may include "unknown".
    """
    class Meta(NamedModel.Meta):
        app_label = _app_label
        db_table = app_table_name(_app_label,
                                  db_table_name("ContactLanguageType"))


class Language(NamedModel):
    """Language model class.

    Uses 2 characters as per ISO 639-1.
    """
    class Meta(NamedModel.Meta):
        app_label = _app_label
        db_table = app_table_name(_app_label, db_table_name("Language"))

    iso_code = fields.char_field(max_length=2)


class Country(NamedModel):
    """Country model class.

    Uses 2 characters as per  ISO 3166.
    """
    class Meta(NamedModel.Meta):
        app_label = _app_label
        db_table = app_table_name(_app_label, db_table_name("Country"))

    iso_code = fields.char_field(max_length=2)


class Region(NamedModel):
    """Abstract class for state and province model.

    Uses 3 characters as per ISO 3166.
    """
    class Meta(NamedModel.Meta):
        abstract = True
        app_label = _app_label

    iso_code = fields.char_field(max_length=3)
    country = fields.foreign_key_field(Country)


class State(Region):
    """State model class."""
    class Meta(Region.Meta):
        db_table = app_table_name(_app_label, db_table_name("State"))


class Province(Region):
    """Province model class."""
    class Meta(Region.Meta.Meta):
        db_table = app_table_name(_app_label, db_table_name("Province"))


class AddressType(NamedModel):
    """Contract address type model class.

    Allow the categorization of contact address.
    Sample values may include 'unknown'.
    """
    class Meta(NamedModel.Meta):
        app_label = _app_label
        db_table = app_table_name(_app_label, db_table_name("AddressType"))

POSTAL_CODE_LENGTH = 10


class Address(VersionedModel):
    """Contact address model class.

    Capture the attributes of contact address(s).
    A contact may be associated with 0 or more addresses as follows:
    Contact(1)  -------> ContactAddress(0..*)
    """
    class Meta(VersionedModel.Meta):
        app_label = _app_label
        db_table = app_table_name(_app_label, db_table_name("Address"))
        unique_together = ('city', 'country', 'postal_code', 'state',
                           'province', 'street_address',
                           'extended_address', 'post_office_box')

    # Labe:l allows to override  name specified in contact
    label = fields.char_field(
                              null=True, blank=True)
    post_office_box = fields.char_field(
                                        null=True, blank=True)

    # street_address/address line 1: e.g.75 Carol St.
    street_address = fields.char_field(
                                       null=True, blank=True)

    # extended_address/address line 2: e.g., apartment or suite number
    extended_address = fields.char_field(
                                         null=True, blank=True)
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

    def __str__(self):
        return "%s, %s %s" % (self.city, self.state_province,
                              str(self.country))
