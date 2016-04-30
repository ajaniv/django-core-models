"""
.. module::  django_core_models.demographics.tests.factories
   :synopsis: demographics application factories module.

*demographics* application unit test factories module.
"""
from __future__ import print_function

from django_core_utils.tests.factories import NamedModelFactory

from .. import models


class AgeModelFactory(NamedModelFactory):
    """Age model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = models.Age


class ChildCountModelFactory(NamedModelFactory):
    """Child count model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = models.ChildCount


class DemographicRegionModelFactory(NamedModelFactory):
    """Demographic region model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = models.DemographicRegion


class EducationLevelModelFactory(NamedModelFactory):
    """Education level model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = models.EducationLevel


class EthnicityModelFactory(NamedModelFactory):
    """Ethnicity model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = models.Ethnicity


class GenderModelFactory(NamedModelFactory):
    """Gender model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = models.Gender


class HouseholdSizeModelFactory(NamedModelFactory):
    """HouseholdSize model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = models.HouseholdSize


class IncomeModelFactory(NamedModelFactory):
    """Income model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = models.Income
