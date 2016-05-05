"""
.. module::  django_core_models.locations.urls
   :synopsis:  django_core_models locations application urls module

django_core_models *locations* application urls module.

"""
from __future__ import absolute_import
from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^organization-types/$',
        views.OrganizationTypeList.as_view(),
        name='organization-type-list'),
    url(r'^organization-types/(?P<pk>[0-9]+)/$',
        views.OrganizationTypeDetail.as_view(),
        name='organization-type-detail'),

    url(r'^organizations/$',
        views.OrganizationList.as_view(),
        name='organization-list'),
    url(r'^organizations/(?P<pk>[0-9]+)/$',
        views.OrganizationDetail.as_view(),
        name='organization-detail'),

    url(r'^organization-units/$',
        views.OrganizationUnitList.as_view(),
        name='organization-unit-list'),
    url(r'^organization-units/(?P<pk>[0-9]+)/$',
        views.OrganizationUnitDetail.as_view(),
        name='organization-unit-detail'),

    url(r'^roles/$',
        views.RoleList.as_view(),
        name='role-list'),
    url(r'^roles/(?P<pk>[0-9]+)/$',
        views.RoleDetail.as_view(),
        name='role-detail'),

    url(r'^titles/$',
        views.TitleList.as_view(),
        name='title-list'),
    url(r'^titles/(?P<pk>[0-9]+)/$',
        views.TitleDetail.as_view(),
        name='title-detail'),


]
