"""
..  module:: django_core_models.core.views
    :synopsis: Django django_core_models core application views  module.

Django django_core_models core application views  module.
"""
from __future__ import absolute_import
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django_core_utils.views import instance_list, instance_detail, ObjectListView, ObjectDetailView
from . import models
from . import serializers


@api_view(['GET', 'POST'])
def category_list(request, content_format=None):
    """
    List all categories, or create a new category instance.
    """
    return instance_list(request, models.Category,
                         serializers.CategorySerializer,
                         format)


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, pk, content_format=None):
    """
    Retrieve, update or delete a category.
    """
    return instance_detail(request, pk, models.Category,
                           serializers.CategorySerializer,
                           format)


class AnnotationMixin(object):
    """Annotation mixin class."""
    queryset = models.Annotation.objects.all()
    serializer_class = serializers.AnnotationSerializer


class AnnotationList(AnnotationMixin, ObjectListView):
    """Class to list all annotations, or create a new annotation instance."""
    pass


class AnnotationDetail(AnnotationMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete annotation instance.
    """
    pass


class CategoryMixin(object):
    """Category mixin class."""
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class CategoryList(CategoryMixin, ObjectListView):
    """Class to list all currencies, or create a new category instance."""
    pass


class CategoryDetail(CategoryMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete category instance.
    """
    pass


class CurrencyMixin(object):
    """Currency mixin class."""
    queryset = models.Currency.objects.all()
    serializer_class = serializers.CurrencySerializer


class CurrencyList(CurrencyMixin, ObjectListView):
    """Class to list all currencies, or create a new currency instance."""
    pass


class CurrencyDetail(CurrencyMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete currency instance.
    """
    pass
