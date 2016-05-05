"""
.. module::  django_core_models.organizations.tests.factories
   :synopsis: organizations application factories module.

*organizations* application factories module.
"""
from __future__ import absolute_import
import factory

from django_core_utils.tests.factories import NamedModelFactory

from .. import models


class OrganizationTypeModelFactory(NamedModelFactory):
    """Organization type model factory class.
    """
    name = "Manufacturing"

    class Meta(object):
        """Model meta class."""
        model = models.OrganizationType


class OrganizationModelFactory(NamedModelFactory):
    """Organization  model factory class.
    """
    name = "General Electric"

    class Meta(object):
        """Model meta class."""
        model = models.Organization

    organization_type = factory.SubFactory(OrganizationTypeModelFactory)


class OrganizationUnitModelFactory(NamedModelFactory):
    """Organization unit model factory class.
    """
    name = "Marketing"

    class Meta(object):
        """Model meta class."""
        model = models.OrganizationUnit

    organization = factory.SubFactory(OrganizationModelFactory)


class RoleModelFactory(NamedModelFactory):
    """Role model factory class.
    """
    name = "Project manager"

    class Meta(object):
        """Model meta class."""
        model = models.Role


class TitleModelFactory(NamedModelFactory):
    """Title model factory class.
    """
    name = "Vice President"

    class Meta(object):
        """Model meta class."""
        model = models.Title
