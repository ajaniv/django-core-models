"""
..  module:: django_core_models.locations.views
    :synopsis: django_core_models location application views  module.

*django_core_models* locations application views  module.
"""
from __future__ import absolute_import


from django_core_utils.views import ObjectListView, ObjectDetailView
from . import models
from . import serializers


class CountryMixin(object):
    """Country mixin class."""
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer


class CountryList(CountryMixin, ObjectListView):
    """Class to list all Country instances, or create  new Country instance."""
    pass


class CountryDetail(CountryMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete Country instance.
    """
    pass


class DistanceUnitMixin(object):
    """DistanceUnit mixin class."""
    queryset = models.DistanceUnit.objects.all()
    serializer_class = serializers.DistanceUnitSerializer


class DistanceUnitList(DistanceUnitMixin, ObjectListView):
    """Class to list all DistanceUnit instances,
    or create new DistanceUnit instance."""
    pass


class DistanceUnitDetail(DistanceUnitMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete DistanceUnit instance.
    """
    pass


class GeographicLocationTypeMixin(object):
    """GeographicLocationType mixin class."""
    queryset = models.GeographicLocationType.objects.all()
    serializer_class = serializers.GeographicLocationTypeSerializer


class GeographicLocationTypeList(GeographicLocationTypeMixin, ObjectListView):
    """Class to list all GeographicLocationType instances,
    or create new GeographicLocationType instance."""
    pass


class GeographicLocationTypeDetail(GeographicLocationTypeMixin,
                                   ObjectDetailView):
    """
    Class to retrieve, update or delete GeographicLocationType instance.
    """
    pass


class GeographicLocationMixin(object):
    """GeographicLocation mixin class."""
    queryset = models.GeographicLocation.objects.all()
    serializer_class = serializers.GeographicLocationSerializer


class GeographicLocationList(GeographicLocationMixin, ObjectListView):
    """Class to list all GeographicLocation instances,
    or create new GeographicLocation instance."""
    pass


class GeographicLocationDetail(GeographicLocationMixin,
                               ObjectDetailView):
    """
    Class to retrieve, update or delete GeographicLocation instance.
    """
    pass


class LanguageTypeMixin(object):
    """LanguageType mixin class."""
    queryset = models.LanguageType.objects.all()
    serializer_class = serializers.LanguageTypeSerializer


class LanguageTypeList(LanguageTypeMixin, ObjectListView):
    """Class to list all LanguageType instances,
    or create new LanguageType instance."""
    pass


class LanguageTypeDetail(LanguageTypeMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete LanguageType instance.
    """
    pass


class LanguageMixin(object):
    """Language mixin class."""
    queryset = models.Language.objects.all()
    serializer_class = serializers.LanguageSerializer


class LanguageList(LanguageMixin, ObjectListView):
    """Class to list all Language instances,
    or create new Language instance."""
    pass


class LanguageDetail(LanguageMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete Language instance.
    """
    pass


class TimezoneTypeMixin(object):
    """TimezoneType mixin class."""
    queryset = models.TimezoneType.objects.all()
    serializer_class = serializers.TimezoneTypeSerializer


class TimezoneTypeList(TimezoneTypeMixin, ObjectListView):
    """Class to list all TimezoneType instances,
    or create new TimezoneType instance."""
    pass


class TimezoneTypeDetail(TimezoneTypeMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete TimezoneType instance.
    """
    pass


class TimezoneMixin(object):
    """TimezoneType mixin class."""
    queryset = models.Timezone.objects.all()
    serializer_class = serializers.TimezoneSerializer


class TimezoneList(TimezoneMixin, ObjectListView):
    """Class to list all Timezone instances,
    or create new Timezone instance."""
    pass


class TimezoneDetail(TimezoneMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete Timezone instance.
    """
    pass


class ProvinceMixin(object):
    """Province mixin class."""
    queryset = models.Province.objects.all()
    serializer_class = serializers.ProvinceSerializer


class ProvinceList(ProvinceMixin, ObjectListView):
    """Class to list all Province instances,
    or create new Province instance."""
    pass


class ProvinceDetail(ProvinceMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete Province instance.
    """
    pass


class StateMixin(object):
    """State mixin class."""
    queryset = models.State.objects.all()
    serializer_class = serializers.StateSerializer


class StateList(StateMixin, ObjectListView):
    """Class to list all State instances,
    or create new State instance."""
    pass


class StateDetail(StateMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete Province instance.
    """
    pass


class CityMixin(object):
    """City mixin class."""
    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer


class CityList(CityMixin, ObjectListView):
    """Class to list all City instances,
    or create new City instance."""
    pass


class CityDetail(CityMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete City instance.
    """
    pass


class AddressTypeMixin(object):
    """AddressType mixin class."""
    queryset = models.AddressType.objects.all()
    serializer_class = serializers.AddressTypeSerializer


class AddressTypeList(AddressTypeMixin, ObjectListView):
    """Class to list all AddressType instances,
    or create new AddressType instance."""
    pass


class AddressTypeDetail(AddressTypeMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete AddressType instance.
    """
    pass


class AddressMixin(object):
    """Address mixin class."""
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer


class AddressList(AddressMixin, ObjectListView):
    """Class to list all Address instances,
    or create new Address instance."""
    pass


class AddressDetail(AddressMixin, ObjectDetailView):
    """
    Class to retrieve, update or delete Address instance.
    """
    pass
