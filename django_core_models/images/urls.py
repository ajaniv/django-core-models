"""
.. module::  django_core_models.images.urls
   :synopsis:  django_core_models images application urls module

django_core_models *images* application urls module.

"""
from __future__ import absolute_import
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^document-orientations/$',
        views.DocumentOrientationList.as_view(),
        name="document-orientation-list"),
    url(r'^document-orientations/(?P<pk>[0-9]+)/$',
        views.DocumentOrientationDetail.as_view(),
        name='document-orientation-detail'),

    url(r'^image-formats/$',
        views.ImageFormatList.as_view(),
        name="image-format-list"),
    url(r'^image-formats/(?P<pk>[0-9]+)/$',
        views.ImageFormatDetail.as_view(),
        name='image-format-detail'),

    url(r'^images/$',
        views.ImageList.as_view(),
        name='image-list'),
    url(r'^images/(?P<pk>[0-9]+)/$',
        views.ImageDetail.as_view(),
        name='image-detail'),

    url(r'^image-references/$',
        views.ImageReferenceList.as_view(),
        name='image-reference-list'),
    url(r'^image-references/(?P<pk>[0-9]+)/$',
        views.ImageReferenceDetail.as_view(),
        name='image-reference-detail'),

]
