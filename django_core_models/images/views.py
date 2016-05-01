"""
..  module:: django_core_models.images.views
    :synopsis: django_core_models images application views  module.

*django_core_models* images application views  module.
"""
from __future__ import absolute_import

from django_core_utils.views import ObjectListView, ObjectDetailView
from . import models
from . import serializers


class DocumentOrientationMixin(object):
    """DocumentOrientation mixin class."""
    queryset = models.DocumentOrientation.objects.all()
    serializer_class = serializers.DocumentOrientationSerializer


class DocumentOrientationList(DocumentOrientationMixin, ObjectListView):
    """Class to list all DocumentOrientation, or create a new DocumentOrientation instance."""
    pass


class DocumentOrientationDetail(DocumentOrientationMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete DocumentOrientation instance.
    """
    pass


class ImageFormatMixin(object):
    """ImageFormat mixin class."""
    queryset = models.ImageFormat.objects.all()
    serializer_class = serializers.ImageFormatSerializer


class ImageFormatList(ImageFormatMixin, ObjectListView):
    """Class to list all ImageFormat, or create a new ImageFormat instance."""
    pass


class ImageFormatDetail(ImageFormatMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete ImageFormat instance.
    """
    pass


class ImageMixin(object):
    """ImageMixin mixin class."""
    queryset = models.Image.objects.all()
    serializer_class = serializers.ImageSerializer


class ImageList(ImageMixin, ObjectListView):
    """Class to list Image ages, or create a new Image instance."""
    pass


class ImageDetail(ImageMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete Image instance.
    """
    pass
