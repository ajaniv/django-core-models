"""
..  module:: django_core_models.social_media.views
    :synopsis: django_core_models social_media application views  module.

*django_core_models* social_media application views  module.
"""
from __future__ import absolute_import

from django_core_utils.views import ObjectListView, ObjectDetailView
from . import models
from . import serializers


class EmailMixin(object):
    """Email mixin class."""
    queryset = models.Email.objects.all()
    serializer_class = serializers.EmailSerializer


class EmailList(EmailMixin, ObjectListView):
    """Class to list all Email instances,
     or create  new Email instance."""
    pass


class EmailDetail(EmailMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete Email instance.
    """
    pass


class EmailTypeMixin(object):
    """EmailType mixin class."""
    queryset = models.EmailType.objects.all()
    serializer_class = serializers.EmailTypeSerializer


class EmailTypeList(EmailTypeMixin, ObjectListView):
    """Class to list all EmailType instances,
     or create  new EmailType instance."""
    pass


class EmailTypeDetail(EmailTypeMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete EmailType instance.
    """
    pass


class FormattedNameMixin(object):
    """FormattedName mixin class."""
    queryset = models.FormattedName.objects.all()
    serializer_class = serializers.FormattedNameSerializer


class FormattedNameList(FormattedNameMixin, ObjectListView):
    """Class to list all FormattedName instances,
    or create new FormattedName instance."""
    pass


class FormattedNameDetail(FormattedNameMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete FormattedName instance.
    """
    pass


class GroupMixin(object):
    """Group mixin class."""
    queryset = models.Group.objects.all()
    serializer_class = serializers.GroupSerializer


class GroupList(GroupMixin, ObjectListView):
    """Class to list all Group instances,
    or create new Group instance."""
    pass


class GroupDetail(GroupMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete Group instance.
    """
    pass


class InstantMessagingMixin(object):
    """InstantMessaging mixin class."""
    queryset = models.InstantMessaging.objects.all()
    serializer_class = serializers.InstantMessagingSerializer


class InstantMessagingList(InstantMessagingMixin, ObjectListView):
    """Class to list all InstantMessaging instances,
     or create  new InstantMessaging instance."""
    pass


class InstantMessagingDetail(InstantMessagingMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete InstantMessaging instance.
    """
    pass


class InstantMessagingTypeMixin(object):
    """InstantMessagingType mixin class."""
    queryset = models.InstantMessagingType.objects.all()
    serializer_class = serializers.InstantMessagingTypeSerializer


class InstantMessagingTypeList(InstantMessagingTypeMixin, ObjectListView):
    """Class to list all InstantMessagingType instances,
     or create new InstantMessagingType instance."""
    pass


class InstantMessagingTypeDetail(InstantMessagingTypeMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete InstantMessagingType instance.
    """
    pass


class LogoTypeMixin(object):
    """Title mixin class."""
    queryset = models.LogoType.objects.all()
    serializer_class = serializers.LogoTypeSerializer


class LogoTypeList(LogoTypeMixin, ObjectListView):
    """Class to list all LogoType instances,
     or create new LogoType instance."""
    pass


class LogoTypeDetail(LogoTypeMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete LogoType instance.
    """
    pass


class NameMixin(object):
    """Name mixin class."""
    queryset = models.Name.objects.all()
    serializer_class = serializers.NameSerializer


class NameList(NameMixin, ObjectListView):
    """Class to list all Name instances,
     or create new LogoType instance."""
    pass


class NameDetail(NameMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete Name instance.
    """
    pass


class NicknameMixin(object):
    """Nickname mixin class."""
    queryset = models.Nickname.objects.all()
    serializer_class = serializers.NicknameSerializer


class NicknameList(NicknameMixin, ObjectListView):
    """Class to list all Nickname instances,
    or create new Nickname instance."""
    pass


class NicknameDetail(NicknameMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete Nickname instance.
    """
    pass


class NicknameTypeMixin(object):
    """NicknameType mixin class."""
    queryset = models.NicknameType.objects.all()
    serializer_class = serializers.NicknameTypeSerializer


class NicknameTypeList(NicknameTypeMixin, ObjectListView):
    """Class to list all NicknameType instances,
     or create new NicknameType instance."""
    pass


class NicknameTypeDetail(NicknameTypeMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete NicknameType instance.
    """
    pass


class PhoneMixin(object):
    """Phone mixin class."""
    queryset = models.Phone.objects.all()
    serializer_class = serializers.PhoneSerializer


class PhoneList(PhoneMixin, ObjectListView):
    """Class to list all Phone instances,
     or create  new Phone instance."""
    pass


class PhoneDetail(PhoneMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete Phone instance.
    """
    pass


class PhoneTypeMixin(object):
    """PhoneType mixin class."""
    queryset = models.PhoneType.objects.all()
    serializer_class = serializers.PhoneTypeSerializer


class PhoneTypeList(PhoneTypeMixin, ObjectListView):
    """Class to list all PhoneType instances,
     or create new PhoneType instance."""
    pass


class PhoneTypeDetail(PhoneTypeMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete PhoneType instance.
    """
    pass


class PhotoTypeMixin(object):
    """PhotoType mixin class."""
    queryset = models.PhotoType.objects.all()
    serializer_class = serializers.PhotoTypeSerializer


class PhotoTypeList(PhotoTypeMixin, ObjectListView):
    """Class to list all PhotoType instances,
     or create new PhotoType instance."""
    pass


class PhotoTypeDetail(PhotoTypeMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete PhotoType instance.
    """
    pass


class UrlMixin(object):
    """Url mixin class."""
    queryset = models.Url.objects.all()
    serializer_class = serializers.UrlSerializer


class UrlList(UrlMixin, ObjectListView):
    """Class to list all Url instances,
     or create  new Url instance."""
    pass


class UrlDetail(UrlMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete Url instance.
    """
    pass


class UrlTypeMixin(object):
    """UrlType mixin class."""
    queryset = models.UrlType.objects.all()
    serializer_class = serializers.UrlTypeSerializer


class UrlTypeList(UrlTypeMixin, ObjectListView):
    """Class to list all UrlType instances,
     or create new UrlType instance."""
    pass


class UrlTypeDetail(UrlTypeMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete UrlType instance.
    """
    pass
