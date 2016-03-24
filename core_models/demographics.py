"""
.. module::  core_models.demographics
   :synopsis:  core_models demographics models module

core_models demographics models module.

"""

from core.models import app_table_name, db_table_name
from core.constants import UNKNOWN
from core.models import NamedModel
from .apps import CoreModelsConfig

_app_label = CoreModelsConfig.name
MALE = 'Male'
FEMALE = 'Female'
GENDER = (MALE, FEMALE, UNKNOWN)

__all__ = [
           'Gender',
           'MALE',
           'FEMALE',
           'GENDER'
           ]


class Gender(NamedModel):
    """Gender model class.

    Values make include  "male", "female", "other", "none", "unknown".
    """
    class Meta(NamedModel.Meta):
        app_label = _app_label
        db_table = app_table_name(_app_label, db_table_name('Gender'))
