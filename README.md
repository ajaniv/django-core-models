core-models
===========

*django-core-models* is a Django project which defines common models for applications requiring contact related functionality. During the development of a contact application inspired by [VCARD RFC6350](https://tools.ietf.org/html/rfc6350/) quite a few low level models which were candidate for reuse by applications in related domains were identified. The choices were:

-   Leave them bundled with the contact application.
-   Create a separate application for each of the underlying domains (i.e. Image, Demographics). This is the implementation choice that was taken at this time.

The applications were implemented with internationalization in mind. This approach is manifested in the *models*, *text*, *forms* application modules.

The intention is to create a data driven application, where no code deployments will be required to support underlying data changes (i.e. new country). Each of the abstractions is derived from *VersionedModel*, providing an audit trail of which user made the change, and when it was made.

*pycountry* is used to validate language, country, state, and province data.

It was developed using Django 1.9.4 for python 2.7, python 3.5, sqlite, MySql and Postgres. *tox*, *Travis*, and *Docker* are used for the testing.

Detailed documentation may be found in the "docs" directory.

Build Status
------------

[![image](https://travis-ci.org/ajaniv/django-core-utils.svg?branch=master)](https://travis-ci.org/ajaniv/django-core-utils)

Domains
-------

### Core

-   Annotation
-   Category

### Demographics

-   Gender

### Image

-   DocumentOrientation
-   Image
-   ImageFormat

### Location

-   Address
-   AddressType
-   Country
-   GeographicLocationType
-   GeographichLocation
-   Language
-   LanguageType
-   Province
-   Region
-   State
-   Timezone
-   TimezoneType

### Organization

-   Organization
-   OrganizationType
-   OrganizationUnit
-   Role
-   Title

### Social Media

-   EmailType
-   FormattedName
-   Group
-   InstantMessagingType
-   LogoType
-   Name
-   NicknameType
-   PhoneType
-   PhotoType
-   UrlType

Quick start
-----------

1.  Add the relevant applications to your INSTALLED\_APPS setting like this:

        INSTALLED_APPS = [
            ...
            'model_apps.core.apps.CoreModelsConfig',
            'model_apps.demographics.apps.DemographicsConfig',
            'model_apps.image.apps.ImageConfig',
            'model_apps.location.apps.LocationConfig',
            'model_apps.organization.apps.OrganizationConfig',
            'model_apps.social_media.apps.SocialMediaConfig',

        ]

Dependencies
------------

### Runtime

-   pycountry
-   [django-core-utils](https://github.com/ajaniv/django-core-utils/).
-   [python-core-utils](https://github.com/ajaniv/python-core-utils/).

### Testing

-   [django-core-utils-tests](https://github.com/ajaniv/django-core-utils-tests/).

### Development

-   coverage
-   flake8
-   tox
-   virtualenv

### Notes

-   pandoc was used to convert from .rst to .md:

    `pandoc -f rst -t markdown_github -o README.md README.rst`

-   check-manifest was run from the command line. Could not get it to work from within tox. There was an error in handling '~' with gitconfig when running:

    `git ls-files -z`

-   In order to configure command line docker environment:

    > 1.  docker-machine restart default
    > 2.  eval $(docker-machine env default)

-   To run unit tests in docker sqlite environment: docker-compose -f docker-compose-sqlite.yml up --abort-on-container-exit .
-   To run unit tests in docker postgres environment: docker-compose -f docker-compose-postgres.yml up --abort-on-container-exit .
-   To run unit tests in docker mysql environment: docker-compose -f docker-compose-mysql.yml up --abort-on-container-exit .
-   To remove all containers: docker rm $(docker ps -a -q)
-   To remove all images: docker rmi -f $(docker images -q)
-   To create admin super user: create\_super\_user.py

