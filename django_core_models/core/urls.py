"""
.. module::  django_core_models.core.urls
   :synopsis:  core application urls module

*core* application urls module.

"""
from __future__ import absolute_import
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^annotations/$', views.AnnotationList.as_view(),
        name="annotation-list"),
    url(r'^annotations/(?P<pk>[0-9]+)/$', views.AnnotationDetail.as_view(),
        name='annotation-detail'),
    url(r'^categories/$', views.CategoryList.as_view(),
        name="category-list"),
    url(r'^categories/(?P<pk>[0-9]+)/$', views.CategoryDetail.as_view(),
        name='category-detail'),
    url(r'^currencies/$', views.CurrencyList.as_view(),
        name='currency-list'),
    url(r'^currencies/(?P<pk>[0-9]+)/$', views.CurrencyDetail.as_view(),
        name='currency-detail'),
]
