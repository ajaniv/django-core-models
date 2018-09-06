"""
.. module::  django_core_models.views
   :synopsis:  django_core_models project views module.

*django_core_models* project views module.

"""
import collections
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes


def core_urls(request, content_format):
    """Return core application end points."""
    return {
        'annotations': reverse(
            'annotation-list', request=request, format=content_format),
        'categories': reverse(
            'category-list', request=request, format=content_format),
        'currencies': reverse(
            'currency-list', request=request, format=content_format),
    }


def demographics_urls(request, content_format):
    """Return demographics application end points."""
    return {
        'ages': reverse(
            'age-list', request=request, format=content_format),
        'child-count': reverse(
            'child-count-list', request=request, format=content_format),
        'demographic-regions': reverse(
            'demographic-region-list', request=request, format=content_format),
        'education-levels': reverse(
            'education-level-list', request=request, format=content_format),
        'ethnicities': reverse(
            'ethnicity-list', request=request, format=content_format),
        'gender': reverse(
            'gender-list', request=request, format=content_format),
        'household-size': reverse(
            'household-size-list', request=request, format=content_format),
        'incomes': reverse(
            'income-list', request=request, format=content_format),
    }


def documents_urls(request, content_format):
    """Return documents application end points."""
    return {
        'document-orientations': reverse(
            'document-orientation-list',
            request=request,
            format=content_format),
        'image-formats': reverse(
            'image-format-list', request=request, format=content_format),
        'images': reverse(
            'image-list', request=request, format=content_format),
    }


def locations_urls(request, content_format):
    """Return locations application end points."""
    return {
        'address-types': reverse(
            'address-type-list', request=request, format=content_format),
        'addresses': reverse(
            'address-list', request=request, format=content_format),
        'cities': reverse(
            'city-list', request=request, format=content_format),
        'countries': reverse(
            'country-list',
            request=request, format=content_format),
        'distance-units': reverse(
            'distance-unit-list', request=request, format=content_format),
        'geographic-location-types': reverse(
            'geographic-location-type-list',
            request=request,
            format=content_format),
        'geographic-location': reverse(
            'geographic-location-list',
            request=request,
            format=content_format),
        'language-types': reverse(
            'language-type-list', request=request, format=content_format),
        'languages': reverse(
            'language-list', request=request, format=content_format),
        'timezone-types': reverse(
            'timezone-type-list', request=request, format=content_format),
        'timezones': reverse(
            'timezone-list', request=request, format=content_format),
        'provinces': reverse(
            'province-list', request=request, format=content_format),
        'states': reverse(
            'state-list', request=request, format=content_format),
    }


def organizations_urls(request, content_format):
    """Return organizations application  end points."""

    return {
        'organization-types': reverse(
            'organization-type-list', request=request, format=content_format),
        'organizations': reverse(
            'organization-list', request=request, format=content_format),
        'organization-units': reverse(
            'organization-unit-list', request=request, format=content_format),
        'roles': reverse(
            'role-list', request=request, format=content_format),
        'titles': reverse(
            'title-list', request=request, format=content_format),

    }


def social_media_urls(request, content_format):
    """Return social media application  end points."""

    return {
        'email-types': reverse(
            'email-type-list', request=request, format=content_format),
        'formatted-names': reverse(
            'formatted-name-list', request=request, format=content_format),
        'groups': reverse(
            'group-list', request=request, format=content_format),
        'instant-messaging-types': reverse(
            'instant-messaging-type-list',
            request=request,
            format=content_format),
        'logo-types': reverse(
            'logo-type-list', request=request, format=content_format),
        'names': reverse(
            'name-list', request=request, format=content_format),
        'nickname-types': reverse(
            'nickname-type-list', request=request, format=content_format),
        'phone-types': reverse(
            'phone-type-list', request=request, format=content_format),
        'photo-types': reverse(
            'photo-type-list', request=request, format=content_format),
        'url-types': reverse(
            'url-type-list', request=request, format=content_format),

    }


def root_urls(request, content_format):
    """Return root end points."""

    return {
        'users': reverse(
            'user-list', request=request, format=content_format),
    }


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def api_root(request, content_format=None):
    end_points = {}
    url_functions = (core_urls, demographics_urls, documents_urls,
                     locations_urls, organizations_urls, social_media_urls,
                     root_urls)
    for url_function in url_functions:
        end_points.update(url_function(request, content_format))
    return Response(collections.OrderedDict(sorted(end_points.items())))
