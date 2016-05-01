"""
.. module::  django_core_models.demographics.tests.factories
   :synopsis: demographics application factories module.

*demographics* application unit test factories module.
"""
from __future__ import absolute_import, print_function

from django_core_utils.tests.factories import NamedModelFactory

from .. import models


class AgeModelFactory(NamedModelFactory):
    """Age model factory class.
    """
    name = "age < 12"

    class Meta(object):
        """Model meta class."""
        model = models.Age


class ChildCountModelFactory(NamedModelFactory):
    """Child count model factory class.
    """
    name = "4"

    class Meta(object):
        """Model meta class."""
        model = models.ChildCount


class DemographicRegionModelFactory(NamedModelFactory):
    """Demographic region model factory class.
    """
    name = "NorthEast"

    class Meta(object):
        """Model meta class."""
        model = models.DemographicRegion


class EducationLevelModelFactory(NamedModelFactory):
    """Education level model factory class.
    """
    name = "No schooling completed"

    class Meta(object):
        """Model meta class."""
        model = models.EducationLevel


class EthnicityModelFactory(NamedModelFactory):
    """Ethnicity model factory class.
    """
    name = "White"

    class Meta(object):
        """Model meta class."""
        model = models.Ethnicity


class GenderModelFactory(NamedModelFactory):
    """Gender model factory class.
    """
    name = "Female"

    class Meta(object):
        """Model meta class."""
        model = models.Gender


class HouseholdSizeModelFactory(NamedModelFactory):
    """HouseholdSize model factory class.
    """
    name = "1"

    class Meta(object):
        """Model meta class."""
        model = models.HouseholdSize


class IncomeModelFactory(NamedModelFactory):
    """Income model factory class.
    """
    name = "10000 < income < 20000"

    class Meta(object):
        """Model meta class."""
        model = models.Income
