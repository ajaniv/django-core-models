"""
.. module::  django_core_models.views
   :synopsis:  django_core_models project views module.

*django_core_models* project views module.

"""

from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def api_root(request, content_format=None):
    return Response({
        'categories': reverse('category-list', request=request,
                              format=content_format),
        'currencies': reverse('currency-list', request=request,
                              format=content_format),
        'users': reverse('user-list', request=request,
                         format=content_format),
    })
