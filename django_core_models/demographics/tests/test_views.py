"""
.. module::  django_core_models.demographics.tests.test_views
   :synopsis: demographics models application views unit test module.

*demographics* application views unit test module.
"""
from __future__ import absolute_import, print_function
from django_core_utils.tests.api_test_utils import NamdedModelApiTestCase

from . import factories
from .. import models
from .. import serializers


class AgeApiTestCase(NamdedModelApiTestCase):
    """Age API unit test class."""
    factory_class = factories.AgeModelFactory
    model_class = models.Age
    serializer_class = serializers.AgeSerializer

    url_detail = "age-detail"
    url_list = "age-list"

    name = factories.AgeModelFactory.name

    def test_create_age(self):
        self.verify_create_defaults()

    def test_create_age_partial(self):
        self.verify_create_defaults_partial()

    def test_get_age(self):
        self.verify_get_defaults()

    def test_put_age_partial(self):
        self.verify_put_partial()

    def test_delete_age(self):
        self.verify_delete_default()


class ChildCountApiTestCase(NamdedModelApiTestCase):
    """ChildCount API unit test class."""
    factory_class = factories.ChildCountModelFactory
    model_class = models.ChildCount
    serializer_class = serializers.ChildCountSerializer

    url_detail = "child-count-detail"
    url_list = "child-count-list"

    name = factories.ChildCountModelFactory.name

    def test_create_child_count(self):
        self.verify_create_defaults()

    def test_create_child_count_partial(self):
        self.verify_create_defaults_partial()

    def test_get_child_count(self):
        self.verify_get_defaults()

    def test_put_child_count_partial(self):
        self.verify_put_partial()

    def test_delete_child_count(self):
        self.verify_delete_default()


class DemographicRegionApiTestCase(NamdedModelApiTestCase):
    """DemographicRegion API unit test class."""
    factory_class = factories.DemographicRegionModelFactory
    model_class = models.DemographicRegion
    serializer_class = serializers.DemographicRegionSerializer

    url_detail = "demographic-region-detail"
    url_list = "demographic-region-list"

    name = factories.DemographicRegionModelFactory.name

    def test_create_demographic_region(self):
        self.verify_create_defaults()

    def test_create_demographic_region_partial(self):
        self.verify_create_defaults_partial()

    def test_get_demographic_region(self):
        self.verify_get_defaults()

    def test_put_demographic_region_partial(self):
        self.verify_put_partial()

    def test_delete_demographic_region(self):
        self.verify_delete_default()


class EducationLevelApiTestCase(NamdedModelApiTestCase):
    """EducationLevel API unit test class."""
    factory_class = factories.EducationLevelModelFactory
    model_class = models.EducationLevel
    serializer_class = serializers.EducationLevelSerializer

    url_detail = "education-level-detail"
    url_list = "education-level-list"

    name = factories.EducationLevelModelFactory.name

    def test_create_education_level(self):
        self.verify_create_defaults()

    def test_create_education_level_partial(self):
        self.verify_create_defaults_partial()

    def test_get_education_level(self):
        self.verify_get_defaults()

    def test_put_education_level_partial(self):
        self.verify_put_partial()

    def test_delete_education_level(self):
        self.verify_delete_default()


class EthnicityApiTestCase(NamdedModelApiTestCase):
    """Ethnicity API unit test class."""
    factory_class = factories.EthnicityModelFactory
    model_class = models.Ethnicity
    serializer_class = serializers.EthnicitySerializer

    url_detail = "ethnicity-detail"
    url_list = "ethnicity-list"

    name = factories.EthnicityModelFactory.name

    def test_create_ethnicity(self):
        self.verify_create_defaults()

    def test_create_ethnicity_partial(self):
        self.verify_create_defaults_partial()

    def test_get_ethnicity(self):
        self.verify_get_defaults()

    def test_put_ethnicity_partial(self):
        self.verify_put_partial()

    def test_delete_ethnicity(self):
        self.verify_delete_default()


class GenderApiTestCase(NamdedModelApiTestCase):
    """Gender API unit test class."""
    factory_class = factories.GenderModelFactory
    model_class = models.Gender
    serializer_class = serializers.GenderSerializer

    url_detail = "gender-detail"
    url_list = "gender-list"

    name = factories.GenderModelFactory.name

    def test_create_gender(self):
        self.verify_create_defaults()

    def test_create_gender_partial(self):
        self.verify_create_defaults_partial()

    def test_get_gender(self):
        self.verify_get_defaults()

    def test_put_gender_partial(self):
        self.verify_put_partial()

    def test_delete_gender(self):
        self.verify_delete_default()


class HouseholdSizeApiTestCase(NamdedModelApiTestCase):
    """HouseholdSize API unit test class."""
    factory_class = factories.HouseholdSizeModelFactory
    model_class = models.HouseholdSize
    serializer_class = serializers.HouseholdSizeSerializer

    url_detail = "household-size-detail"
    url_list = "household-size-list"

    name = factories.HouseholdSizeModelFactory.name

    def test_create_household_size(self):
        self.verify_create_defaults()

    def test_create_household_size_partial(self):
        self.verify_create_defaults_partial()

    def test_get_household_size(self):
        self.verify_get_defaults()

    def test_put_household_size_partial(self):
        self.verify_put_partial()

    def test_delete_household_size(self):
        self.verify_delete_default()


class IncomeApiTestCase(NamdedModelApiTestCase):
    """Income API unit test class."""
    factory_class = factories.IncomeModelFactory
    model_class = models.Income
    serializer_class = serializers.IncomeSerializer

    url_detail = "income-detail"
    url_list = "income-list"

    name = factories.IncomeModelFactory.name

    def test_create_income(self):
        self.verify_create_defaults()

    def test_create_income_partial(self):
        self.verify_create_defaults_partial()

    def test_get_income(self):
        self.verify_get_defaults()

    def test_put_income_partial(self):
        self.verify_put_partial()

    def test_delete_income(self):
        self.verify_delete_default()
