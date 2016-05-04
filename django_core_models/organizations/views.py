"""
..  module:: django_core_models.organizations.views
    :synopsis: django_core_models organizations application views  module.

*django_core_models* organizations application views  module.
"""
from __future__ import absolute_import


from django_core_utils.views import ObjectListView, ObjectDetailView
from . import models
from . import serializers


class OrganizationTypeMixin(object):
    """OrganizationType mixin class."""
    queryset = models.OrganizationType.objects.all()
    serializer_class = serializers.OrganizationTypeSerializer


class OrganizationTypeList(OrganizationTypeMixin, ObjectListView):
    """Class to list all OrganizationType instances,
     or create  new OrganizationType instance."""
    pass


class OrganizationTypeDetail(OrganizationTypeMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete OrganizationType instance.
    """
    pass


class OrganizationMixin(object):
    """Organization mixin class."""
    queryset = models.Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer


class OrganizationList(OrganizationMixin, ObjectListView):
    """Class to list all Organization instances,
    or create new Organization instance."""
    pass


class OrganizationDetail(OrganizationMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete Organization instance.
    """
    pass


class OrganizationUnitMixin(object):
    """OrganizationUnit mixin class."""
    queryset = models.OrganizationUnit.objects.all()
    serializer_class = serializers.OrganizationUnitSerializer


class OrganizationUnitList(OrganizationUnitMixin, ObjectListView):
    """Class to list all OrganizationUnit instances,
    or create new OrganizationUnit instance."""
    pass


class OrganizationUnitDetail(OrganizationUnitMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete OrganizationUnit instance.
    """
    pass


class RoleMixin(object):
    """GeographicLocation mixin class."""
    queryset = models.Role.objects.all()
    serializer_class = serializers.RoleSerializer


class RoleList(RoleMixin, ObjectListView):
    """Class to list all Role instances, or create new Role instance."""
    pass


class RoleDetail(RoleMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete Role instance.
    """
    pass


class TitleMixin(object):
    """Title mixin class."""
    queryset = models.Title.objects.all()
    serializer_class = serializers.TitleSerializer


class TitleList(TitleMixin, ObjectListView):
    """Class to list all Title instances, or create new Title instance."""
    pass


class TitleDetail(TitleMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete Title instance.
    """
    pass
