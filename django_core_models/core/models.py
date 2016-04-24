"""
.. module::  core.models
   :synopsis:  core application models module

*core*  application models module.

"""
from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _
from inflection import humanize, pluralize, underscore

from django_core_utils import fields
from django_core_utils.models import NamedModel, OptionalNamedModel, db_table

from .validation import currency_validation

_app_label = "core"
_annotation = "Annotation"
_annotation_verbose = humanize(underscore(_annotation))


class Annotation(OptionalNamedModel):
    """Annotation model class.

    Capture annotations/notes.
    """
    annotation = fields.annotation_field()

    class Meta(OptionalNamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _annotation)
        verbose_name = _(_annotation_verbose)
        verbose_name_plural = _(pluralize(_annotation_verbose))


_category = "Category"
_category_verbose = humanize(underscore(_category))


class Category(NamedModel):
    """Contact category model class.

    Allows classification of contacts, other abstractions.
    Sample values may include "industry", "travel", "unknown".
    """

    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _category)
        verbose_name = _(_category_verbose)
        verbose_name_plural = _(pluralize(_category_verbose))

_currency = "Currency"
_currency_verbose = humanize(underscore(_currency))


class Currency(NamedModel):
    """Currency model class.

    """
    iso_code = fields.char_field(max_length=3, unique=True)

    class Meta(NamedModel.Meta):
        """Model meta class declaration."""
        app_label = _app_label
        db_table = db_table(_app_label, _currency)
        verbose_name = _(_currency_verbose)
        verbose_name_plural = _(pluralize(_currency_verbose))

    def clean(self):
        """Perform cross field validation.
        """
        super(Currency, self).clean()
        currency_validation(self)
