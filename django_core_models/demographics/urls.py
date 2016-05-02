"""
.. module::  django_core_models.core.urls
   :synopsis:  django_core_models core application urls module

django_core_models *core* application urls module.

"""
from __future__ import absolute_import
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^ages/$',
        views.AgeList.as_view(),
        name="age-list"),
    url(r'^ages/(?P<pk>[0-9]+)/$',
        views.AgeDetail.as_view(),
        name='age-detail'),

    url(r'^child-count/$',
        views.ChildCountList.as_view(),
        name="child-count-list"),
    url(r'^child-count/(?P<pk>[0-9]+)/$',
        views.ChildCountDetail.as_view(),
        name='child-count-detail'),

    url(r'^demographic-regions/$',
        views.DemographicRegionList.as_view(),
        name='demographic-region-list'),
    url(r'^demographic-region/(?P<pk>[0-9]+)/$',
        views.DemographicRegionDetail.as_view(),
        name='demographic-region-detail'),

    url(r'^education-levels/$',
        views.EducationLevelList.as_view(),
        name='education-level-list'),
    url(r'^education-level/(?P<pk>[0-9]+)/$',
        views.EducationLevelDetail.as_view(),
        name='education-level-detail'),

    url(r'^ethnicities/$',
        views.EthnicityList.as_view(),
        name='ethnicity-list'),
    url(r'^ethnicities/(?P<pk>[0-9]+)/$',
        views.EthnicityDetail.as_view(),
        name='ethnicity-detail'),

    url(r'^gender/$',
        views.GenderList.as_view(),
        name='gender-list'),
    url(r'^gender/(?P<pk>[0-9]+)/$',
        views.GenderDetail.as_view(),
        name='gender-detail'),

    url(r'^household-size/$',
        views.HouseholdSizeList.as_view(),
        name='household-size-list'),
    url(r'^household-size/(?P<pk>[0-9]+)/$',
        views.HouseholdSizeDetail.as_view(),
        name='household-size-detail'),

    url(r'^incomes/$',
        views.IncomeList.as_view(),
        name='income-list'),
    url(r'^income/(?P<pk>[0-9]+)/$',
        views.IncomeDetail.as_view(),
        name='income-detail'),
]
