"""
.. module::  core_models.tests
   :synopsis: core models demographics unit test module.

*core models* demographics unit test module.
"""
from __future__ import print_function

from core_utils.tests.factories import NamedModelFactory
from core_utils.tests.test_util import NamedModelTestCase

from ..models import Gender, GENDER, MALE, FEMALE


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
        for name in GENDER:
            instance = GenderModelFactory(name=name)
            self.verify_instance(instance)
        gender_count = Gender.objects.count()
        self.assertEqual(
            len(GENDER),
            gender_count, "Missing gender instances")
        male = Gender.objects.get(name=MALE)
        male.name = 'new gender'
        male.save()
        self.assertEqual(male.version, 2, "Gender version mismatch")
        male.delete()
        self.assertEqual(
            Gender.objects.count() + 1,
            gender_count, "Missing gender instances")

    def test_sex(self):
        gender = GenderModelFactory(name=MALE)
        self.assertEqual(gender.sex, MALE)
        gender.sex = FEMALE
        gender.save()
        self.assertTrue(Gender.objects.get(name=FEMALE))
