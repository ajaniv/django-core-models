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


class EmailApiTestCase(VersionedModelApiTestCase):
    """Email API unit test class."""
    factory_class = factories.EmailModelFactory
    model_class = models.Email
    serializer_class = serializers.EmailSerializer

    url_detail = "email-detail"
    url_list = "email-list"

    address = "joe.shmmoe@example.com"

    def email_data(self,):
        """return name data"""
        data = dict(address=self.address)
        return data

    def post_required_data(self, user=None, site=None):
        """Return  post request required data."""
        data = super(
            EmailApiTestCase, self).post_required_data(user, site)
        data.update(self.email_data())
        return data

    def verify_create_email(self, data=None):
        """Generate and verify post request for email creation."""
        data = data or self.post_required_data()
        response, instance = self.verify_create(
            url_name=self.url_list,
            data=data,
            model_class=self.model_class)

        self.assertEqual(instance.address,
                         self.address,
                         "email.addresss initialization error")

        return response, instance

    def test_create_email(self):
        self.verify_create_email()

    def test_create_email_partial(self):
        data = self.email_data()
        self.verify_create_email(data=data)

    def test_get_email(self):
        self.verify_get_defaults()

    def test_put_email_partial(self):
        instance = self.create_instance_default()
        data = dict(id=instance.id,
                    address=self.address)
        self.verify_put(self.url_detail, instance, data, self.serializer_class)

    def test_delete_email(self):
        self.verify_delete_default()


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


class InstantMessagingApiTestCase(VersionedModelApiTestCase):
    """InstantMessaging API unit test class."""
    factory_class = factories.InstantMessagingModelFactory
    model_class = models.InstantMessaging
    serializer_class = serializers.InstantMessagingSerializer

    url_detail = "instant-messaging-detail"
    url_list = "instant-messaging-list"

    address = factories.random_instant_messaging_address()

    def instant_messaging_data(self,):
        """return instant messaging data"""
        data = dict(address=self.address)
        return data

    def post_required_data(self, user=None, site=None):
        """Return  post request required data."""
        data = super(
            InstantMessagingApiTestCase, self).post_required_data(user, site)
        data.update(self.instant_messaging_data())
        return data

    def verify_create_instant_messaging(self, data=None):
        """Generate and verify post request for instant messaging creation."""
        data = data or self.post_required_data()
        response, instance = self.verify_create(
            url_name=self.url_list,
            data=data,
            model_class=self.model_class)

        self.assertEqual(instance.address,
                         self.address,
                         "InstantMessaging addresss initialization error")

        return response, instance

    def test_create_instant_messaging(self):
        self.verify_create_instant_messaging()

    def test_create_instant_messaging_partial(self):
        data = self.instant_messaging_data()
        self.verify_create_instant_messaging(data=data)

    def test_get_email(self):
        self.verify_get_defaults()

    def test_put_email_partial(self):
        instance = self.create_instance_default()
        data = dict(id=instance.id,
                    address=self.address)
        self.verify_put(self.url_detail, instance, data, self.serializer_class)

    def test_delete_instant_messaging(self):
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


class PhoneApiTestCase(VersionedModelApiTestCase):
    """Phone API unit test class."""
    factory_class = factories.PhoneModelFactory
    model_class = models.Phone
    serializer_class = serializers.PhoneSerializer

    url_detail = "phone-detail"
    url_list = "phone-list"

    number = factories.random_phone_number()

    def phone_data(self,):
        """return phone data"""
        data = dict(number=self.number)
        return data

    def post_required_data(self, user=None, site=None):
        """Return  post request required data."""
        data = super(
            PhoneApiTestCase, self).post_required_data(user, site)
        data.update(self.phone_data())
        return data

    def verify_create_phone(self, data=None):
        """Generate and verify post request for phone creation."""
        data = data or self.post_required_data()
        response, instance = self.verify_create(
            url_name=self.url_list,
            data=data,
            model_class=self.model_class)

        self.assertEqual(instance.number,
                         self.number,
                         "Phone.number initialization error")

        return response, instance

    def test_create_phone(self):
        self.verify_create_phone()

    def test_create_phone_partial(self):
        data = self.phone_data()
        self.verify_create_phone(data=data)

    def test_get_phone(self):
        self.verify_get_defaults()

    def test_put_phone_partial(self):
        instance = self.create_instance_default()
        data = dict(id=instance.id,
                    number=self.number)
        self.verify_put(self.url_detail, instance, data, self.serializer_class)

    def test_delete_phone(self):
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


class UrlApiTestCase(VersionedModelApiTestCase):
    """Url API unit test class."""
    factory_class = factories.UrlModelFactory
    model_class = models.Url
    serializer_class = serializers.UrlSerializer

    url_detail = "url-detail"
    url_list = "url-list"

    address = factories.random_url()

    def url_data(self,):
        """return url data"""
        data = dict(address=self.address)
        return data

    def post_required_data(self, user=None, site=None):
        """Return  post request required data."""
        data = super(
            UrlApiTestCase, self).post_required_data(user, site)
        data.update(self.url_data())
        return data

    def verify_create_url(self, data=None):
        """Generate and verify post request for url creation."""
        data = data or self.post_required_data()
        response, instance = self.verify_create(
            url_name=self.url_list,
            data=data,
            model_class=self.model_class)

        self.assertEqual(instance.address,
                         self.address,
                         "Url.address initialization error")

        return response, instance

    def test_create_url(self):
        self.verify_create_url()

    def test_create_url_partial(self):
        data = self.url_data()
        self.verify_create_url(data=data)

    def test_get_url(self):
        self.verify_get_defaults()

    def test_put_url_partial(self):
        instance = self.create_instance_default()
        data = dict(id=instance.id,
                    address=self.address)
        self.verify_put(self.url_detail, instance, data, self.serializer_class)

    def test_delete_url(self):
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
