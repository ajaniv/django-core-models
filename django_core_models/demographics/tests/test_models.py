"""
.. module::  demographics.test
   :synopsis: demographics application models unit test module.

*demographics* application models unit test module.
"""
from __future__ import absolute_import, print_function

from django_core_utils.tests.test_utils import NamedModelTestCase
from . import factories
from ..models import GENDER, GENDER_FEMALE, GENDER_MALE, Gender


class AgeTestCase(NamedModelTestCase):
    """Age model unit test class.
    """
    def test_age_crud(self):
        self.verify_named_model_crud(
            names=self.NAMES,
            factory_class=factories.AgeModelFactory,
            get_by_name=self.NAME_1)


class ChildCountTestCase(NamedModelTestCase):
    """Child count model unit test class.
    """
    def test_child_count_crud(self):
        self.verify_named_model_crud(
            names=self.NAMES,
            factory_class=factories.AgeModelFactory,
            get_by_name=self.NAME_1)


class DemographicRegionTestCase(NamedModelTestCase):
    """Demographic region  model unit test class.
    """
    def test_demographic_region_count_crud(self):
        self.verify_named_model_crud(
            names=self.NAMES,
            factory_class=factories.DemographicRegionModelFactory,
            get_by_name=self.NAME_1)


class EducationLevelTestCase(NamedModelTestCase):
    """Education level   model unit test class.
    """
    def test_education_level_crud(self):
        self.verify_named_model_crud(
            names=self.NAMES,
            factory_class=factories.EducationLevelModelFactory,
            get_by_name=self.NAME_1)


class EthnicityTestCase(NamedModelTestCase):
    """Ethnicity model unit test class.
    """
    def test_ethnicity_crud(self):
        self.verify_named_model_crud(
            names=self.NAMES,
            factory_class=factories.EthnicityModelFactory,
            get_by_name=self.NAME_1)


class GenderTestCase(NamedModelTestCase):
    """Gender model unit test class.
    """
    def test_gender_crud(self):
        self.verify_named_model_crud(
            names=GENDER,
            factory_class=factories.GenderModelFactory,
            get_by_name=GENDER_MALE)

    def test_sex(self):
        gender = factories.GenderModelFactory(name=GENDER_MALE)
        self.assertEqual(gender.sex, GENDER_MALE)
        gender.sex = GENDER_FEMALE
        gender.save()
        self.assertTrue(Gender.objects.get(name=GENDER_FEMALE))


class HouseholdSizeTestCase(NamedModelTestCase):
    """Household size model unit test class.
    """
    def test_household_size_crud(self):
        self.verify_named_model_crud(
            names=self.NAMES,
            factory_class=factories.HouseholdSizeModelFactory,
            get_by_name=self.NAME_1)


class IncomeTestCase(NamedModelTestCase):
    """Income  model unit test class.
    """
    def test_income_crud(self):
        self.verify_named_model_crud(
            names=self.NAMES,
            factory_class=factories.IncomeModelFactory,
            get_by_name=self.NAME_1)
