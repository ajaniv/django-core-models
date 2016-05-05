"""
.. module::  social_media.tests.test_models
   :synopsis: social media application models unit test module.

*social media*  application models unit test module.
"""
from __future__ import print_function


from django_core_utils.tests.test_utils import (NamedModelTestCase,
                                                VersionedModelTestCase)

from . import factories


class EmailTypeTestCase(NamedModelTestCase):
    """Email type model unit test class.
    """
    def test_email_type_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=factories.EmailTypeModelFactory,
            get_by_name="name_1")


class FormattedNameTestCase(VersionedModelTestCase):
    """Formatted name model unit test class.
    """
    def test_formatted_name_crud(self):
        self.verify_versioned_model_crud(
            factory_class=factories.FormattedNameModelFactory)

    def test_str(self):
        name = 'John Smith'
        instance = factories.FormattedNameModelFactory(name=name)
        self.assertTrue(
            str(instance).endswith(
                '{}'.format(name)))


class GroupTestCase(NamedModelTestCase):
    """Group model unit test class.
    """
    def test_group_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=factories.GroupModelFactory,
            get_by_name="name_1")


class InstantMessagingTypeTestCase(NamedModelTestCase):
    """Instant messaging type model unit test class.
    """
    def test_instant_messaging_type_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=factories.InstantMessagingTypeModelFactory,
            get_by_name="name_1")


class LogoTypeTestCase(NamedModelTestCase):
    """Logo type model unit test class.
    """
    def test_nickname_type_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=factories.LogoTypeModelFactory,
            get_by_name="name_1")


class NameTestCase(VersionedModelTestCase):
    """Name model unit test class.
    """
    def test_name_crud(self):
        self.verify_versioned_model_crud(
            factory_class=factories.NameModelFactory)

    def test_other_fields(self):

        instance = factories.NameModelFactory(
            additional_name='name_0',
            honorific_prefix='name_1',
            honorific_suffix='name_2')
        attrs = ('additional_name', 'honorific_prefix', 'honorific_suffix')
        for index, attr in enumerate(attrs):
            self.assertEqual(
                getattr(instance, attr),
                'name_%s' % index,
                'name other fields initialization error')

    def test_full_name(self):
        family_name = 'Smith'
        given_name = 'John'
        instance = factories.NameModelFactory(
            family_name=family_name, given_name=given_name)
        self.assertTrue(
            instance.full_name.startswith(
                '{} {}'.format(given_name, family_name)))

    def test_str(self):
        family_name = 'Smith'
        given_name = 'John'
        instance = factories.NameModelFactory(
            family_name=family_name, given_name=given_name)
        self.assertTrue(
            str(instance).endswith(
                '{} {}'.format(family_name, given_name)))


class NicknameTypeTestCase(NamedModelTestCase):
    """Nickname type model unit test class.
    """
    def test_nickname_type_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=factories.NicknameTypeModelFactory,
            get_by_name="name_1")


class PhoneTypeTestCase(NamedModelTestCase):
    """Phone type model unit test class.
    """
    def test_phone_type_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=factories.PhoneTypeModelFactory,
            get_by_name="name_1")


class PhotoTypeTestCase(NamedModelTestCase):
    """Photo type model unit test class.
    """
    def test_photo_type_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=factories.PhotoTypeModelFactory,
            get_by_name="name_1")


class UrlTypeTestCase(NamedModelTestCase):
    """Url type model unit test class.
    """
    def test_url_type_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=factories.UrlTypeModelFactory,
            get_by_name="name_1")
