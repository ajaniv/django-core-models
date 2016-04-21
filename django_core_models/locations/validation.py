"""
.. module::  location.validation
   :synopsis:  location validation module

*location* application validation module.

"""
import re

import pycountry
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def _invalid_iso(entity):
    """Generate invalid iso template."""
    base = "is an invalid %s iso code" % entity
    return "%(value)s " + base


def _invalid_name(entity):
    """Generate invalid name template."""
    base = "is an invalid %s name." % entity
    return "%(value)s " + base + "  Expected %(expected)s."


# Note: there are some minor differences in pycountry api which makes it
# a little bit tricky to eliminate what appears as redundant logic


def country_validation(country):
    """Perform country validation.
    """
    entity = "country"
    try:
        official = pycountry.countries.get(alpha2=country.iso_code)
    except KeyError:
        raise ValidationError(
            _(_invalid_iso(entity)),
            params={'value': country.iso_code})

    if official.official_name != country.name:
        raise ValidationError(
            _(_invalid_name(entity)),
            params={'value': country.name,
                    'expected': official.official_name})


def language_validation(language):
    """Perform language validation.
    """

    entity = "language"
    try:
        official = pycountry.languages.get(
            iso639_1_code=language.iso_code)
    except KeyError:
        raise ValidationError(
            _(_invalid_iso(entity)),
            params={'value': language.iso_code})

    if official.name != language.name:
        raise ValidationError(
            _(_invalid_name(entity)),
            params={'value': language.name,
                    'expected': official.name})


def state_validation(state):
    """Perform state validation."""
    entity = "state"
    try:
        official = pycountry.subdivisions.get(code=state.iso_code)
    except KeyError:
        raise ValidationError(_(_invalid_iso(entity)),
                              params={'value': state.iso_code})

    if official.name != state.name:
        raise ValidationError(
            _(_invalid_name(entity)),
            params={'value': state.name,
                    'expected': official.name})

    if not state.country.is_usa():
        raise ValidationError(_("%(country)s is an invalid for %(state)s."),
                              params={'country': state.country.name,
                                      'state': state.name})


def province_validation(province):
    """Perform province validation."""
    entity = "province"
    try:
        official = pycountry.subdivisions.get(code=province.iso_code)
    except KeyError:
        raise ValidationError(_(_invalid_iso(entity)),
                              params={'value': province.iso_code})

    if official.name != province.name:
        raise ValidationError(
            _(_invalid_name(entity)),
            params={'value': province.name,
                    'expected': official.name})

    if province.country.iso_code != official.country_code:
        raise ValidationError(
            _("%(country)s is an invalid country for %(province)s."),
            params={'country': province.country.name,
                    'province': province.name})


def state_and_province_validation(state, province):
    """Validate state and province.
    """
    if state is None and province is None:
        raise ValidationError(_("State and province are none."))
    if state and province:
        raise ValidationError(_("State and province are set."))


def country_state_province_validation(country, state, province):
    """Validate country."""
    if country is not None:
        if country.is_usa():
            if state is None:
                raise ValidationError(_("Country is USA. State is not set."))
            underlying_country = state.country
        else:
            if province is None:
                raise ValidationError(
                    _("Country is not USA. Province is not set."))
            underlying_country = province.country
        if country != underlying_country:
            raise ValidationError(
                _("State/province country improperly configured."))


def street_and_post_office_box_validation(post_office_box, street_address):
    """Validate street and post office box"""
    if not (post_office_box or street_address):
        raise ValidationError(_("post_office_box and street_address not set"))
    if post_office_box and street_address:
        raise ValidationError(_("post_office_box and street_address are set"))


re_usa_post_office_box = re.compile(r"""
    (
        (
            (Post\s*|P[\.\s]*)
            (Office\s*|O[\.\s]*)
            (Box|B[\.\s]*|Bin)?\s*
        )
        (\d+)\s*?
    )
    """, re.IGNORECASE | re.VERBOSE)


def post_office_box_validation(country, value):
    """Validate post office box."""
    msg = "%(value)s is an invalid post office box."
    if value:
        if country.is_usa() and re_usa_post_office_box.match(value) is None:
            raise ValidationError(_(msg),
                                  params={'value': value})

re_usa_postal_code = re.compile(r"""
    (\d{5})
    | ((\d{5}) (\s*-\s*) (\d{4}))
    """, re.VERBOSE)


def postal_code_validation(country, value):
    """Validate postal code."""
    msg = "%(value)s is an invalid postal code."
    if value:
        if country.is_usa():
            # should be invalid - '67890 A'
            if (re_usa_postal_code.match(value) is None or
                    re.search('[a-zA-Z]+', value)):  # @IgnorePep8
                raise ValidationError(_(msg),
                                      params={'value': value})
