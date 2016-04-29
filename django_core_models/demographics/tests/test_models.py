"""
.. module::  demographics.test
   :synopsis: demographics application models unit test module.

*demographics* application models unit test module.
"""
from __future__ import print_function

from django_core_utils.tests.factories import NamedModelFactory
from django_core_utils.tests.test_utils import NamedModelTestCase

from ..models import GENDER, GENDER_FEMALE, GENDER_MALE, Gender


class GenderModelFactory(NamedModelFactory):
    """Gender model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = Gender


class GenderTestCase(NamedModelTestCase):
    """Gender model unit test class.
    """
    def test_gender_crud(self):
        self.verify_named_model_crud(names=GENDER,
                                     factory_class=GenderModelFactory,
                                     get_by_name=GENDER_MALE)

    def test_sex(self):
        gender = GenderModelFactory(name=GENDER_MALE)
        self.assertEqual(gender.sex, GENDER_MALE)
        gender.sex = GENDER_FEMALE
        gender.save()
        self.assertTrue(Gender.objects.get(name=GENDER_FEMALE))
