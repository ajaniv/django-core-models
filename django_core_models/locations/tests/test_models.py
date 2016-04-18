"""
.. module::  location.tests.test_models
   :synopsis: location application models unit test module.

*location* application models unit test module.
"""
from __future__ import print_function

import factory.fuzzy
from pytz import timezone

from django_core_utils.tests.factories import (NamedModelFactory,
                                               VersionedModelFactory)
from django_core_utils.tests.test_util import (NamedModelTestCase,
                                               VersionedModelTestCase)

from ..models import (Address, AddressType, Country, GeographicLocation,
                      GeographicLocationType, Language, LanguageType, Province,
                      State, Timezone, TimezoneType)


class GeographicLocationTypeModelFactory(NamedModelFactory):
    """Geographic location type model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = GeographicLocationType


class GeographicLocationTypeTestCase(NamedModelTestCase):
    """Geographic location type model unit test class.
    """
    def test_geographic_location_type_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=GeographicLocationTypeModelFactory,
            get_by_name="name_1")

FUZZY_LATITUDE = 89.99
FUZZY_LONGITUDE = 179.99


class GeographicLocationModelFactory(NamedModelFactory):
    """Geographic location model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = GeographicLocation

    latitude = factory.fuzzy.FuzzyFloat(-FUZZY_LATITUDE, FUZZY_LATITUDE)
    longitude = factory.fuzzy.FuzzyFloat(-FUZZY_LONGITUDE, FUZZY_LONGITUDE)

LATITUDE = 10.0
LONGITUDE = -10.00


class GeographicLocationTestCase(NamedModelTestCase):
    """Geographic location model unit test class.
    """
    def test_geographic_location_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=TimezoneModelFactory,
            get_by_name="name_1")

    def test_geographic_location_fields(self):
        instance = GeographicLocationModelFactory(
            latitude=LATITUDE, longitude=LONGITUDE)
        self.assertAlmostEquals(instance.latitude, LATITUDE)
        self.assertAlmostEquals(instance.longitude, LONGITUDE)


class TimezoneTypeModelFactory(NamedModelFactory):
    """Timezone type model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = TimezoneType


class TimezoneTypeTestCase(NamedModelTestCase):
    """Timezone type  model unit test class.
    """
    def test_timezone_type_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=TimezoneTypeModelFactory,
            get_by_name="name_1")

ZONE_NAME = 'Europe/Amsterdam'


class TimezoneModelFactory(NamedModelFactory):
    """Timezone model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = Timezone

TIME_ZONE = "America/New_York"


class TimezoneTestCase(NamedModelTestCase):
    """Timezone  model unit test class.
    """
    def test_timezone_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=TimezoneModelFactory,
            get_by_name="name_1")

    def test_timezone_fields(self):
        instance = TimezoneModelFactory(name=ZONE_NAME,
                                        timezone=timezone(ZONE_NAME))
        self.verify_instance(instance)
        self.assertEqual(instance.timezone.zone,
                         ZONE_NAME,
                         "time zone initialization error")


class LanguageTypeModelFactory(NamedModelFactory):
    """Language type model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = LanguageType


class LanguageTypeTestCase(NamedModelTestCase):
    """Language type  model unit test class.
    """
    def test_Language_type_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=LanguageTypeModelFactory,
            get_by_name="name_1")

ISO_639_2_FR = "fr"


class LanguageModelFactory(NamedModelFactory):
    """Language model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = Language


class LanguageTestCase(NamedModelTestCase):
    """Language model unit test class.
    """
    def test_language_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=LanguageModelFactory,
            get_by_name="name_1")

    def test_language_fields(self):
        instance = LanguageModelFactory(iso_code=ISO_639_2_FR)
        self.verify_instance(instance)
        self.assertEqual(instance.iso_code,
                         ISO_639_2_FR,
                         "language initialization error")

COUNTRY_US = "United States of America"
COUNTRY_FRANCE = "France"
ISO_3166_2_FR = "FR"
ISO_3166_2_US = "US"


class CountryModelFactory(NamedModelFactory):
    """Country model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = Country

    name = COUNTRY_US
    iso_code = ISO_3166_2_US


class CountryTestCase(NamedModelTestCase):
    """Country model unit test class.
    """
    def test_country_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=CountryModelFactory,
            get_by_name="name_1")

    def test_language_fields(self):
        instance = CountryModelFactory(name=COUNTRY_FRANCE,
                                       iso_code=ISO_3166_2_FR)
        self.verify_instance(instance)
        self.assertEqual(instance.iso_code,
                         ISO_3166_2_FR,
                         "country initialization error")

ISO_3166_2_ALABAMA = "US-AL"
STATE_ALABAMA = "Alabama"


class StateModelFactory(NamedModelFactory):
    """State model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = State

    country = factory.SubFactory(CountryModelFactory)
    name = STATE_ALABAMA
    iso_code = ISO_3166_2_ALABAMA


class StateTestCase(NamedModelTestCase):
    """Region model unit test class.
    """
    def test_state_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=StateModelFactory,
            get_by_name="name_1")

    def test_state_fields(self):
        instance = StateModelFactory(
            name=STATE_ALABAMA,
            country=CountryModelFactory(),
            iso_code=ISO_3166_2_ALABAMA)
        self.verify_instance(instance)
        self.assertEqual(instance.iso_code,
                         ISO_3166_2_ALABAMA,
                         "state iso initialization error")
        self.assertEqual(instance.country.iso_code,
                         ISO_3166_2_US,
                         "state country initialization error")

ISO_3166_2_Normandy = "FR-P"
ISO_3166_2_ALABAMA = "AL"
PROVINCE_LOWER_NORMANDY = "Lower Normandy"


class ProvinceModelFactory(NamedModelFactory):
    """Province model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = Province

    country = factory.SubFactory(CountryModelFactory)


class ProvinceTestCase(NamedModelTestCase):
    """Province model unit test class.
    """
    def test_province_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=ProvinceModelFactory,
            get_by_name="name_1")

    def test_state_fields(self):
        instance = ProvinceModelFactory(
            name=PROVINCE_LOWER_NORMANDY,
            country=CountryModelFactory(name="France", iso_code=ISO_3166_2_FR),
            iso_code=ISO_3166_2_Normandy)
        self.verify_instance(instance)
        self.assertEqual(instance.iso_code,
                         ISO_3166_2_Normandy,
                         "province iso initialization error")
        self.assertEqual(instance.country.iso_code,
                         ISO_3166_2_FR,
                         "state country initialization error")


class AddressTypeModelFactory(NamedModelFactory):
    """Address type model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = AddressType


class AddressTypeTestCase(NamedModelTestCase):
    """Address type model unit test class.
    """
    def test_address_type_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=AddressTypeModelFactory,
            get_by_name="name_1")

CITY_ALABAMA = "Mobile"
POSTAL_CODE_ALABAMA = "36601"
STREET_ADDRES_ALABAMA = "224 Mountain Ave"
POST_OFFICE_BOX_ALABAMA = "P.O. Box 786"


class USAddressModelFactory(VersionedModelFactory):
    """US Address  model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = Address

    street_address = STREET_ADDRES_ALABAMA
    city = CITY_ALABAMA
    state = factory.SubFactory(StateModelFactory)
    country = factory.SubFactory(CountryModelFactory)
    postal_code = POSTAL_CODE_ALABAMA


class USAddressTestCase(VersionedModelTestCase):
    """US Address model unit test class.
    """
    def test_address_crud(self):
        self.verify_versioned_model_crud(
            factory_class=USAddressModelFactory)

    def test_post_office_box_field(self):
        instance = USAddressModelFactory(
            street_address=None,
            post_office_box=POST_OFFICE_BOX_ALABAMA)
        self.verify_instance(instance)
        self.assertEqual(instance.post_office_box, POST_OFFICE_BOX_ALABAMA,
                         "address.post office box initialization error")

    def test_timezone_field(self):
        instance = USAddressModelFactory(timezone=TimezoneModelFactory())
        self.verify_instance(instance)

    def test_geographic_location_field(self):
        instance = USAddressModelFactory(
            geographic_location=GeographicLocationModelFactory())
        self.verify_instance(instance)

    def test_post_office_box_and_street_address_field(self):
        with self.assertRaises(ValueError):
            USAddressModelFactory(post_office_box=POST_OFFICE_BOX_ALABAMA)

    def test_country_usa_no_state(self):
        with self.assertRaises(ValueError):
            USAddressModelFactory(state=None)

    def test_str(self):
        expected = "{} {} {} {} {}".format(
            STREET_ADDRES_ALABAMA, CITY_ALABAMA,
            STATE_ALABAMA, POSTAL_CODE_ALABAMA,
            COUNTRY_US)
        instance = USAddressModelFactory(
            geographic_location=GeographicLocationModelFactory())
        text = str(instance)
        self.assertTrue(text.endswith(expected))

CITY_FRANCE = "Paris"
POSTAL_CODE_FRANCE = "75016"
STREET_ADDRES_FRANCE = "51 Avenue Bugeud"
POST_OFFICE_BOX_FRANCE = "P.O. Box 786"

_france = factory.SubFactory(
    CountryModelFactory, iso_code=ISO_3166_2_FR, name=COUNTRY_FRANCE)


class FrenchAddressModelFactory(VersionedModelFactory):
    """French Address  model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = Address

    country = _france
    province = factory.SubFactory(
        ProvinceModelFactory,
        name=PROVINCE_LOWER_NORMANDY,
        iso_code=ISO_3166_2_Normandy,
        country=_france)
    country = _france
    street_address = STREET_ADDRES_FRANCE
    city = CITY_FRANCE
    postal_code = POSTAL_CODE_FRANCE


class FrenchAdressTestCase(VersionedModelTestCase):
    """French address model unit test class.
    """
    def test_address_crud(self):
        self.verify_versioned_model_crud(
            factory_class=FrenchAddressModelFactory)

    def test_post_office_box_field(self):
        instance = FrenchAddressModelFactory(
            street_address=None,
            post_office_box=POST_OFFICE_BOX_FRANCE)
        self.verify_instance(instance)
        self.assertEqual(instance.post_office_box, POST_OFFICE_BOX_FRANCE,
                         "address.post office box initialization error")

    def test_timezone_field(self):
        instance = FrenchAddressModelFactory(timezone=TimezoneModelFactory())
        self.verify_instance(instance)

    def test_geographic_location_field(self):
        instance = FrenchAddressModelFactory(
            geographic_location=GeographicLocationModelFactory())
        self.verify_instance(instance)

    def test_post_office_box_and_street_address_field(self):
        with self.assertRaises(ValueError):
            FrenchAddressModelFactory(post_office_box=POST_OFFICE_BOX_FRANCE)

    def test_country_no_province(self):
        with self.assertRaises(ValueError):
            FrenchAddressModelFactory(province=None)
