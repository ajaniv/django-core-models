"""
..  module:: image.text
    :synopsis: Django image application text  module.

Django image application text  module.
"""
from django.utils.translation import ugettext_lazy as _

# flake8: noqa
# required because of pep8 regression in ignoring disable of E123

image_labels = {
    "image": _("Image"),
    "image_format": _("Format"),
    "image_orientation": _("Orientation"),
    "height": _("Height"),
    "width": _("Width"),
    }

image_help_texts = {
    "image": _("Image contents."),
    "image_format": _("Image format."),
    "image_orientation": _("Image orientation."),
    "height": _("Image height."),
    "width": _("Image width."),
    }

image_reference_labels = {
    "image": _("Image"),
    "url": _("Url"),
    }

image_reference_help_texts = {
    "image": _("Image."),
    "image_url": _("Image url."),
    }
