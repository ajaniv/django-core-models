"""
.. module::  core.models
   :synopsis:  core application models module

*core*  application models module.

"""
from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _
from inflection import humanize, pluralize, underscore

from django_core_utils import fields
from django_core_utils.models import NamedModel, VersionedModel, db_table

_app_label = "core"
_annotation = "Annotation"
_annotation_verbose = humanize(underscore(_annotation))


class Annotation(VersionedModel):
    """Annotation model class.

    Capture annotations/notes.
    """
    annotation = fields.annotation_field()

    class Meta(VersionedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _annotation)
        verbose_name = _(_annotation_verbose)
        verbose_name_plural = _(pluralize(_annotation_verbose))


_category = "Category"
_category_verbose = humanize(underscore(_category))


class Category(NamedModel):
    """Contact category model class.

    Allows classification of contacts.
    Sample values may include "industry", "travel", "unknown".
    """

    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _category)
        verbose_name = _(_category_verbose)
        verbose_name_plural = _(pluralize(_category_verbose))
