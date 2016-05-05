"""
.. module::  django_core_models.social_media.tests.factories
   :synopsis: social_media application factories module.

*social_media* application factories module.
"""
from __future__ import absolute_import
import factory.fuzzy

from django_core_utils.tests.factories import (NamedModelFactory,
                                               VersionedModelFactory)

from .. import models


class EmailTypeModelFactory(NamedModelFactory):
    """Email type model factory class.
    """
    name = "Work"

    class Meta(object):
        """Model meta class."""
        model = models.EmailType


class FormattedNameModelFactory(VersionedModelFactory):
    """Formatted name model factory class.
    """
    name = factory.fuzzy.FuzzyText()

    class Meta(object):
        """Model meta class."""
        model = models.FormattedName


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


class UrlTypeModelFactory(NamedModelFactory):
    """Url type model factory class.
    """
    name = "facebook"

    class Meta(object):
        """Model meta class."""
        model = models.UrlType
