"""
.. module::  model_apps.image.apps
   :synopsis:  Django image application configuration  module.

Django image  application configuration  module.

"""
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ImageConfig(AppConfig):
    """Django's image application configuration class."""
    name = __package__
    verbose_name = _("Image")
