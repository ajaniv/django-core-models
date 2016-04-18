"""
.. module::  demographics.models
   :synopsis:  demographics application  models module.

*demographics* application models module.

"""
from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _
from inflection import humanize, pluralize, underscore

from django_core_utils.constants import UNKNOWN
from django_core_utils.models import NamedModel, db_table

_app_label = "demographics"

GENDER_MALE = 'Male'
GENDER_FEMALE = 'Female'
GENDER_UNKNOWN = UNKNOWN
GENDER = (GENDER_MALE, GENDER_FEMALE, GENDER_UNKNOWN)

_gender = "Gender"
_gender_verbose = humanize(underscore(_gender))


class Gender(NamedModel):
    """Gender model class.

    Values may include  "male", "female", "other", "none", "unknown".
    """
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _gender)
        verbose_name = _(humanize(_gender_verbose))
        verbose_name_plural = _(pluralize(humanize(_gender_verbose)))

    @property
    def sex(self):
        return self.name

    @sex.setter
    def sex(self, value):
        self.name = value
