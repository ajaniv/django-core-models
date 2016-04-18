"""
.. module::  model_apps.organization.forms
   :synopsis:  Django organization application forms  module.

Django organization application forms  module.

"""
from __future__ import absolute_import

from utils.core import dict_merge

from core_utils import forms

from .models import Organization, OrganizationUnit
from .text import (organization_help_texts, organization_labels,
                   organization_unit_help_texts, organization_unit_labels)


class OrganizationAdminForm(forms.NamedModelAdminForm):
    """Organization  model admin form  class.
    """
    class Meta(forms.NamedModelAdminForm.Meta):
        """Form meta class."""
        model = Organization
        labels = dict_merge(
            forms.NamedModelAdminForm.Meta.labels,
            organization_labels)

        help_texts = dict_merge(
            forms.NamedModelAdminForm.Meta.help_texts,
            organization_help_texts)


class OrganizationUnitAdminForm(forms.NamedModelAdminForm):
    """Organization unit model admin form  class.
    """
    class Meta(forms.NamedModelAdminForm.Meta):
        """Form meta class."""
        model = OrganizationUnit
        labels = dict_merge(
            forms.NamedModelAdminForm.Meta.labels,
            organization_unit_labels)

        help_texts = dict_merge(
            forms.NamedModelAdminForm.Meta.help_texts,
            organization_unit_help_texts)
