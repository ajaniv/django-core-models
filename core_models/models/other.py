"""
.. module::  core_models.models
   :synopsis:  core_models models module

core_models models module.

"""
from __future__ import absolute_import

from core_utils import fields
from core_utils.models import NamedModel, VersionedModel, db_table

from ..apps import CoreModelsConfig

_app_label = CoreModelsConfig.name


class Annotation(VersionedModel):
    """Annotation model class.

    Capture annotations/notes.
    """
    annotation = fields.annotation_field()

    class Meta(VersionedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, "Annotation")


class Category(NamedModel):
    """Contact category model class.

    Allows classification of contacts.
    Sample values may include "industry", "travel", "unknown".
    """
    # @TODO: what are some of the possible instance messaging types?
    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, "Category")
