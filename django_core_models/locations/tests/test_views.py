"""
.. module::  django_core_models.locations.tests.test_views
   :synopsis: locations models application views unit test module.

*locations models* application views unit test module.
"""
from __future__ import absolute_import, print_function
from django_core_utils.tests.api_test_utils import (NamdedModelApiTestCase,
                                                    VersionedModelApiTestCase)

from django_core_models_libs.test_utils import IsoApiTestCase
from . import factories
from .. import models
from .. import serializers


class AddressTypeApiTestCase(NamdedModelApiTestCase):
    """AddressType API unit test class."""
    factory_class = factories.AddressTypeModelFactory
    model_class = models.AddressType
    serializer_class = serializers.AddressTypeSerializer

    url_detail = "address-type-detail"
    url_list = "address-type-list"

    name = factories.AddressTypeModelFactory.name

    def test_create_address_type(self):
        self.verify_create_defaults()

    def test_create_address_type_partial(self):
        self.verify_create_defaults_partial()

    def test_get_address_type(self):
        self.verify_get_defaults()

    def test_put_address_type_partial(self):
        instance = self.create_instance_default()
        data = dict(id=instance.id, name=self.name)
        self.verify_put(self.url_detail, instance, data, self.serializer_class)

    def test_delete_address_type(self):
        self.verify_delete_default()


class CountryApiTestCase(IsoApiTestCase):
    """Country API unit test class."""
    factory_class = factories.CountryModelFactory
    model_class = models.Country
    serializer_class = serializers.CountrySerializer

    url_list = "country-list"
    url_detail = "country-detail"

    iso_code = factories.CountryMixin.ISO_3166_2_USA
    name = factories.CountryMixin.COUNTRY_USA

    def test_create_country(self):
        self.verify_create_defaults()

    def test_create_country_partial(self):
        self.verify_create_defaults_partial()

    def test_get_country(self):
        self.verify_get_defaults()

    def test_put_country_partial(self):
        instance = self.create_instance_default()
        data = dict(id=instance.id, name=self.name, iso_code=self.iso_code)
        self.verify_put(self.url_detail, instance, data, self.serializer_class)

    def test_delete_country(self):
        self.verify_delete_default()


class DistanceUnitApiTestCase(NamdedModelApiTestCase):
    """DistanceUnit API unit test class."""
    factory_class = factories.DistanceUnitModelFactory
    model_class = models.DistanceUnit
    serializer_class = serializers.DistanceUnitSerializer

    url_detail = "distance-unit-detail"
    url_list = "distance-unit-list"

    name = factories.DistanceUnitModelFactory.name

    def test_create_distance_unit(self):
        self.verify_create_defaults()

    def test_create_distance_unit_partial(self):
        self.verify_create_defaults_partial()

    def test_get_distance_unit(self):
        self.verify_get_defaults()

    def test_put_distance_unit_partial(self):
        instance = self.create_instance_default()
        data = dict(id=instance.id, name=self.name)
        self.verify_put(self.url_detail, instance, data, self.serializer_class)

    def test_delete_distance_unit(self):
        self.verify_delete_default()


class GeographicLocationTypeApiTestCase(NamdedModelApiTestCase):
    """GeographicLocationType API unit test class."""
    factory_class = factories.GeographicLocationTypeModelFactory
    model_class = models.GeographicLocationType
    serializer_class = serializers.GeographicLocationTypeSerializer

    url_detail = "geographic-location-type-detail"
    url_list = "geographic-location-type-list"

    name = factories.GeographicLocationTypeModelFactory.name

    def test_create_geographic_location_type(self):
        self.verify_create_defaults()

    def test_create_geographic_location_type_partial(self):
        self.verify_create_defaults_partial()

    def test_get_geographic_location_type(self):
        self.verify_get_defaults()

    def test_put_geographic_location_type_partial(self):
        instance = self.create_instance_default()
        data = dict(id=instance.id, name=self.name)
        self.verify_put(self.url_detail, instance, data, self.serializer_class)

    def test_delete_geographic_location_type(self):
        self.verify_delete_default()


class GeographicLocationApiTestCase(NamdedModelApiTestCase):
    """GeographicLocation API unit test class."""
    factory_class = factories.GeographicLocationModelFactory
    model_class = models.GeographicLocation
    serializer_class = serializers.GeographicLocationSerializer

    url_detail = "geographic-location-detail"
    url_list = "geographic-location-list"

    name = factories.GeographicLocationModelFactory.name

    def geographic_location_data(self, instance):
        """return geogralphic location data"""
        instance = instance or self.factory_class()
        data = dict(latitude=instance.latitude,
                    longitude=instance.longitude)
        return data

    def post_required_data(self, ref_instance, user=None, site=None):
        """Return named model post request required data."""
        data = super(
            GeographicLocationApiTestCase, self).post_required_data(user, site)
        data.update(self.geographic_location_data(ref_instance))
        return data

    def verify_create_geographic_location(
            self, ref_instance=None, data=None, expected_name=None):
        """Generate post request for geographic location creation."""
        data = data or self.post_required_data(ref_instance)
        response, instance = self.verify_create(
            url=self.url_list,
            data=data,
            model_class=self.model_class,
            expected_name=expected_name)

        if ref_instance:
            self.assert_instance_equal(
                ref_instance, instance,
                ("latitude", "longitude", "range", "range_unit"))

        return response, instance

    def test_create_geographic_location(self):
        instance = self.create_instance_default()
        self.verify_create_geographic_location(
            ref_instance=instance, expected_name=self.name)

    def test_create_geographic_location_partial(self):
        instance = self.create_instance_default()
        data = self.geographic_location_data(instance)
        data["name"] = self.name
        self.verify_create_geographic_location(
            ref_instance=instance,
            data=data,
            expected_name=self.name)

    def test_get_geographic_location(self):
        self.verify_get_defaults()

    def test_put_geographic_location_partial(self):
        instance = self.create_instance_default()
        data = dict(id=instance.id, name=self.name)
        self.verify_put(self.url_detail, instance, data, self.serializer_class)

    def test_delete_geographic_location(self):
        self.verify_delete_default()


class LanguageTypeApiTestCase(NamdedModelApiTestCase):
    """LanaguageType API unit test class."""
    factory_class = factories.LanguageTypeModelFactory
    model_class = models.LanguageType
    serializer_class = serializers.LanguageTypeSerializer

    url_detail = "language-type-detail"
    url_list = "language-type-list"

    name = factories.LanguageTypeModelFactory.name

    def test_create_language_type(self):
        self.verify_create_defaults()

    def test_create_language_type_partial(self):
        self.verify_create_defaults_partial()

    def test_get_language_type(self):
        self.verify_get_defaults()

    def test_put_language_type_partial(self):
        instance = self.create_instance_default()
        data = dict(id=instance.id, name=self.name)
        self.verify_put(self.url_detail, instance, data, self.serializer_class)

    def test_delete_language_type(self):
        self.verify_delete_default()


class LanguageApiTestCase(IsoApiTestCase):
    """Language API unit test class."""
    factory_class = factories.LanguageModelFactory
    model_class = models.Language
    serializer_class = serializers.LanguageSerializer

    url_list = "language-list"
    url_detail = "language-detail"

    iso_code = factories.LanguageMixin.ISO_639_2_EN
    name = factories.LanguageMixin.LANGUAGE_ENGLISH

    def test_create_language(self):
        self.verify_create_defaults()

    def test_create_language_partial(self):
        self.verify_create_defaults_partial()

    def test_get_language(self):
        self.verify_get_defaults()

    def test_put_language_partial(self):
        instance = self.create_instance_default()
        data = dict(id=instance.id, name=self.name, iso_code=self.iso_code)
        self.verify_put(self.url_detail, instance, data, self.serializer_class)

    def test_delete_language(self):
        self.verify_delete_default()


class TimezoneTypeApiTestCase(NamdedModelApiTestCase):
    """TimezoneType API unit test class."""
    factory_class = factories.TimezoneTypeModelFactory
    model_class = models.TimezoneType
    serializer_class = serializers.TimezoneTypeSerializer

    url_detail = "timezone-type-detail"
    url_list = "timezone-type-list"

    name = factories.TimezoneTypeModelFactory.name

    def test_create_timezone_type(self):
        self.verify_create_defaults()

    def test_create_timezone_type_partial(self):
        self.verify_create_defaults_partial()

    def test_get_timezone_type(self):
        self.verify_get_defaults()

    def test_put_timezone_type_partial(self):
        instance = self.create_instance_default()
        data = dict(id=instance.id, name=self.name)
        self.verify_put(self.url_detail, instance, data, self.serializer_class)

    def test_delete_timezone_type(self):
        self.verify_delete_default()


class TimezoneApiTestCase(NamdedModelApiTestCase):
    """Timezone API unit test class."""
    factory_class = factories.TimezoneModelFactory
    model_class = models.Timezone
    serializer_class = serializers.TimezoneSerializer

    url_detail = "timezone-detail"
    url_list = "timezone-list"

    name = "New York"

    def timezone_data(self, instance):
        """return timezone data"""
        instance = instance or self.factory_class()
        data = dict(timezone=str(instance.timezone))
        return data

    def post_required_data(self, ref_instance, user=None, site=None):
        """Return named model post request required data."""
        data = super(
            TimezoneApiTestCase, self).post_required_data(user, site)
        data.update(self.timezone_data(ref_instance))
        return data

    def verify_create_timezone(
            self, ref_instance=None, data=None, expected_name=None):
        """Generate post request for timezone creation."""
        data = data or self.post_required_data(ref_instance)
        response, instance = self.verify_create(
            url=self.url_list,
            data=data,
            model_class=self.model_class,
            expected_name=expected_name)

        if ref_instance:
            self.assert_instance_equal(ref_instance, instance, ("timezone", ))

        return response, instance

    def test_create_timezone(self):
        instance = self.create_instance_default()
        self.verify_create_timezone(
            ref_instance=instance, expected_name=self.name)

    def test_create_timezone_partial(self):
        instance = self.create_instance_default()
        data = self.timezone_data(instance)
        data["name"] = self.name
        self.verify_create_timezone(
            ref_instance=instance,
            data=data,
            expected_name=self.name)

    def test_get_timezone(self):
        self.verify_get_defaults()

    def test_put_timezone_partial(self):
        instance = self.create_instance_default()
        data = dict(id=instance.id, name=self.name)
        self.verify_put(self.url_detail, instance, data, self.serializer_class)

    def test_delete_timezone(self):
        self.verify_delete_default()


class RegionApiTestCase(IsoApiTestCase):
    """Region model api test class."""

    def region_data(self, country):
        """return region data"""
        data = dict(country=country.id)
        return data

    def post_required_data(self, country, user=None, site=None):
        """Return named model post request required data."""
        data = super(
            RegionApiTestCase, self).post_required_data(user, site)
        data.update(self.region_data(country))
        return data

    def verify_create_region(
            self, country, data=None, expected_name=None):
        """Generate post request for region creation."""
        data = data or self.post_required_data(country)
        response, instance = self.verify_create(
            url=self.url_list,
            data=data,
            model_class=self.model_class,
            expected_name=expected_name,
            expected_iso_code=self.iso_code,)

        self.assertEqual(data["country"],
                         instance.country.id)

        return response, instance

    def create_country(self, country=None):
        """
        Return a country instance."""

        name = country or self.country
        if name == factories.CountryModelFactory.COUNTRY_FRANCE:
            return factories.country_france()
        else:
            return factories.country_usa()


class ProvinceApiTestCase(RegionApiTestCase):
    """Province API unit test class."""
    factory_class = factories.ProvinceModelFactory
    model_class = models.Province
    serializer_class = serializers.ProvinceSerializer

    url_detail = "province-detail"
    url_list = "province-list"

    name = factories.ProvinceModelFactory.PROVINCE_CALAIS
    iso_code = factories.ProvinceModelFactory.ISO_3166_2_CALAIS
    country = factories.CountryModelFactory.COUNTRY_FRANCE

    def test_create_province(self):
        country = self.create_country()
        self.verify_create_region(
            country, expected_name=self.name)

    def test_create_province_partial(self):
        country = self.create_country()
        data = self.region_data(country)
        data["name"] = self.name
        data["iso_code"] = self.iso_code
        self.verify_create_region(
            country,
            data=data,
            expected_name=self.name)

    def test_get_province(self):
        self.verify_get_defaults()

    def test_put_province_partial(self):
        instance = self.create_instance_default()
        country = self.create_country()
        data = dict(id=instance.id, name=self.name,
                    iso_code=self.iso_code,
                    country=country.id)
        self.verify_put(self.url_detail, instance, data, self.serializer_class)

    def test_delete_province(self):
        self.verify_delete_default()


class StateApiTestCase(RegionApiTestCase):
    """State API unit test class."""
    factory_class = factories.StateModelFactory
    model_class = models.State
    serializer_class = serializers.StateSerializer

    url_detail = "state-detail"
    url_list = "state-list"

    name = factories.StateModelFactory.STATE_ALABAMA
    iso_code = factories.StateModelFactory.ISO_3166_2_ALABAMA
    country = factories.CountryModelFactory.COUNTRY_USA

    def test_create_state(self):
        country = self.create_country()
        self.verify_create_region(
            country, expected_name=self.name)

    def test_create_state_partial(self):
        country = self.create_country()
        data = self.region_data(country)
        data["name"] = self.name
        data["iso_code"] = self.iso_code
        self.verify_create_region(
            country,
            data=data,
            expected_name=self.name)

    def test_get_state(self):
        self.verify_get_defaults()

    def test_put_state_partial(self):
        instance = self.create_instance_default()
        country = self.create_country()
        data = dict(id=instance.id, name=self.name,
                    iso_code=self.iso_code,
                    country=country.id)
        self.verify_put(self.url_detail, instance, data, self.serializer_class)

    def test_delete_state(self):
        self.verify_delete_default()


class CityApiTestCase(NamdedModelApiTestCase):
    """Base class for city rest api test cases"""
    model_class = models.City
    serializer_class = serializers.CitySerializer

    url_detail = "city-detail"
    url_list = "city-list"

    def post_required_data(self, ref_instance, user=None, site=None):
        """Return named model post request required data."""
        data = super(
            CityApiTestCase, self).post_required_data(user, site)
        data.update(self.city_data(ref_instance))
        return data

    def verify_create_city(
            self, ref_instance=None, data=None, expected_name=None):
        """Generate post request for geographic location creation."""
        data = data or self.post_required_data(ref_instance)
        response, instance = self.verify_create(
            url=self.url_list,
            data=data,
            model_class=self.model_class,
            expected_name=expected_name)

        attrs = self.verify_attrs
        if ref_instance:
            self.assert_instance_equal(ref_instance, instance, attrs)

        return response, instance


class FrenchCityApiTestCase(CityApiTestCase):
    """French City API unit test class."""
    factory_class = factories.FrenchCityModelFactory
    name = "Lille"
    verify_attrs = ("province",)

    def city_data(self, instance):
        """return city data"""
        instance = instance or self.factory_class()
        data = dict(province=instance.province.id)
        return data

    def test_create_city(self):
        instance = self.create_instance_default()
        self.verify_create_city(
            ref_instance=instance, expected_name=self.name)

    def test_create_city_partial(self):
        instance = self.create_instance_default()
        data = self.city_data(instance)
        data["name"] = self.name
        data["province"] = instance.province.id
        self.verify_create_city(
            ref_instance=instance,
            data=data,
            expected_name=self.name)

    def test_get_city(self):
        self.verify_get_defaults()

    def test_put_city_partial(self):
        instance = self.create_instance_default()
        data = dict(
            id=instance.id, name=self.name, province=instance.province.id)
        self.verify_put(self.url_detail, instance, data, self.serializer_class)

    def test_delete_city(self):
        self.verify_delete_default()


class USCityApiTestCase(CityApiTestCase):
    """US City API unit test class."""
    factory_class = factories.USCityModelFactory
    name = "Houston"
    verify_attrs = ("state",)

    def city_data(self, instance):
        """return city location data"""
        instance = instance or self.factory_class()
        data = dict(state=instance.state.id)
        return data

    def test_create_city(self):
        instance = self.create_instance_default()
        self.verify_create_city(
            ref_instance=instance, expected_name=self.name)

    def test_create_city_partial(self):
        instance = self.create_instance_default()
        data = self.city_data(instance)
        data["name"] = self.name
        data["state"] = instance.state.id
        self.verify_create_city(
            ref_instance=instance,
            data=data,
            expected_name=self.name)

    def test_get_city(self):
        self.verify_get_defaults()

    def test_put_city_partial(self):
        instance = self.create_instance_default()
        data = dict(id=instance.id, name=self.name, state=instance.state.id)
        self.verify_put(self.url_detail, instance, data, self.serializer_class)

    def test_delete_city(self):
        self.verify_delete_default()


class AddressApiTestCase(VersionedModelApiTestCase):
    """Base class for address api test cases."""
    url_detail = "address-detail"
    url_list = "address-list"
    model_class = models.Address
    serializer_class = serializers.AddressSerializer
    label = "Mr John Smith"

    def address_data(self, instance):
        """return address data"""
        instance = instance or self.factory_class()
        data = dict(
            city=instance.city,
            country=instance.country.id,
            label=self.label,
            postal_code=instance.postal_code,
            street_address=instance.street_address)
        return data

    def post_required_data(self, ref_instance, user=None, site=None):
        """Return named model post request required data."""
        data = super(
            AddressApiTestCase, self).post_required_data(user, site)
        data.update(self.address_data(ref_instance))
        return data

    def verify_create_address(
            self, ref_instance=None,
            data=None, extra_attrs=None,
            expected_label=None):
        """Generate post request for address creation."""
        data = data or self.post_required_data(ref_instance)

        response, instance = self.verify_create(
            url_name=self.url_list,
            data=data,
            model_class=self.model_class)

        base_attrs = ("city", "country", "postal_code", "street_address",)
        attrs = base_attrs + extra_attrs if extra_attrs else base_attrs
        if ref_instance:
            self.assert_instance_equal(ref_instance, instance, attrs)

        self.assertEqual(instance.label, expected_label,
                         "label comparison mismatch")

        return response, instance


class FrenchAddressApiTestCase(AddressApiTestCase):
    """French address API unit test class."""
    factory_class = factories.FrenchAddressModelFactory

    def address_data(self, instance):
        """return address data"""
        instance = instance or self.factory_class()
        data = super(FrenchAddressApiTestCase, self).address_data(instance)
        data.update(dict(province=instance.province.id))
        return data

    def test_create_address(self):
        instance = self.create_instance_default()
        self.verify_create_address(
            ref_instance=instance,
            extra_attrs=("province",),
            expected_label=self.label)

    def test_create_address_partial(self):
        instance = self.create_instance_default()
        data = self.address_data(instance)
        self.verify_create_address(
            ref_instance=instance,
            data=data,
            expected_label=self.label)

    def test_get_address(self):
        self.verify_get_defaults()

    def test_put_address_partial(self):
        instance = self.create_instance_default()
        data = dict(id=instance.id, label=self.label)
        self.verify_put(self.url_detail, instance, data, self.serializer_class)

    def test_delete_address(self):
        self.verify_delete_default()


class USAddressApiTestCase(AddressApiTestCase):
    """US address API unit test class."""
    factory_class = factories.USAddressModelFactory

    def address_data(self, instance):
        """return address data"""
        instance = instance or self.factory_class()
        data = super(USAddressApiTestCase, self).address_data(instance)
        data.update(dict(state=instance.state.id))
        return data

    def test_create_address(self):
        instance = self.create_instance_default()
        self.verify_create_address(
            ref_instance=instance,
            extra_attrs=("state",),
            expected_label=self.label)

    def test_create_address_partial(self):
        instance = self.create_instance_default()
        data = self.address_data(instance)
        self.verify_create_address(
            ref_instance=instance,
            data=data,
            expected_label=self.label)

    def test_get_address(self):
        self.verify_get_defaults()

    def test_put_address_partial(self):
        instance = self.create_instance_default()
        data = dict(id=instance.id, label=self.label)
        self.verify_put(self.url_detail, instance, data, self.serializer_class)

    def test_delete_address(self):
        self.verify_delete_default()
