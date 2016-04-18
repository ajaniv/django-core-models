"""
.. module::  model_apps.social_media.apps
   :synopsis:  Django core application configuration  module.

Django social_media  application configuration  module.

"""
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class SocialMediaConfig(AppConfig):
    """Django's social media  application configuration class."""
    name = __package__
    verbose_name = _("Social Media")
