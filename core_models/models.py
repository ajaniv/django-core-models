"""
.. module::  core_models.models
   :synopsis:  core_models models module

core_models models module.

"""

from core.models import app_table_name, db_table_name
from core.models import VersionedModel, NamedModel
from core import fields

from .demographics import *  # @UnusedWildImport
from .image import *  # @UnusedWildImport
from .location import *  # @UnusedWildImport
from .organization import *  # @UnusedWildImport
from .social_media import *  # @UnusedWildImport

from .apps import CoreModelsConfig

_app_label = CoreModelsConfig.name


class Annotation(VersionedModel):
    """Annotation model class.

    Capture annotations/notes.
    """
    class Meta(VersionedModel.Meta):
        app_label = _app_label
        db_table = app_table_name(_app_label, db_table_name("Title"))
    annotation = fields.annotation_field()


class Category(NamedModel):
    """Contact category model class.

    Allows classification of contacts.
    Sample values may include "industry", "travel", "unknown".
    """
    # @TODO: what are some of the possible instance messaging types?
    class Meta(NamedModel.Meta):
        app_label = _app_label
        db_table = app_table_name(_app_label,
                                  db_table_name("Category"))
