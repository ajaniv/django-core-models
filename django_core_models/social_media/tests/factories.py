"""
.. module::  django_core_models.social_media.tests.factories
   :synopsis: social_media application factories module.

*social_media* application factories module.
"""
from __future__ import absolute_import
import functools
import random
import factory.fuzzy

from django_core_utils.tests.factories import (NamedModelFactory,
                                               VersionedModelFactory)

from .. import models


class EmailModelFactory(VersionedModelFactory):
    """Email model factory class.
    """
    address = factory.Sequence(lambda n: 'person{0}@example.com'.format(n))

    class Meta(object):
        """Model meta class."""
        model = models.Email


class EmailTypeModelFactory(NamedModelFactory):
    """Email type model factory class.
    """
    name = "Work"

    class Meta(object):
        """Model meta class."""
        model = models.EmailType


class SimpleNameModelFactory(VersionedModelFactory):
    """SimpleName model factory class."""
    name = factory.fuzzy.FuzzyText()

    class Meta(object):
        """Model meta class."""
        model = models.SimpleName
        abstract = True


class FormattedNameModelFactory(SimpleNameModelFactory):
    """Formatted name model factory class.
    """

    class Meta(object):
        """Model meta class."""
        model = models.FormattedName


class NicknameModelFactory(SimpleNameModelFactory):
    """Nickname model factory class.
    """

    class Meta(object):
        """Model meta class."""
        model = models.Nickname


class GroupModelFactory(NamedModelFactory):
    """Group model factory class.
    """
    name = "Organizers"

    class Meta(object):
        """Model meta class."""
        model = models.Group


class InstantMessagingTypeModelFactory(NamedModelFactory):
    """Instant messaging type model factory class.
    """
    name = "slack"

    class Meta(object):
        """Model meta class."""
        model = models.InstantMessagingType


class LogoTypeModelFactory(NamedModelFactory):
    """Logo type model factory class.
    """
    name = "business"

    class Meta(object):
        """Model meta class."""
        model = models.LogoType


class NameModelFactory(VersionedModelFactory):
    """Name model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = models.Name

    family_name = factory.fuzzy.FuzzyText()
    given_name = factory.fuzzy.FuzzyText()


class NicknameTypeModelFactory(NamedModelFactory):
    """Nickname type model factory class.
    """
    name = "personal"

    class Meta(object):
        """Model meta class."""
        model = models.NicknameType


def random_phone_number(n=None):
    """Generate a randam phone number"""
    # TODO: make more robust

    digit_gen = functools.partial(random.randint, 0, 9)
    digits = [str(digit_gen()) for _ in range(4)]
    return "+1415555{}".format("".join(digits))


class PhoneModelFactory(VersionedModelFactory):
    """Phone model factory class.
    """
    number = factory.Sequence(
        lambda n: random_phone_number(n))

    class Meta(object):
        """Model meta class."""
        model = models.Phone


class PhoneTypeModelFactory(NamedModelFactory):
    """Phone type model factory class.
    """
    name = "work"

    class Meta(object):
        """Model meta class."""
        model = models.PhoneType


class PhotoTypeModelFactory(NamedModelFactory):
    """Photo type model factory class.
    """
    name = "mobile"

    class Meta(object):
        """Model meta class."""
        model = models.PhotoType


def random_url(n=None):
    """Generate a randam url """
    n = n or random.randint(0, 1000)
    return "http://www.dummy-{n}.com".format(n=n)


class UrlModelFactory(VersionedModelFactory):
    """Url model factory class.
    """
    address = factory.Sequence(lambda n: random_url(n))

    class Meta(object):
        """Model meta class."""
        model = models.Url


class UrlTypeModelFactory(NamedModelFactory):
    """Url type model factory class.
    """
    name = "facebook"

    class Meta(object):
        """Model meta class."""
        model = models.UrlType
