"""
.. module::  django_core_models.documents.urls
   :synopsis:  django_core_models documents application urls module

django_core_models *documents* application urls module.

"""
from __future__ import absolute_import
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^documents/$',
        views.DocumentList.as_view(),
        name='document-list'),
    url(r'^documents/(?P<pk>[0-9]+)/$',
        views.DocumentDetail.as_view(),
        name='document-detail'),
    
    url(r'^document-formats/$',
        views.DocumentFormatList.as_view(),
        name="document-format-list"),
    url(r'^document-formats/(?P<pk>[0-9]+)/$',
        views.DocumentFormatDetail.as_view(),
        name='document-format-detail'),
               
    url(r'^document-references/$',
        views.DocumentReferenceList.as_view(),
        name='document-reference-list'),
    url(r'^document-references/(?P<pk>[0-9]+)/$',
        views.DocumentReferenceDetail.as_view(),
        name='document-reference-detail'),
    
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
