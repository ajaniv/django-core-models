"""
.. module::  social_media.tests.test_models
   :synopsis: social media application models unit test module.

*social media*  application models unit test module.
"""
from __future__ import print_function

import factory.fuzzy

from django_core_utils.tests.factories import (NamedModelFactory,
                                               VersionedModelFactory)
from django_core_utils.tests.test_util import (NamedModelTestCase,
                                               VersionedModelTestCase)

from ..models import (EmailType, FormattedName, Group, InstantMessagingType,
                      LogoType, Name, NicknameType, PhoneType, PhotoType,
                      UrlType)


class GroupModelFactory(NamedModelFactory):
    """Group model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = Group


class GroupTestCase(NamedModelTestCase):
    """Group model unit test class.
    """
    def test_group_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=GroupModelFactory,
            get_by_name="name_1")


class NameModelFactory(VersionedModelFactory):
    """Name model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = Name

    family_name = factory.fuzzy.FuzzyText()
    given_name = factory.fuzzy.FuzzyText()


class NameTestCase(VersionedModelTestCase):
    """Name model unit test class.
    """
    def test_name_crud(self):
        self.verify_versioned_model_crud(
            factory_class=NameModelFactory)

    def test_other_fields(self):

        instance = NameModelFactory(additional_name='name_0',
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
        instance = NameModelFactory(
            family_name=family_name, given_name=given_name)
        self.assertTrue(
            instance.full_name.startswith(
                '{} {}'.format(given_name, family_name)))

    def test_str(self):
        family_name = 'Smith'
        given_name = 'John'
        instance = NameModelFactory(
            family_name=family_name, given_name=given_name)
        self.assertTrue(
            str(instance).endswith(
                '{} {}'.format(family_name, given_name)))


class FormattedNameModelFactory(VersionedModelFactory):
    """Formatted name model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = FormattedName

    name = factory.fuzzy.FuzzyText()


class FormattedNameTestCase(VersionedModelTestCase):
    """Formatted name model unit test class.
    """
    def test_formatted_name_crud(self):
        self.verify_versioned_model_crud(
            factory_class=FormattedNameModelFactory)

    def test_str(self):
        name = 'John Smith'
        instance = FormattedNameModelFactory(name=name)
        self.assertTrue(
            str(instance).endswith(
                '{}'.format(name)))


class NicknameTypeModelFactory(NamedModelFactory):
    """Nickname type model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = NicknameType


class NicknameTypeTestCase(NamedModelTestCase):
    """Nickname type model unit test class.
    """
    def test_nickname_type_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=NicknameTypeModelFactory,
            get_by_name="name_1")


class LogoTypeModelFactory(NamedModelFactory):
    """Logo type model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = LogoType


class LogoTypeTestCase(NamedModelTestCase):
    """Logo type model unit test class.
    """
    def test_nickname_type_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=LogoTypeModelFactory,
            get_by_name="name_1")


class PhotoTypeModelFactory(NamedModelFactory):
    """Photo type model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = PhotoType


class PhotoTypeTestCase(NamedModelTestCase):
    """Photo type model unit test class.
    """
    def test_photo_type_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=PhotoTypeModelFactory,
            get_by_name="name_1")


class UrlTypeModelFactory(NamedModelFactory):
    """Url type model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = UrlType


class UrlTypeTestCase(NamedModelTestCase):
    """Url type model unit test class.
    """
    def test_url_type_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=UrlTypeModelFactory,
            get_by_name="name_1")


class PhoneTypeModelFactory(NamedModelFactory):
    """Phone type model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = PhoneType


class PhoneTypeTestCase(NamedModelTestCase):
    """Phone type model unit test class.
    """
    def test_phone_type_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=PhoneTypeModelFactory,
            get_by_name="name_1")


class EmailTypeModelFactory(NamedModelFactory):
    """Email type model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = EmailType


class EmailTypeTestCase(NamedModelTestCase):
    """Email type model unit test class.
    """
    def test_email_type_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=EmailTypeModelFactory,
            get_by_name="name_1")


class InstantMessagingTypeModelFactory(NamedModelFactory):
    """Instant messaging type model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = InstantMessagingType


class InstantMessagingTypeTestCase(NamedModelTestCase):
    """Instant messaging type model unit test class.
    """
    def test_instant_messaging_type_crud(self):
        self.verify_named_model_crud(
            names=("name_1", "name_2"),
            factory_class=InstantMessagingTypeModelFactory,
            get_by_name="name_1")
