"""
.. module::  demographics.models
   :synopsis:  demographics application  models module.

*demographics* application models module.

"""
from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _
from inflection import humanize, pluralize, underscore

from django_core_utils.constants import UNKNOWN
from django_core_utils.models import NamedModel, db_table

_app_label = "demographics"


_age = "Age"
_age_verbose = humanize(underscore(_age))


class Age(NamedModel):
    """Age demographics model class.
    """
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _age)
        verbose_name = _(_age_verbose)
        verbose_name_plural = _(pluralize(_age_verbose))

_child_count = "ChildCount"
_child_count_verbose = humanize(underscore(_child_count))


class ChildCount(NamedModel):
    """ChildCount demographics model class.
    """
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _child_count)
        verbose_name = _(_child_count_verbose)
        verbose_name_plural = _(pluralize(_child_count_verbose))

_demographic_region = "DemographicRegion"
_demographic_region_verbose = humanize(underscore(_demographic_region))


class DemographicRegion(NamedModel):
    """DemographicRegion demographics model class.
    """
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _demographic_region)
        verbose_name = _(_demographic_region_verbose)
        verbose_name_plural = _(pluralize(_demographic_region_verbose))

_education_level = "EducationLevel"
_education_level_verbose = humanize(underscore(_education_level))


class EducationLevel(NamedModel):
    """EducationLevel demographics model class.
    """
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _education_level)
        verbose_name = _(_education_level_verbose)
        verbose_name_plural = _(pluralize(_education_level_verbose))

_ethnicity = "Ethnicity"
_ethnicity_verbose = humanize(underscore(_ethnicity))


class Ethnicity(NamedModel):
    """Ethnicity demographics model class.
    """
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _ethnicity)
        verbose_name = _(_ethnicity_verbose)
        verbose_name_plural = _(pluralize(_ethnicity_verbose))

GENDER_MALE = 'Male'
GENDER_FEMALE = 'Female'
GENDER_UNKNOWN = UNKNOWN
GENDER = (GENDER_MALE, GENDER_FEMALE, GENDER_UNKNOWN)

_gender = "Gender"
_gender_verbose = humanize(underscore(_gender))


class Gender(NamedModel):
    """Gender demographics model class.

    Values may include  "male", "female", "other", "none", "unknown".
    """
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _gender)
        verbose_name = _(_gender_verbose)
        verbose_name_plural = _(pluralize(_gender_verbose))

    @property
    def sex(self):
        return self.name

    @sex.setter
    def sex(self, value):
        self.name = value

_household_size = "HouseHoldSize"
_household_size_verbose = humanize(underscore(_household_size))


class HouseHoldSize(NamedModel):
    """HouseHoldSize demographics model class.
    """
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _household_size)
        verbose_name = _(_household_size_verbose)
        verbose_name_plural = _(pluralize(_household_size_verbose))
_income = "Income"
_income_verbose = humanize(underscore(_income))


class Income(NamedModel):
    """Income demographics model class.
    """
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _income)
        verbose_name = _(_income_verbose)
        verbose_name_plural = _(pluralize(_income_verbose))
