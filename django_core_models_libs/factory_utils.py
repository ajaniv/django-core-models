"""
.. module::  django_core_models.factory_utils
   :synopsis:  django_core factory  utilities  module.

django_core factory utilities  module.

"""


class ISOMixin(object):
    """ISO  mixin class."""
    @classmethod
    def name(cls, n):
        if n >= len(cls.names):
            n = 0
        return cls.names[n]

    @classmethod
    def iso_code(cls, n):
        if n >= len(cls.iso_codes):
            n = 0
        return cls.iso_codes[n]
