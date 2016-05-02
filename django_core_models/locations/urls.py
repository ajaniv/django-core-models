"""
.. module::  django_core_models.locations.urls
   :synopsis:  django_core_models locations application urls module

django_core_models *locations* application urls module.

"""
from __future__ import absolute_import
from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^addresses/$',
        views.AddressList.as_view(),
        name='address-list'),
    url(r'^addresses/(?P<pk>[0-9]+)/$',
        views.AddressDetail.as_view(),
        name='address-detail'),

    url(r'^address-types/$',
        views.AddressTypeList.as_view(),
        name='address-type-list'),
    url(r'^address-types/(?P<pk>[0-9]+)/$',
        views.AddressTypeDetail.as_view(),
        name='address-type-detail'),

    url(r'^cities/$',
        views.CityList.as_view(),
        name='city-list'),
    url(r'^cities/(?P<pk>[0-9]+)/$',
        views.CityDetail.as_view(),
        name='city-detail'),

    url(r'^countries/$',
        views.CountryList.as_view(),
        name='country-list'),
    url(r'^countries/(?P<pk>[0-9]+)/$',
        views.CountryDetail.as_view(),
        name='country-detail'),

    url(r'^distance-units/$', views.DistanceUnitList.as_view(),
        name='distance-unit-list'),
    url(r'^distance-units/(?P<pk>[0-9]+)/$',
        views.DistanceUnitDetail.as_view(),
        name='distance-unit-detail'),

    url(r'^geographic-locations/$',
        views.GeographicLocationList.as_view(),
        name='geographic-location-list'),
    url(r'^geographic-locations/(?P<pk>[0-9]+)/$',
        views.GeographicLocationDetail.as_view(),
        name='geographic-location-detail'),

    url(r'^geographic-location-types/$',
        views.GeographicLocationTypeList.as_view(),
        name='geographic-location-type-list'),
    url(r'^geographic-location-types/(?P<pk>[0-9]+)/$',
        views.GeographicLocationTypeDetail.as_view(),
        name='geographic-location-type-detail'),

    url(r'^language-types/$',
        views.LanguageTypeList.as_view(),
        name='language-type-list'),
    url(r'^language-types/(?P<pk>[0-9]+)/$',
        views.LanguageTypeDetail.as_view(),
        name='language-type-detail'),

    url(r'^languages/$',
        views.LanguageList.as_view(),
        name='language-list'),
    url(r'^languages/(?P<pk>[0-9]+)/$',
        views.LanguageDetail.as_view(),
        name='language-detail'),

    url(r'^timezone-types/$',
        views.TimezoneTypeList.as_view(),
        name='timezone-type-list'),
    url(r'^timezone-types/(?P<pk>[0-9]+)/$',
        views.TimezoneTypeDetail.as_view(),
        name='timezone-type-detail'),

    url(r'^timezones/$',
        views.TimezoneList.as_view(),
        name='timezone-list'),
    url(r'^timezones/(?P<pk>[0-9]+)/$',
        views.TimezoneDetail.as_view(),
        name='timezone-detail'),

    url(r'^proninces/$',
        views.ProvinceList.as_view(),
        name='province-list'),
    url(r'^proninces/(?P<pk>[0-9]+)/$',
        views.ProvinceDetail.as_view(),
        name='province-detail'),

    url(r'^states/$',
        views.StateList.as_view(),
        name='state-list'),
    url(r'^states/(?P<pk>[0-9]+)/$',
        views.StateDetail.as_view(),
        name='state-detail'),

]
