"""
.. module::  django_core_models.social_media.urls
   :synopsis:  django_core_models social_media application urls module

django_core_models *social_media* application urls module.

"""
from __future__ import absolute_import
from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'email-types/$',
        views.EmailTypeList.as_view(),
        name='email-type-list'),
    url(r'^email-types/(?P<pk>[0-9]+)/$',
        views.EmailTypeDetail.as_view(),
        name='email-type-detail'),

    url(r'emails/$',
        views.EmailList.as_view(),
        name='email-list'),
    url(r'^emails/(?P<pk>[0-9]+)/$',
        views.EmailDetail.as_view(),
        name='email-detail'),

    url(r'^formatted-names/$',
        views.FormattedNameList.as_view(),
        name='formatted-name-list'),
    url(r'^formatted-names/(?P<pk>[0-9]+)/$',
        views.FormattedNameDetail.as_view(),
        name='formatted-name-detail'),

    url(r'^groups/$',
        views.GroupList.as_view(),
        name='group-list'),
    url(r'^groups/(?P<pk>[0-9]+)/$',
        views.GroupDetail.as_view(),
        name='group-detail'),

    url(r'^instant-messaging/$',
        views.InstantMessagingList.as_view(),
        name='instant-messaging-list'),
    url(r'^instant-messaging/(?P<pk>[0-9]+)/$',
        views.InstantMessagingDetail.as_view(),
        name='instant-messaging-detail'),

    url(r'^instant-messaging-types/$',
        views.InstantMessagingTypeList.as_view(),
        name='instant-messaging-type-list'),
    url(r'^instant-messaging-types/(?P<pk>[0-9]+)/$',
        views.InstantMessagingTypeDetail.as_view(),
        name='instant-messaging-type-detail'),

    url(r'^logo-types/$',
        views.LogoTypeList.as_view(),
        name='logo-type-list'),
    url(r'^logo-types/(?P<pk>[0-9]+)/$',
        views.LogoTypeDetail.as_view(),
        name='logo-type-detail'),

    url(r'^names/$',
        views.NameList.as_view(),
        name='name-list'),
    url(r'^names/(?P<pk>[0-9]+)/$',
        views.NameDetail.as_view(),
        name='name-detail'),

    url(r'^nicknames/$',
        views.NicknameList.as_view(),
        name='nickname-list'),
    url(r'^nicknames/(?P<pk>[0-9]+)/$',
        views.NicknameDetail.as_view(),
        name='nickname-detail'),

    url(r'^nickname-types/$',
        views.NicknameTypeList.as_view(),
        name='nickname-type-list'),
    url(r'^nickname-types/(?P<pk>[0-9]+)/$',
        views.NicknameTypeDetail.as_view(),
        name='nickname-type-detail'),

    url(r'phones/$',
        views.PhoneList.as_view(),
        name='phone-list'),
    url(r'^phones/(?P<pk>[0-9]+)/$',
        views.PhoneDetail.as_view(),
        name='phone-detail'),

    url(r'^phone-types/$',
        views.PhoneTypeList.as_view(),
        name='phone-type-list'),
    url(r'^phone-types/(?P<pk>[0-9]+)/$',
        views.PhoneTypeDetail.as_view(),
        name='phone-type-detail'),

    url(r'^photo-types/$',
        views.PhotoTypeList.as_view(),
        name='photo-type-list'),
    url(r'^photo-types/(?P<pk>[0-9]+)/$',
        views.PhotoTypeDetail.as_view(),
        name='photo-type-detail'),

    url(r'urls/$',
        views.UrlList.as_view(),
        name='url-list'),
    url(r'^urls/(?P<pk>[0-9]+)/$',
        views.UrlDetail.as_view(),
        name='url-detail'),

    url(r'^url-types/$',
        views.UrlTypeList.as_view(),
        name='url-type-list'),
    url(r'^url-types/(?P<pk>[0-9]+)/$',
        views.UrlTypeDetail.as_view(),
        name='url-type-detail'),


]
