"""
.. module::  location.tests.test_models
   :synopsis: location application models unit test module.

*location* application models unit test module.
"""
from __future__ import print_function

from django.core.exceptions import ValidationError
from pytz import timezone

from django_core_utils.tests.test_util import (NamedModelTestCase,
                                               VersionedModelTestCase)

from .factories import (AddressTypeModelFactory, CountryModelFactory,
                        FrenchAddressModelFactory, FrenchCityModelFactory,
                        GeographicLocationModelFactory,
                        GeographicLocationTypeModelFactory,
                        LanguageModelFactory, LanguageTypeModelFactory,
                        ProvinceModelFactory, StateModelFactory,
                        TimezoneModelFactory, TimezoneTypeModelFactory,
                        USAddressModelFactory, USCityModelFactory,
                        country_france, country_usa)


class AddressTypeTestCase(NamedModelTestCase):
    """Address type model unit test class.
    """
    def test_address_type_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=AddressTypeModelFactory,
            get_by_name="name_1")


class CountryTestCase(NamedModelTestCase):
    """Country model unit test class.
    """

    def test_country_crud(self):
        countries = [CountryModelFactory(name=name, iso_code=iso_code)
                     for name, iso_code in zip(CountryModelFactory.names,
                                               CountryModelFactory.iso_codes)]
        self.verify_named_instances_crud(
            countries,
            factory_class=CountryModelFactory,
            get_by_name=CountryModelFactory.COUNTRY_USA)

    def test_country_fields(self):
        instance = CountryModelFactory(
            name=CountryModelFactory.COUNTRY_FRANCE,
            iso_code=CountryModelFactory.ISO_3166_2_FR)

        self.verify_instance(instance)
        instance.full_clean()
        self.assertEqual(instance.iso_code,
                         CountryModelFactory.ISO_3166_2_FR,
                         "country initialization error")


class FrenchCityTestCase(NamedModelTestCase):
    """French city model unit test class.
    """
    def test_frency_city_crud(self):
        self.verify_named_model_crud(
            names=FrenchCityModelFactory.names,
            factory_class=FrenchCityModelFactory,
            get_by_name=FrenchCityModelFactory.CITY_FRANCE_PARIS)


class GeographicLocationTypeTestCase(NamedModelTestCase):
    """Geographic location type model unit test class.
    """
    def test_geographic_location_type_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=GeographicLocationTypeModelFactory,
            get_by_name="name_1")


class GeographicLocationTestCase(NamedModelTestCase):
    """Geographic location model unit test class.
    """
    def test_geographic_location_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=GeographicLocationModelFactory,
            get_by_name="name_1")

    def test_geographic_location_fields(self):
        latitude = GeographicLocationModelFactory.FUZZY_LATITUDE
        longitude = GeographicLocationModelFactory.FUZZY_LONGITUDE
        instance = GeographicLocationModelFactory(
            latitude=latitude,
            longitude=longitude)
        self.assertAlmostEquals(instance.latitude, latitude)
        self.assertAlmostEquals(instance.longitude, longitude)


class LanguageTypeTestCase(NamedModelTestCase):
    """Language type  model unit test class.
    """
    def test_Language_type_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=LanguageTypeModelFactory,
            get_by_name="name_1")


class LanguageTestCase(NamedModelTestCase):
    """Language model unit test class.
    """
    def test_language_crud(self):
        languages = [LanguageModelFactory(name=name, iso_code=iso_code)
                     for name, iso_code in zip(LanguageModelFactory.names,
                                               LanguageModelFactory.iso_codes)]
        self.verify_named_instances_crud(
            languages,
            factory_class=LanguageModelFactory,
            get_by_name=LanguageModelFactory.LANGUAGE_ENGLISH)

    def test_language_fields(self):
        instance = LanguageModelFactory(
            name=LanguageModelFactory.LANGUAGE_FRENCH,
            iso_code=LanguageModelFactory.ISO_639_2_FR)
        self.verify_instance(instance)
        self.assertEqual(instance.iso_code,
                         LanguageModelFactory.ISO_639_2_FR,
                         "language initialization error")


class ProvinceTestCase(NamedModelTestCase):
    """Province model unit test class.
    """
    def test_province_crud(self):
        provinces = [ProvinceModelFactory(name=name, iso_code=iso_code)
                     for name, iso_code in zip(ProvinceModelFactory.names,
                                               ProvinceModelFactory.iso_codes)]
        self.verify_named_instances_crud(
            provinces,
            factory_class=ProvinceModelFactory,
            get_by_name=ProvinceModelFactory.PROVINCE_LOWER_NORMANDY)
        ProvinceModelFactory

    def test_state_fields(self):
        instance = ProvinceModelFactory(
            name=ProvinceModelFactory.PROVINCE_LOWER_NORMANDY,
            country=country_france,
            iso_code=ProvinceModelFactory.ISO_3166_2_Normandy)
        self.verify_instance(instance)
        self.assertEqual(instance.iso_code,
                         ProvinceModelFactory.ISO_3166_2_Normandy,
                         "province iso initialization error")
        self.assertEqual(instance.country.iso_code,
                         CountryModelFactory.ISO_3166_2_FR,
                         "state country initialization error")


class StateTestCase(NamedModelTestCase):
    """State model unit test class.
    """
    def test_state_crud(self):
        states = [StateModelFactory(name=name, iso_code=iso_code)
                  for name, iso_code in zip(StateModelFactory.names,
                                            StateModelFactory.iso_codes)]
        self.verify_named_instances_crud(
            states,
            factory_class=StateModelFactory,
            get_by_name=StateModelFactory.STATE_ALABAMA)

    def test_state_fields(self):
        instance = StateModelFactory(
            name=StateModelFactory.STATE_ALABAMA,
            country=country_usa,
            iso_code=StateModelFactory.ISO_3166_2_ALABAMA)
        self.verify_instance(instance)
        self.assertEqual(instance.iso_code,
                         StateModelFactory.ISO_3166_2_ALABAMA,
                         "state iso initialization error")
        self.assertEqual(instance.country.iso_code,
                         CountryModelFactory.ISO_3166_2_USA,
                         "state country initialization error")


class TimezoneTypeTestCase(NamedModelTestCase):
    """Timezone type  model unit test class.
    """
    def test_timezone_type_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=TimezoneTypeModelFactory,
            get_by_name="name_1")


class TimezoneTestCase(NamedModelTestCase):
    """Timezone  model unit test class.
    """
    def test_timezone_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=TimezoneModelFactory,
            get_by_name="name_1")

    def test_timezone_fields(self):
        zone_name = TimezoneModelFactory.TIMEZONE_AMSTERDAM
        instance = TimezoneModelFactory(
            name=zone_name, timezone=timezone(zone_name))
        self.verify_instance(instance)
        self.assertEqual(instance.timezone.zone,
                         zone_name,
                         "time zone initialization error")


class USACityTestCase(NamedModelTestCase):
    """US city model unit test class.
    """
    def test_us_city_crud(self):
        self.verify_named_model_crud(
            names=USCityModelFactory.names,
            factory_class=USCityModelFactory,
            get_by_name=USCityModelFactory.CITY_US_ALABAMA)


class USAddressTestCase(VersionedModelTestCase):
    """US Address model unit test class.
    """
    def test_address_crud(self):
        self.verify_versioned_model_crud(
            factory_class=USAddressModelFactory)

    def test_post_office_box_field(self):
        instance = USAddressModelFactory(
            street_address=None,
            post_office_box=USAddressModelFactory.POST_OFFICE_BOX_ALABAMA)
        self.verify_instance(instance)
        self.assertEqual(instance.post_office_box,
                         USAddressModelFactory.POST_OFFICE_BOX_ALABAMA,
                         "address.post office box initialization error")

    def test_timezone_field(self):
        instance = USAddressModelFactory(timezone=TimezoneModelFactory())
        self.verify_instance(instance)

    def test_geographic_location_field(self):
        instance = USAddressModelFactory(
            geographic_location=GeographicLocationModelFactory())
        self.verify_instance(instance)

    def test_post_office_box_and_street_address_field(self):
        with self.assertRaises(ValidationError):
            instance = USAddressModelFactory(
                post_office_box=USAddressModelFactory.POST_OFFICE_BOX_ALABAMA)
            instance.full_clean()

    def test_country_usa_no_state(self):
        with self.assertRaises(ValidationError):
            instance = USAddressModelFactory(state=None)
            instance.full_clean()

    def test_str(self):
        expected = "{} {} {} {} {}".format(
            USAddressModelFactory.STREET_ADDRES_ALABAMA,
            USCityModelFactory.CITY_US_ALABAMA,
            StateModelFactory.STATE_ALABAMA,
            USAddressModelFactory.POSTAL_CODE_ALABAMA,
            CountryModelFactory.COUNTRY_USA)
        instance = USAddressModelFactory()
        text = str(instance)
        self.assertTrue(text.endswith(expected))


class FrenchAdressTestCase(VersionedModelTestCase):
    """French address model unit test class.
    """
    def test_address_crud(self):
        self.verify_versioned_model_crud(
            factory_class=FrenchAddressModelFactory)

    def test_post_office_box_field(self):
        instance = FrenchAddressModelFactory(
            street_address=None,
            post_office_box=FrenchAddressModelFactory.POST_OFFICE_BOX_FRANCE)
        self.verify_instance(instance)
        self.assertEqual(instance.post_office_box,
                         FrenchAddressModelFactory.POST_OFFICE_BOX_FRANCE,
                         "address.post office box initialization error")

    def test_timezone_field(self):
        instance = FrenchAddressModelFactory(timezone=TimezoneModelFactory())
        self.verify_instance(instance)

    def test_geographic_location_field(self):
        instance = FrenchAddressModelFactory(
            geographic_location=GeographicLocationModelFactory())
        self.verify_instance(instance)

    def test_post_office_box_and_street_address_field(self):
        factory_class = FrenchAddressModelFactory
        with self.assertRaises(ValidationError):
            instance = FrenchAddressModelFactory(
                post_office_box=factory_class.POST_OFFICE_BOX_FRANCE)
            instance.full_clean()

    def test_country_no_province(self):
        with self.assertRaises(ValidationError):
            instance = FrenchAddressModelFactory(province=None)
            instance.full_clean()
