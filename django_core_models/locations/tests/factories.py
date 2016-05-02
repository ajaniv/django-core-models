"""
.. module::  location.tests.factories
   :synopsis: location application factories module.

*location* application factories module.
"""
from __future__ import absolute_import

import decimal

import factory

from django_core_models_libs.factory_utils import ISOMixin
from django_core_utils.tests.factories import (NamedModelFactory,
                                               VersionedModelFactory)

from .. import models


class AddressTypeModelFactory(NamedModelFactory):
    """Address type model factory class.
    """
    name = "Home"

    class Meta(object):
        """Model meta class."""
        model = models.AddressType


class CountryMixin(ISOMixin):
    """Country mixin class"""
    COUNTRY_USA = "United States of America"
    COUNTRY_FRANCE = "French Republic"
    ISO_3166_2_FR = "FR"
    ISO_3166_2_USA = "US"
    names = (COUNTRY_USA, COUNTRY_FRANCE)
    iso_codes = (ISO_3166_2_USA, ISO_3166_2_FR)


class CountryModelFactory(CountryMixin, NamedModelFactory):
    """Country model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = models.Country
        django_get_or_create = ('name', 'iso_code')

    name = factory.Sequence(lambda n: CountryMixin.name(n))
    iso_code = factory.Sequence(lambda n: CountryMixin.iso_code(n))

country_france_sub_factory = factory.SubFactory(
    CountryModelFactory,
    iso_code=CountryModelFactory.ISO_3166_2_FR,
    name=CountryModelFactory.COUNTRY_FRANCE)

country_usa_sub_factory = factory.SubFactory(
    CountryModelFactory,
    iso_code=CountryModelFactory.ISO_3166_2_USA,
    name=CountryModelFactory.COUNTRY_USA)


def country_usa():
    """Return instance of country USA."""
    return CountryModelFactory(
        name=CountryModelFactory.COUNTRY_USA,
        iso_code=CountryModelFactory.ISO_3166_2_USA)


def country_france():
    """Return instance of country France."""
    return CountryModelFactory(
        name=CountryModelFactory.COUNTRY_FRANCE,
        iso_code=CountryModelFactory.ISO_3166_2_FR)


class DistanceUnitModelFactory(NamedModelFactory):
    """Distance unit model factory class.
    """
    name = "meter"

    class Meta(object):
        """Model meta class."""
        model = models.DistanceUnit


class GeographicLocationTypeModelFactory(NamedModelFactory):
    """Geographic location type model factory class.
    """
    name = "Major city"

    class Meta(object):
        """Model meta class."""
        model = models.GeographicLocationType


class GeographicLocationMixin(object):
    """GeographicLocation mixin class"""
    FUZZY_LATITUDE = decimal.Decimal('89.9999')
    FUZZY_LONGITUDE = decimal.Decimal('179.9999')


class GeographicLocationModelFactory(GeographicLocationMixin,
                                     NamedModelFactory):
    """Geographic location model factory class.
    """
    latitude = GeographicLocationMixin.FUZZY_LATITUDE
    longitude = GeographicLocationMixin.FUZZY_LONGITUDE
    name = "London"

    class Meta(object):
        """Model meta class."""
        model = models.GeographicLocation


class LanguageTypeModelFactory(NamedModelFactory):
    """Language type model factory class.
    """
    name = "Work"

    class Meta(object):
        """Model meta class."""
        model = models.LanguageType


class LanguageMixin(ISOMixin):
    """Language mixin class."""
    ISO_639_2_FR = "fr"
    ISO_639_2_EN = "en"
    LANGUAGE_FRENCH = "French"
    LANGUAGE_ENGLISH = "English"
    names = (LANGUAGE_ENGLISH, LANGUAGE_FRENCH)
    iso_codes = (ISO_639_2_EN, ISO_639_2_FR)


class LanguageModelFactory(LanguageMixin, NamedModelFactory):
    """Language model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = models.Language
        django_get_or_create = ('name', 'iso_code')

    name = factory.Sequence(lambda n: LanguageMixin.name(n))
    iso_code = factory.Sequence(lambda n: LanguageMixin.iso_code(n))


class ProvinceMixin(ISOMixin):
    ISO_3166_2_Normandy = "FR-P"
    ISO_3166_2_CALAIS = "FR-O"

    PROVINCE_LOWER_NORMANDY = "Basse-Normandie"
    PROVINCE_CALAIS = "Nord - Pas-de-Calais"

    names = (PROVINCE_LOWER_NORMANDY, PROVINCE_CALAIS)
    iso_codes = (ISO_3166_2_Normandy, ISO_3166_2_CALAIS)


class ProvinceModelFactory(ProvinceMixin, NamedModelFactory):
    """Province model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = models.Province
        django_get_or_create = ('name', 'iso_code')

    country = country_france_sub_factory
    name = factory.Sequence(lambda n: ProvinceMixin.name(n))
    iso_code = factory.Sequence(lambda n: ProvinceMixin.iso_code(n))

province_normandy_sub_factory = factory.SubFactory(
    ProvinceModelFactory,
    name=ProvinceModelFactory.PROVINCE_LOWER_NORMANDY,
    iso_code=ProvinceModelFactory.ISO_3166_2_Normandy,
    country=country_france_sub_factory)


class StateMixin(ISOMixin):
    """State mixin class."""
    ISO_3166_2_ALABAMA = "US-AL"
    ISO_3166_2_NEW_JERSEY = "US-NJ"
    STATE_ALABAMA = "Alabama"
    STATE_NEW_JERSEY = "New Jersey"
    names = (STATE_ALABAMA, STATE_NEW_JERSEY)
    iso_codes = (ISO_3166_2_ALABAMA, ISO_3166_2_NEW_JERSEY)


class StateModelFactory(StateMixin, NamedModelFactory):
    """State model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = models.State
        django_get_or_create = ('name', 'iso_code')

    country = country_usa_sub_factory
    name = factory.Sequence(lambda n: StateMixin.name(n))
    iso_code = factory.Sequence(lambda n: StateMixin.iso_code(n))

state_alabama_sub_factory = factory.SubFactory(
    StateModelFactory,
    name=StateModelFactory.STATE_ALABAMA,
    iso_code=StateModelFactory.ISO_3166_2_ALABAMA,
    country=country_usa_sub_factory)


class TimezoneTypeModelFactory(NamedModelFactory):
    """Timezone type model factory class.
    """
    name = "Timezone type"

    class Meta(object):
        """Model meta class."""
        model = models.TimezoneType


class Timezone(object):
    """Timezone mixin class"""
    TIMEZONE_AMSTERDAM = 'Europe/Amsterdam'


class TimezoneModelFactory(Timezone, NamedModelFactory):
    """Timezone model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = models.Timezone


class FranceCityMixin(ISOMixin):
    """French city mixin class."""

    CITY_FRANCE_PARIS = "Paris"
    CITY_FRANCE_LILLE = "LILLE"
    names = (CITY_FRANCE_PARIS, CITY_FRANCE_LILLE)


class FrenchCityModelFactory(FranceCityMixin, NamedModelFactory):
    """French city model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = models.City

    name = factory.Sequence(lambda n: FranceCityMixin.name(n))
    province = factory.SubFactory(
        ProvinceModelFactory,
        name=ProvinceModelFactory.PROVINCE_LOWER_NORMANDY,
        iso_code=ProvinceModelFactory.ISO_3166_2_Normandy,
        country=country_france_sub_factory)


class USCityMixin(ISOMixin):
    """US city mixin class."""
    CITY_US_ALABAMA = "Mobile"
    CITY_US_NEW_YORK = "New York"
    names = (CITY_US_ALABAMA, CITY_US_NEW_YORK)


class USCityModelFactory(USCityMixin, NamedModelFactory):
    """US city model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = models.City

    name = factory.Sequence(lambda n: USCityMixin.name(n))
    state = state_alabama_sub_factory


class USAddressMixin(object):
    CITY_ALABAMA = "Mobile"
    POSTAL_CODE_ALABAMA = "36601"
    STREET_ADDRES_ALABAMA = "224 Mountain Ave"
    POST_OFFICE_BOX_ALABAMA = "P.O. Box 786"


class USAddressModelFactory(USAddressMixin, VersionedModelFactory):
    """US Address  model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = models.Address

    city = USCityModelFactory.CITY_US_ALABAMA
    country = country_usa_sub_factory
    postal_code = USAddressMixin.POSTAL_CODE_ALABAMA
    street_address = USAddressMixin.STREET_ADDRES_ALABAMA
    state = state_alabama_sub_factory


class FrenchAddressMixin(object):
    """French address mixin class."""
    POST_OFFICE_BOX_FRANCE = "P.O. Box 786"
    POSTAL_CODE_FRANCE = "75016"
    STREET_ADDRES_FRANCE = "51 Avenue Bugeud"


class FrenchAddressModelFactory(FrenchAddressMixin, VersionedModelFactory):
    """French Address  model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = models.Address
    city = FrenchCityModelFactory.CITY_FRANCE_PARIS
    country = country_france_sub_factory
    postal_code = FrenchAddressMixin.POSTAL_CODE_FRANCE
    province = province_normandy_sub_factory
    street_address = FrenchAddressMixin.STREET_ADDRES_FRANCE
