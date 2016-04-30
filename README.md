core-models
===========

*django-core-models* is a Django project which defines common models for applications requiring contact related functionality. During the development of a contact application inspired by [VCARD RFC6350](https://tools.ietf.org/html/rfc6350/) quite a few low level models which were candidate for reuse by applications in related domains were identified. The choices were:

-   Leave them bundled with the contact application.
-   Separate the domains (i.e. location, demographics) into multiple packages. A POC verified that this approach is feasible.
-   Create a separate application for each of the underlying domains (i.e. Image, Demographics) managed by a separate project and SCM repository. This is the implementation choice that was taken at this time, primarily driven by the focus on ease of reuse.

The applications were implemented with internationalization in mind. This approach is manifested in the *models*, *text*, *forms* application modules.

The implementation uses Django admin facilities for data management, support, and other internal end user requirements. The intention is to have a companion set of browser based (i.e. AngularJS) and mobile applications support external end user needs.

A companion set of REST API end points is available using [djangorestframework](http://www.django-rest-framework.org/). These were developed by reusing components from [django-core-utils](https://github.com/ajaniv/django-core-utils/).

The requirement was to create a data driven application, where no code deployments will be required to support underlying data changes (i.e. new country). Each of the abstractions is derived from [*VersionedModel*](https://github.com/ajaniv/django-core-utils/), providing an audit trail of which user made the change, and when it was made.

*pycountry* is used to validate language, country, state, and province data.

It was developed using Django 1.9.4 for python 2.7, python 3.5, sqlite, MySql and Postgres. *tox*, *Travis*, *Docker* and *coverage* are used for unit test execution. The unit tests are also executed under Django 1.8.

Detailed documentation may be found in the "docs" directory.

Build Status
------------

[![image](https://travis-ci.org/ajaniv/django-core-utils.svg?branch=master)](https://travis-ci.org/ajaniv/django-core-utils)

Domains
-------

### Core

-   Annotation
-   Category
-   Currency

### Demographics

-   Age
-   ChildCount
-   DemographicRegion
-   EducationLevel
-   Ethnicity
-   Gender
-   HouseholdSize
-   Income

### Image

-   DocumentOrientation
-   Image
-   ImageFormat

### Location

-   Address
-   AddressType
-   City
-   Country
-   DistanceUnit
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

### Development/Runtime

-   [pycountry](https://pypi.python.org/pypi/pycountry).
-   [djangorestframework](http://www.django-rest-framework.org/).
-   [django-core-utils](https://github.com/ajaniv/django-core-utils/).
-   [python-core-utils](https://github.com/ajaniv/python-core-utils/).

### Testing

-   [django-core-utils-tests](https://github.com/ajaniv/django-core-utils-tests/).

### Development

-   coverage
-   flake8
-   tox
-   virtualenv

Rest API
--------

-   Key design principle avoid duplicate field, instance level validation. There is an additional performance hit with creation of instance for validation by using the underlying Django model clean method.
-   'api' is used to distinguish between the Rest api and other urls. Following the 'api' is the application designation such as '/api/core\_models/'
-   API versioning is implemented using headers and defaults to 1.
-   One is able to specify a subset of the required fields for both POST and PUT; the remainder are obtained from the request context (i.e site id, creation\_user)
-   While at present basic authentication is used, support for other implementations (i.e. token) is planned.

### Command line scenarios

These sample scenarios were executed using the [http](https://github.com/jkbrzt/httpie) command line utility:

-   create a currency with basic authentication: http -v -a admin:admin123 --json POST http://127.0.0.1:8000/currencies/ name="US Dollar" iso\_code="USD" creation\_user=1 effective\_user=1 update\_user=1 site=1
-   Specify api version: http -v -a admin:admin123 --json POST http://127.0.0.1:8000/api/core-models/currencies/ name="US Dollar" iso\_code="USD" creation\_user=1 effective\_user=1 update\_user=1 site=1 'Accept: application/json; version=1.0'
-   Specify minimal set of required fields while the remainder are derived from the request context: http -v -a admin:admin123 --json POST <http://127.0.0.1:8000/api/core-models/currencies/> name="Yen" iso\_code="JPY" 'Accept: application/json; version=1.0'\`

### Browser scenarios

These scenarios were executed using a browser:

-   Show list of currencies: http://127.0.0.1:8000/api/core-models/currencies/
-   Show list of API end points: http://127.0.0.1:8000/api/root/end-points/

    Returns:

        Api Root
        GET /api/root/end-points/
        HTTP 200 OK
        Allow: OPTIONS, GET
        Content-Type: application/json
        Vary: Accept

        {
            "currencies": "http://127.0.0.1:8000/api/core-models/currencies/",
            "categories": "http://127.0.0.1:8000/api/core-models/categories/",
            "users": "http://127.0.0.1:8000/api/root/users/"
        }

Docker unit test execution
--------------------------

To run unit tests in docker environment:

-   sqlite: docker-compose -f docker-sqlite-compose-test.yml up --abort-on-container-exit .
-   postgres: docker-compose -f docker-postgres-compose-test.yml up --abort-on-container-exit .
-   mysql: docker-compose -f docker-mysql-compose-test.yml up --abort-on-container-exit .

Docker container execution
--------------------------

To run browser against a docker container:

-   sqlite: docker-compose -f docker-sqlite-compose.yml up -d .
-   postgres: docker-compose -f docker-postgres-compose.yml up -d .
-   mysql: docker-compose -f docker-mysql-compose.yml up -d.

Set the browser address to the ip address returned from docker-machine ip. For example: http://192.168.99.100:8000/

Docker notes
------------

-   In order to configure command line docker environment:

    > 1.  docker-machine restart default
    > 2.  eval $(docker-machine env default)

-   To remove all containers: docker rm $(docker ps -a -q)
-   To remove all images: docker rmi -f $(docker images -q)

Data management
---------------

Fixtures were used to help test aspects of application usability. These are not automatically loaded during migration or testing. Sample fixtures are stored in the fixtures directory.

Fixture files can be created per application as outlined below:

-   python manage.py dumpdata --natural-foreign --natural-primary -o fixtures/locations.json locations

Fixtures can be loaded per application as outlined below:

-   python manage.py loaddata fixtures/locations.json

Other
-----

-   pandoc was used to convert from .rst to .md:

    `pandoc -f rst -t markdown_github -o README.md README.rst`

-   check-manifest was run from the command line. Could not get it to work from within tox. There was an error in handling '~' with gitconfig when running:

    `git ls-files -z`

-   To create admin super user: create\_super\_user.py

Todo
----

-   Organize docker files under a sub-directory without getting directory access exceptions.

Want to learn about [my favorite programming language](http://www.python.org)?
