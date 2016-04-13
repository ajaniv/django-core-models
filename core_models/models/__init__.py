"""
.. module::  core_models.models
   :synopsis:  core_models models package.

*core_models* models package.

"""
from __future__ import absolute_import

from .demographics import (GENDER_FEMALE, GENDER_MALE,
                           GENDER_UNKNOWN, GENDER, Gender)
from .image import (IMAGE_FORMAT_GIF, IMAGE_FORMAT_JPEG,
                    IMAGE_FORMAT_PNG, IMAGE_FORMAT_UNKNOWN,
                    IMAGE_FORMATS, ORIENTATION_LANDSCAPE,
                    ORIENTATION_PORTRAIT, ORIENTATION_UNKNOWN,
                    VISUAL_ORIENTATION, DocumentOrientation, Image,
                    ImageFormat, ImageManager)
from .location import (Address, AddressType, Country, GeographicLocation,
                       GeographicLocationType, Language, LanguageType,
                       Province, Region, State, Timezone, TimezoneType)
from .organization import (Organization, OrganizationType, OrganizationUnit,
                           Role, Title)
from .other import Annotation, Category
from .social_media import (EmailType, FormattedName, Group,
                           InstantMessagingType, LogoType, Name, NicknameType,
                           PhoneType, PhotoType, UrlType)
