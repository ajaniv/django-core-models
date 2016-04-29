"""
.. module::  django_core_models.urls
   :synopsis:  django_core_models project urls module.

*django_core_models* project urls module.

"""
from __future__ import absolute_import
from django.conf.urls import url
from django_core_utils.views import UserList, UserDetail
from . import views

urlpatterns = [
    url(r'^api_root/$', views.api_root, name='api-root'),
    url(r'^users/$', UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view(), name='user-detail'),
]
