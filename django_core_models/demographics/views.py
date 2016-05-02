"""
..  module:: django_core_models.demographics.views
    :synopsis: django_core_models demographics application views  module.

*django_core_models* demographics application views  module.
"""
from __future__ import absolute_import

from django_core_utils.views import ObjectListView, ObjectDetailView
from . import models
from . import serializers


class AgeMixin(object):
    """Age mixin class."""
    queryset = models.Age.objects.all()
    serializer_class = serializers.AgeSerializer


class AgeList(AgeMixin, ObjectListView):
    """Class to list all Age instances, or create a new Age instance."""
    pass


class AgeDetail(AgeMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete Age instance.
    """
    pass


class ChildCountMixin(object):
    """ChildCount mixin class."""
    queryset = models.ChildCount.objects.all()
    serializer_class = serializers.ChildCountSerializer


class ChildCountList(ChildCountMixin, ObjectListView):
    """Class to list all ChildCount instances,
    or create a new ChildCount instance."""
    pass


class ChildCountDetail(ChildCountMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete ChildCount instance.
    """
    pass


class DemographicRegionMixin(object):
    """DemographicRegion mixin class."""
    queryset = models.DemographicRegion.objects.all()
    serializer_class = serializers.DemographicRegionSerializer


class DemographicRegionList(DemographicRegionMixin, ObjectListView):
    """Class to list all DemographicRegion instances,
     or create a new DemographicRegion instance."""
    pass


class DemographicRegionDetail(DemographicRegionMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete DemographicRegion instance.
    """
    pass


class EducationLevelMixin(object):
    """EducationLevel mixin class."""
    queryset = models.EducationLevel.objects.all()
    serializer_class = serializers.EducationLevelSerializer


class EducationLevelList(EducationLevelMixin, ObjectListView):
    """Class to list all EducationLevel instances,
     or create a new EducationLevel instance."""
    pass


class EducationLevelDetail(EducationLevelMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete EducationLevel instance.
    """
    pass


class EthnicityMixin(object):
    """Ethnicity mixin class."""
    queryset = models.Ethnicity.objects.all()
    serializer_class = serializers.EthnicitySerializer


class EthnicityList(EthnicityMixin, ObjectListView):
    """Class to list all Ethnicity instances,
     or create a new Ethnicity instance."""
    pass


class EthnicityDetail(EthnicityMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete Ethnicity instance.
    """
    pass


class GenderMixin(object):
    """Gender mixin class."""
    queryset = models.Gender.objects.all()
    serializer_class = serializers.GenderSerializer


class GenderList(GenderMixin, ObjectListView):
    """Class to list all Gender instances,
     or create a new Gender instance."""
    pass


class GenderDetail(GenderMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete Gender instance.
    """
    pass


class HouseholdSizeMixin(object):
    """HouseholdSize mixin class."""
    queryset = models.HouseholdSize.objects.all()
    serializer_class = serializers.HouseholdSizeSerializer


class HouseholdSizeList(HouseholdSizeMixin, ObjectListView):
    """Class to list all HouseholdSize instances,
     or create a new HouseholdSize instance."""
    pass


class HouseholdSizeDetail(HouseholdSizeMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete HouseholdSize instance.
    """
    pass


class IncomeMixin(object):
    """Income mixin class."""
    queryset = models.Income.objects.all()
    serializer_class = serializers.IncomeSerializer


class IncomeList(IncomeMixin, ObjectListView):
    """Class to list all Income instances,
     or create a new Income instance."""
    pass


class IncomeDetail(IncomeMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete Income instance.
    """
    pass
