"""
.. module::  core_models.demographics
   :synopsis:  core_models demographics models module

*core_models* demographics models module.

"""
from __future__ import absolute_import

from core_utils.constants import UNKNOWN
from core_utils.models import NamedModel, db_table

from ..apps import CoreModelsConfig

_app_label = CoreModelsConfig.name

MALE = 'Male'
FEMALE = 'Female'
GENDER = (MALE, FEMALE, UNKNOWN)


class Gender(NamedModel):
    """Gender model class.

    Values may include  "male", "female", "other", "none", "unknown".
    """
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, 'Gender')

    @property
    def sex(self):
        return self.name

    @sex.setter
    def sex(self, value):
        self.name = value
