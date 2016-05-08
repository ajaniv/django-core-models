"""
.. module::  django_core_models.social_media.tests.test_views
   :synopsis: social_media models application views unit test module.

*social_media*  application views unit test module.
"""
from __future__ import absolute_import, print_function
from django_core_utils.tests.api_test_utils import (NamedModelApiTestCase,
                                                    VersionedModelApiTestCase)

from . import factories
from .. import models
from .. import serializers


class EmailTypeApiTestCase(NamedModelApiTestCase):
    """EmailType API unit test class."""
    factory_class = factories.EmailTypeModelFactory
    model_class = models.EmailType
    serializer_class = serializers.EmailTypeSerializer

    url_detail = "email-type-detail"
    url_list = "email-type-list"

    name = factories.EmailTypeModelFactory.name

    def test_create_email_type(self):
        self.verify_create_defaults()

    def test_create_email_type_partial(self):
        self.verify_create_defaults_partial()

    def test_get_email_type(self):
        self.verify_get_defaults()

    def test_put_email_type_partial(self):
        instance = self.create_instance_default()
        data = dict(id=instance.id, name=self.name)
        self.verify_put(self.url_detail, instance, data, self.serializer_class)

    def test_delete_email_type(self):
        self.verify_delete_default()


class SimpleNameApiTestCase(VersionedModelApiTestCase):
    """SimpleName model api test case class."""
    def name_data(self,):
        """return  name data"""
        data = dict(name=self.name)
        return data

    def post_required_data(self, user=None, site=None):
        """Return  post request required data."""
        data = super(
            SimpleNameApiTestCase, self).post_required_data(user, site)
        data.update(self.name_data())
        return data

    def verify_create_name(self, data=None):
        """Generate and verify post request for  name creation."""
        data = data or self.post_required_data()
        response, instance = self.verify_create(
            url_name=self.url_list,
            data=data,
            model_class=self.model_class)

        self.assertEqual(instance.name,
                         self.name,
                         "name initialization error")

        return response, instance


class FormattedNameApiTestCase(SimpleNameApiTestCase):
    """FormattedName API unit test class."""
    factory_class = factories.FormattedNameModelFactory
    model_class = models.FormattedName
    serializer_class = serializers.FormattedNameSerializer

    url_detail = "formatted-name-detail"
    url_list = "formatted-name-list"

    name = "Mr John Smith II"

    def test_create_formatted_name(self):
        self.verify_create_name()

    def test_create_formatted_name_partial(self):
        data = self.name_data()
        self.verify_create_name(data=data)

    def test_get_formatted_name(self):
        self.verify_get_defaults()

    def test_put_formatted_name_partial(self):
        instance = self.create_instance_default()
        data = dict(id=instance.id, name=self.name)
        self.verify_put(self.url_detail, instance, data, self.serializer_class)

    def test_delete_formatted_name(self):
        self.verify_delete_default()


class NicknameApiTestCase(SimpleNameApiTestCase):
    """Nickname API unit test class."""
    factory_class = factories.NicknameModelFactory
    model_class = models.Nickname
    serializer_class = serializers.NicknameSerializer

    url_detail = "nickname-detail"
    url_list = "nickname-list"

    name = "smiley"

    def test_create_nickname(self):
        self.verify_create_name()

    def test_create_nickname_partial(self):
        data = self.name_data()
        self.verify_create_name(data=data)

    def test_get_nickname_name(self):
        self.verify_get_defaults()

    def test_put_nickname_partial(self):
        instance = self.create_instance_default()
        data = dict(id=instance.id, name=self.name)
        self.verify_put(self.url_detail, instance, data, self.serializer_class)

    def test_delete_nickname(self):
        self.verify_delete_default()


class GroupApiTestCase(NamedModelApiTestCase):
    """Group API unit test class."""
    factory_class = factories.GroupModelFactory
    model_class = models.Group
    serializer_class = serializers.GroupSerializer

    url_detail = "group-detail"
    url_list = "group-list"

    name = factories.GroupModelFactory.name

    def test_create_group(self):
        self.verify_create_defaults()

    def test_create_group_partial(self):
        self.verify_create_defaults_partial()

    def test_get_group(self):
        self.verify_get_defaults()

    def test_put_group_partial(self):
        instance = self.create_instance_default()
        data = dict(id=instance.id, name=self.name)
        self.verify_put(self.url_detail, instance, data, self.serializer_class)

    def test_delete_email_type(self):
        self.verify_delete_default()


class InstantMessagingTypeApiTestCase(NamedModelApiTestCase):
    """InstantMessagingType API unit test class."""
    factory_class = factories.InstantMessagingTypeModelFactory
    model_class = models.InstantMessagingType
    serializer_class = serializers.InstantMessagingTypeSerializer

    url_detail = "instant-messaging-type-detail"
    url_list = "instant-messaging-type-list"

    name = factories.InstantMessagingTypeModelFactory.name

    def test_create_instant_messaging_type(self):
        self.verify_create_defaults()

    def test_create_instant_messaging_type_partial(self):
        self.verify_create_defaults_partial()

    def test_get_instant_messaging_type(self):
        self.verify_get_defaults()

    def test_put_instant_messaging_type_partial(self):
        instance = self.create_instance_default()
        data = dict(id=instance.id, name=self.name)
        self.verify_put(self.url_detail, instance, data, self.serializer_class)

    def test_delete_instant_messaging_type(self):
        self.verify_delete_default()


class LogoTypeApiTestCase(NamedModelApiTestCase):
    """LogoType API unit test class."""
    factory_class = factories.LogoTypeModelFactory
    model_class = models.LogoType
    serializer_class = serializers.LogoTypeSerializer

    url_detail = "logo-type-detail"
    url_list = "logo-type-list"

    name = factories.LogoTypeModelFactory.name

    def test_create_logo_type(self):
        self.verify_create_defaults()

    def test_create_logo_type_partial(self):
        self.verify_create_defaults_partial()

    def test_get_logo_type(self):
        self.verify_get_defaults()

    def test_put_logo_type_partial(self):
        instance = self.create_instance_default()
        data = dict(id=instance.id, name=self.name)
        self.verify_put(self.url_detail, instance, data, self.serializer_class)

    def test_delete_logo_type(self):
        self.verify_delete_default()


class NameApiTestCase(VersionedModelApiTestCase):
    """Name API unit test class."""
    factory_class = factories.NameModelFactory
    model_class = models.Name
    serializer_class = serializers.NameSerializer

    url_detail = "name-detail"
    url_list = "name-list"

    family_name = "Smith"
    given_name = "John"

    def name_data(self,):
        """return name data"""
        data = dict(family_name=self.family_name,
                    given_name=self.given_name)
        return data

    def post_required_data(self, user=None, site=None):
        """Return  post request required data."""
        data = super(
            NameApiTestCase, self).post_required_data(user, site)
        data.update(self.name_data())
        return data

    def verify_create_name(self, data=None):
        """Generate and verify post request for name creation."""
        data = data or self.post_required_data()
        response, instance = self.verify_create(
            url_name=self.url_list,
            data=data,
            model_class=self.model_class)

        self.assertEqual(instance.family_name,
                         self.family_name,
                         "name.family_name initialization error")
        self.assertEqual(instance.given_name,
                         self.given_name,
                         "name.given_name initialization error")

        return response, instance

    def test_create_name(self):
        self.verify_create_name()

    def test_create_name_partial(self):
        data = self.name_data()
        self.verify_create_name(data=data)

    def test_get_name(self):
        self.verify_get_defaults()

    def test_put_name_partial(self):
        instance = self.create_instance_default()
        data = dict(id=instance.id,
                    family_name=self.family_name,
                    given_name=self.given_name)
        self.verify_put(self.url_detail, instance, data, self.serializer_class)

    def test_delete_formatted_name(self):
        self.verify_delete_default()


class NicknameTypeApiTestCase(NamedModelApiTestCase):
    """NicknameType API unit test class."""
    factory_class = factories.NicknameTypeModelFactory
    model_class = models.NicknameType
    serializer_class = serializers.NicknameTypeSerializer

    url_detail = "nickname-type-detail"
    url_list = "nickname-type-list"

    name = factories.NicknameTypeModelFactory.name

    def test_create_nickname_type(self):
        self.verify_create_defaults()

    def test_create_nickname_type_partial(self):
        self.verify_create_defaults_partial()

    def test_get_nickname_type(self):
        self.verify_get_defaults()

    def test_put_nickname_type_partial(self):
        instance = self.create_instance_default()
        data = dict(id=instance.id, name=self.name)
        self.verify_put(self.url_detail, instance, data, self.serializer_class)

    def test_delete_nickname_type(self):
        self.verify_delete_default()


class PhoneTypeApiTestCase(NamedModelApiTestCase):
    """PhoneType API unit test class."""
    factory_class = factories.PhoneTypeModelFactory
    model_class = models.PhoneType
    serializer_class = serializers.PhoneTypeSerializer

    url_detail = "phone-type-detail"
    url_list = "phone-type-list"

    name = factories.PhoneTypeModelFactory.name

    def test_create_phone_type(self):
        self.verify_create_defaults()

    def test_create_phone_type_partial(self):
        self.verify_create_defaults_partial()

    def test_get_phone_type(self):
        self.verify_get_defaults()

    def test_put_phone_type_partial(self):
        instance = self.create_instance_default()
        data = dict(id=instance.id, name=self.name)
        self.verify_put(self.url_detail, instance, data, self.serializer_class)

    def test_delete_phone_type(self):
        self.verify_delete_default()


class PhotoTypeApiTestCase(NamedModelApiTestCase):
    """PhotoType API unit test class."""
    factory_class = factories.PhotoTypeModelFactory
    model_class = models.PhotoType
    serializer_class = serializers.PhotoTypeSerializer

    url_detail = "photo-type-detail"
    url_list = "photo-type-list"

    name = factories.PhotoTypeModelFactory.name

    def test_create_photo_type(self):
        self.verify_create_defaults()

    def test_create_photo_type_partial(self):
        self.verify_create_defaults_partial()

    def test_get_photo_type(self):
        self.verify_get_defaults()

    def test_put_photo_type_partial(self):
        instance = self.create_instance_default()
        data = dict(id=instance.id, name=self.name)
        self.verify_put(self.url_detail, instance, data, self.serializer_class)

    def test_delete_photo_type(self):
        self.verify_delete_default()


class UrlTypeApiTestCase(NamedModelApiTestCase):
    """UrlType API unit test class."""
    factory_class = factories.UrlTypeModelFactory
    model_class = models.UrlType
    serializer_class = serializers.UrlTypeSerializer

    url_detail = "url-type-detail"
    url_list = "url-type-list"

    name = factories.UrlTypeModelFactory.name

    def test_create_url_type(self):
        self.verify_create_defaults()

    def test_create_url_type_partial(self):
        self.verify_create_defaults_partial()

    def test_get_url_type(self):
        self.verify_get_defaults()

    def test_put_url_type_partial(self):
        instance = self.create_instance_default()
        data = dict(id=instance.id, name=self.name)
        self.verify_put(self.url_detail, instance, data, self.serializer_class)

    def test_delete_url_type(self):
        self.verify_delete_default()
