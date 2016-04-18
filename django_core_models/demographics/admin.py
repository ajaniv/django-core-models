"""
.. module::  demographics.admin
   :synopsis:  Django demographics application admin  module.

Django demographics application admin  module.

"""
from __future__ import absolute_import

from django_core_utils.admin import (NamedModelAdmin, admin_site_register,
                                     named_model_admin_class_attrs)
from python_core_utils.core import class_name

from .models import Gender

_named_classes = (Gender,)

for clasz in _named_classes:
    admin_site_register(
        clasz,
        (NamedModelAdmin,),
        named_model_admin_class_attrs(class_name(clasz)))
