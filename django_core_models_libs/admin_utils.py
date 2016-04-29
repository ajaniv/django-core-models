"""
.. module::  django_core_models_libs.admin_utils
   :synopsis:  django_core_models admin utilities  module.

django_core_models admin utilities  module.

"""
iso_list_display = ("id", "get_name", "alias", "iso_code",
                    "version", "update_time", "update_user")

iso_fields = (
    ("name",),
    ("iso_code",),
    ("alias",),
    ("description",),)
