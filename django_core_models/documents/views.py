"""
..  module:: django_core_models.documents.views
    :synopsis: django_core_models documents application views  module.

*django_core_models* documents application views  module.
"""
from __future__ import absolute_import

from django_core_utils.views import ObjectListView, ObjectDetailView
from . import models
from . import serializers

class DocumentMixin(object):
    """DocumentMixin mixin class."""
    queryset = models.Document.objects.all()
    serializer_class = serializers.DocumentSerializer


class DocumentList(DocumentMixin, ObjectListView):
    """Class to list Documents, or create a new Document instance."""
    pass


class DocumentDetail(DocumentMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete Document instance.
    """
    pass

class DocumentFormatMixin(object):
    """DocumentFormat mixin class."""
    queryset = models.DocumentFormat.objects.all()
    serializer_class = serializers.DocumentFormatSerializer


class DocumentFormatList(DocumentFormatMixin, ObjectListView):
    """Class to list all DocumentFormat, or create a new DocumentFormat instance."""
    pass


class DocumentFormatDetail(DocumentFormatMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete DocumentFormat instance.
    """
    pass

class DocumentOrientationMixin(object):
    """DocumentOrientation mixin class."""
    queryset = models.DocumentOrientation.objects.all()
    serializer_class = serializers.DocumentOrientationSerializer


class DocumentOrientationList(DocumentOrientationMixin, ObjectListView):
    """Class to list all DocumentOrientation,
     or create a new DocumentOrientation instance."""
    pass


class DocumentOrientationDetail(DocumentOrientationMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete DocumentOrientation instance.
    """
    pass

class DocumentReferenceMixin(object):
    """DocumentReference  mixin class."""
    queryset = models.DocumentReference.objects.all()
    serializer_class = serializers.DocumentReferenceSerializer


class DocumentReferenceList(DocumentReferenceMixin, ObjectListView):
    """Class to list DocumentReference, or create a new Image instance."""
    pass


class DocumentReferenceDetail(DocumentReferenceMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete DocumentReference instance.
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
    """Class to list Images, or create a new Image instance."""
    pass


class ImageDetail(ImageMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete Image instance.
    """
    pass


class ImageReferenceMixin(object):
    """ImageReference  mixin class."""
    queryset = models.ImageReference.objects.all()
    serializer_class = serializers.ImageReferenceSerializer


class ImageReferenceList(ImageReferenceMixin, ObjectListView):
    """Class to list ImageReference, or create a new Image instance."""
    pass


class ImageReferenceDetail(ImageReferenceMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete ImageReference instance.
    """
    pass
