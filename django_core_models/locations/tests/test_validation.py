"""
.. module::  location.tests.test_validation
   :synopsis: location application validation unit test module.

*location* application validation unit test module.
"""
from __future__ import print_function

from django.core.exceptions import ValidationError

from django_core_utils.tests.test_utils import BaseModelTestCase

from . import factories
from ..validation import (country_validation, language_validation,
                          post_office_box_validation, postal_code_validation,
                          province_validation, state_validation)
from .factories import (CountryModelFactory, LanguageModelFactory,
                        ProvinceModelFactory, StateModelFactory)


class ValidationTestCase(BaseModelTestCase):
    """Base validation unit test class."""
    def country_usa(self):
        return factories.country_usa()

    def country_france(self):
        return factories.country_france()

valid_post_office_boxes = (
    'PO Box 001', 'P.O. Box 002', 'po b 001', 'po bin 001',
    'Post O bin 001', 'P. Office bin 001',
    'P.O.Box 003')

invalid_post_office_boxes = ('004 P.O. Box', '005 PO Box', '006', 'abc')


class PostOfficeBoxValidationTestCase(ValidationTestCase):
    """Post office box validation unit test class."""

    def test_post_office_box_validation_usa(self):
        for pob in valid_post_office_boxes:
            post_office_box_validation(self.country_usa(), pob)

    def test_usa_post_office_box_validation_exceptions_usa(self):
        for pob in invalid_post_office_boxes:
            with self.assertRaises(ValidationError):
                post_office_box_validation(self.country_usa(), pob)

valid_postal_codes = ('12345', '12345-6789', '12345 - 6789')
invalid_postal_codes = ('1234', '1234A', '12345 A', '12345-6789A')


class PostalCodeValidationTestCase(ValidationTestCase):
    """Postal code validation unit test class."""

    def test_postal_code_validation_usa(self):
        for postal_box in valid_postal_codes:
            postal_code_validation(self.country_usa(), postal_box)

    def test_postal_code_validation_exceptions_usa(self):
        for pob in invalid_postal_codes:
            with self.assertRaises(ValidationError):
                postal_code_validation(self.country_usa(), pob)


class CountryValidationTestCase(ValidationTestCase):
    """Country validation unit test class."""

    def test_country_validation_usa(self):
        country_validation(self.country_usa())

    def test_postal_code_validation_exceptions_usa(self):
        with self.assertRaises(ValidationError):
                country_validation(CountryModelFactory(
                    name="USA", iso_code="US"))


class LanguageValidationTestCase(ValidationTestCase):
    """Language validation unit test class."""

    def test_language_validation_usa(self):
        language_validation(LanguageModelFactory(
            name=LanguageModelFactory.LANGUAGE_FRENCH,
            iso_code=LanguageModelFactory.ISO_639_2_FR))

    def test_language_validation_exceptions_usa(self):
        with self.assertRaises(ValidationError):
            country_validation(CountryModelFactory(
                name="French", iso_code="zz"))


class ProvinceValidationTestCase(ValidationTestCase):
    """Province validation unit test class."""

    def test_province_validation(self):
        province_validation(ProvinceModelFactory(
            name=ProvinceModelFactory.PROVINCE_LOWER_NORMANDY,
            iso_code=ProvinceModelFactory.ISO_3166_2_Normandy,
            country=self.country_france()))

    def test_province_validation_invalid_iso(self):
        with self.assertRaises(ValidationError):
            province_validation(ProvinceModelFactory(
                name=ProvinceModelFactory.PROVINCE_LOWER_NORMANDY,
                iso_code="FR-ABC",
                country=self.country_france()))

    def test_province_validation_invalid_name(self):
        with self.assertRaises(ValidationError):
            province_validation(StateModelFactory(
                name="Bad name",
                iso_code=ProvinceModelFactory.ISO_3166_2_Normandy,
                country=self.country_france()))

    def test_state_validation_invalid_country(self):
        with self.assertRaises(ValidationError):
            province_validation(StateModelFactory(
                name=ProvinceModelFactory.PROVINCE_LOWER_NORMANDY,
                iso_code=ProvinceModelFactory.ISO_3166_2_Normandy,
                country=self.country_usa()))


class StateValidationTestCase(ValidationTestCase):
    """State validation unit test class."""

    def test_state_validation(self):
        state_validation(StateModelFactory(
            name="New Jersey", iso_code="US-NJ",
            country=self.country_usa()))

    def test_state_validation_invalid_iso(self):
        with self.assertRaises(ValidationError):
            state_validation(StateModelFactory(
                name="New Jersey",
                iso_code="US-NJT",
                country=self.country_usa()))

    def test_state_validation_invalid_name(self):
        with self.assertRaises(ValidationError):
            state_validation(StateModelFactory(
                name="Old Jersey",
                iso_code="US-NJ",
                country=self.country_usa()))

    def test_state_validation_invalid_country(self):
        with self.assertRaises(ValidationError):
            state_validation(StateModelFactory(
                name="New Jersey",
                iso_code="US-NJ",
                country=self.country_france()))
