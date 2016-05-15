"""
.. module::  social_media.forms
   :synopsis:  Django social_media application forms  module.

Django social_media application forms  module.

"""
from __future__ import absolute_import


from django_core_utils import forms
from python_core_utils.core import dict_merge

from . import models
from . import text


class EmailAdminForm(forms.VersionedModelAdminForm):
    """Formatted name  model admin form  class.
    """
    class Meta(forms.VersionedModelAdminForm.Meta):
        """Form meta class."""
        model = models.Email
        labels = dict_merge(
            forms.VersionedModelAdminForm.Meta.labels,
            text.email_labels)

        help_texts = dict_merge(
            forms.VersionedModelAdminForm.Meta.help_texts,
            text.email_help_texts)


class FormattedNameAdminForm(forms.VersionedModelAdminForm):
    """FormattedName  model admin form  class.
    """
    class Meta(forms.VersionedModelAdminForm.Meta):
        """Form meta class."""
        model = models.FormattedName
        labels = dict_merge(
            forms.VersionedModelAdminForm.Meta.labels,
            text.formatted_name_labels)

        help_texts = dict_merge(
            forms.VersionedModelAdminForm.Meta.help_texts,
            text.formatted_name_help_texts)


class InstantMessagingAdminForm(forms.VersionedModelAdminForm):
    """InstantMessaging model admin form  class.
    """
    address = forms.InstantMessagingField(
        help_text=text.instant_messaging_help_texts["address"])

    class Meta(forms.VersionedModelAdminForm.Meta):
        """Form meta class."""
        model = models.InstantMessaging
        labels = dict_merge(
            forms.VersionedModelAdminForm.Meta.labels,
            text.instant_messaging_labels)

        help_texts = dict_merge(
            forms.VersionedModelAdminForm.Meta.help_texts,
            text.instant_messaging_help_texts)


class NameAdminForm(forms.VersionedModelAdminForm):
    """Name model admin form  class.
    """
    class Meta(forms.VersionedModelAdminForm.Meta):
        """Form meta class."""
        model = models.Name
        labels = dict_merge(
            forms.VersionedModelAdminForm.Meta.labels,
            text.name_labels)

        help_texts = dict_merge(
            forms.VersionedModelAdminForm.Meta.help_texts,
            text.name_help_texts)


class NicknameAdminForm(forms.VersionedModelAdminForm):
    """Nickname model admin form  class.
    """
    class Meta(forms.VersionedModelAdminForm.Meta):
        """Form meta class."""
        model = models.Nickname
        labels = dict_merge(
            forms.VersionedModelAdminForm.Meta.labels,
            text.nickname_labels)

        help_texts = dict_merge(
            forms.VersionedModelAdminForm.Meta.help_texts,
            text.nickname_help_texts)


class PhoneAdminForm(forms.VersionedModelAdminForm):
    """Phone model admin form  class.
    """
    class Meta(forms.VersionedModelAdminForm.Meta):
        """Form meta class."""
        model = models.Phone
        labels = dict_merge(
            forms.VersionedModelAdminForm.Meta.labels,
            text.phone_labels)

        help_texts = dict_merge(
            forms.VersionedModelAdminForm.Meta.help_texts,
            text.phone_help_texts)


class UrlAdminForm(forms.VersionedModelAdminForm):
    """Url model admin form  class.
    """
    class Meta(forms.VersionedModelAdminForm.Meta):
        """Form meta class."""
        model = models.Url
        labels = dict_merge(
            forms.VersionedModelAdminForm.Meta.labels,
            text.url_labels)

        help_texts = dict_merge(
            forms.VersionedModelAdminForm.Meta.help_texts,
            text.url_help_texts)
