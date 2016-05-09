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

[![image](https://travis-ci.org/ajaniv/django-core-models.svg?branch=master)](https://travis-ci.org/ajaniv/django-core-models)

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

-   Email
-   EmailType
-   FormattedName
-   Group
-   InstantMessagingType
-   LogoType
-   Name
-   Nickname
-   NicknameType
-   Phone
-   PhoneType
-   PhotoType
-   Url
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

#### Create (currency) with basic authentication

All the mandatory fields are specified.

Request:

    http -v -a admin:admin123 --json POST http://127.0.0.1:8000/api/core-models/currencies/ name="US Dollar" iso_code="USD" creation_user=1 effective_user=1 update_user=1 site=1

Response:

    POST /api/core-models/currencies/ HTTP/1.1
    Accept: application/json
    Accept-Encoding: gzip, deflate
    Authorization: Basic YWRtaW46YWRtaW4xMjM=
    Connection: keep-alive
    Content-Length: 118
    Content-Type: application/json
    Host: 127.0.0.1:8000
    User-Agent: HTTPie/0.9.3

    {
        "creation_user": "1",
        "effective_user": "1",
        "iso_code": "USD",
        "name": "US Dollar",
        "site": "1",
        "update_user": "1"
    }

    HTTP/1.0 201 Created
    Allow: GET, POST, HEAD, OPTIONS
    Content-Type: application/json
    Date: Thu, 05 May 2016 15:41:29 GMT
    Server: WSGIServer/0.2 CPython/3.5.1
    Vary: Accept, Cookie
    X-Frame-Options: SAMEORIGIN

    {
        "alias": null,
        "creation_time": "2016-05-05T15:41:29.152318Z",
        "creation_user": 1,
        "deleted": false,
        "description": null,
        "effective_user": 1,
        "enabled": true,
        "id": 1,
        "iso_code": "USD",
        "name": "US Dollar",
        "site": 1,
        "update_time": "2016-05-05T15:41:29.152404Z",
        "update_user": 1,
        "uuid": "e2e8ff29-5caf-4111-a851-8b376fc31024",
        "version": 1
    }

#### Delete (currency) with basic authentication

Request:

    http -v -a admin:admin123 --json DELETE http://127.0.0.1:8000/api/core-models/currencies/1/

Response:

    DELETE /api/core-models/currencies/1/ HTTP/1.1
    Accept: application/json
    Accept-Encoding: gzip, deflate
    Authorization: Basic YWRtaW46YWRtaW4xMjM=
    Connection: keep-alive
    Content-Length: 0
    Content-Type: application/json
    Host: 127.0.0.1:8000
    User-Agent: HTTPie/0.9.3



    HTTP/1.0 204 No Content
    Allow: GET, PUT, DELETE, HEAD, OPTIONS
    Content-Length: 0
    Date: Thu, 05 May 2016 15:55:43 GMT
    Server: WSGIServer/0.2 CPython/3.5.1
    Vary: Accept, Cookie
    X-Frame-Options: SAMEORIGIN

#### Create (currency) providing specific api version

If the api version is not provided, a default value of the current version is used.

Request:

    http -v -a admin:admin123 --json POST http://127.0.0.1:8000/api/core-models/currencies/ name="US Dollar" iso_code="USD" creation_user=1 effective_user=1 update_user=1 site=1 'Accept: application/json; version=1.0'

Response:

    POST /api/core-models/currencies/ HTTP/1.1
    Accept:  application/json; version=1.0
    Accept-Encoding: gzip, deflate
    Authorization: Basic YWRtaW46YWRtaW4xMjM=
    Connection: keep-alive
    Content-Length: 118
    Content-Type: application/json
    Host: 127.0.0.1:8000
    User-Agent: HTTPie/0.9.3

    {
        "creation_user": "1",
        "effective_user": "1",
        "iso_code": "USD",
        "name": "US Dollar",
        "site": "1",
        "update_user": "1"
    }

    HTTP/1.0 201 Created
    Allow: GET, POST, HEAD, OPTIONS
    Content-Type: application/json; version=1.0
    Date: Thu, 05 May 2016 15:57:52 GMT
    Server: WSGIServer/0.2 CPython/3.5.1
    Vary: Accept, Cookie
    X-Frame-Options: SAMEORIGIN

    {
        "alias": null,
        "creation_time": "2016-05-05T15:57:52.353654Z",
        "creation_user": 1,
        "deleted": false,
        "description": null,
        "effective_user": 1,
        "enabled": true,
        "id": 2,
        "iso_code": "USD",
        "name": "US Dollar",
        "site": 1,
        "update_time": "2016-05-05T15:57:52.353708Z",
        "update_user": 1,
        "uuid": "81fa9654-e799-4074-a8c1-a047ebf9e6ff",
        "version": 1
    }

#### Update (currency) providing subset of fields

Only the fields required to validate the instance are required. Further implementation work is required to simplify the approach.

Request:

    http -v -a admin:admin123 --json PUT http://127.0.0.1:8000/api/core-models/currencies/2/ name="US Dollar" iso_code="USD" alias="default currency"

Response:

    PUT /api/core-models/currencies/2/ HTTP/1.1
    Accept: application/json
    Accept-Encoding: gzip, deflate
    Authorization: Basic YWRtaW46YWRtaW4xMjM=
    Connection: keep-alive
    Content-Length: 69
    Content-Type: application/json
    Host: 127.0.0.1:8000
    User-Agent: HTTPie/0.9.3

    {
        "alias": "default currency",
        "iso_code": "USD",
        "name": "US Dollar"
    }

    HTTP/1.0 200 OK
    Allow: GET, PUT, DELETE, HEAD, OPTIONS
    Content-Type: application/json
    Date: Thu, 05 May 2016 16:06:55 GMT
    Server: WSGIServer/0.2 CPython/3.5.1
    Vary: Accept, Cookie
    X-Frame-Options: SAMEORIGIN

    {
        "alias": "default currency",
        "creation_time": "2016-05-05T15:57:52.353654Z",
        "creation_user": 1,
        "deleted": false,
        "description": null,
        "effective_user": 1,
        "enabled": true,
        "id": 2,
        "iso_code": "USD",
        "name": "US Dollar",
        "site": 1,
        "update_time": "2016-05-05T16:06:55.460644Z",
        "update_user": 1,
        "uuid": "81fa9654-e799-4074-a8c1-a047ebf9e6ff",
        "version": 2
    }

#### Create (currency) providing subset of fields

Specify minimal set of required fields while the remainder are derived from the request context

Request:

    http -v -a admin:admin123 --json POST http://127.0.0.1:8000/api/core-models/currencies/ name="Yen" iso_code="JPY" 'Accept: application/json; version=1.0'

Response:

    POST /api/core-models/currencies/ HTTP/1.1
    Accept:  application/json; version=1.0
    Accept-Encoding: gzip, deflate
    Authorization: Basic YWRtaW46YWRtaW4xMjM=
    Connection: keep-alive
    Content-Length: 34
    Content-Type: application/json
    Host: 127.0.0.1:8000
    User-Agent: HTTPie/0.9.3

    {
        "iso_code": "JPY",
        "name": "Yen"
    }

    HTTP/1.0 201 Created
    Allow: GET, POST, HEAD, OPTIONS
    Content-Type: application/json; version=1.0
    Date: Thu, 05 May 2016 16:13:09 GMT
    Server: WSGIServer/0.2 CPython/3.5.1
    Vary: Accept, Cookie
    X-Frame-Options: SAMEORIGIN

    {
        "alias": null,
        "creation_time": "2016-05-05T16:13:09.766046Z",
        "creation_user": 1,
        "deleted": false,
        "description": null,
        "effective_user": 1,
        "enabled": true,
        "id": 3,
        "iso_code": "JPY",
        "name": "Yen",
        "site": 1,
        "update_time": "2016-05-05T16:13:09.766161Z",
        "update_user": 1,
        "uuid": "4e0b23ed-b4cd-443a-99b0-52cf5d886b97",
        "version": 1
    }

#### Get all instances (currencies)

Request:

    http -v -a admin:admin123 --json GET http://127.0.0.1:8000/api/core-models/currencies/

Response:

    GET /api/core-models/currencies/ HTTP/1.1
    Accept: application/json
    Accept-Encoding: gzip, deflate
    Authorization: Basic YWRtaW46YWRtaW4xMjM=
    Connection: keep-alive
    Content-Type: application/json
    Host: 127.0.0.1:8000
    User-Agent: HTTPie/0.9.3



    HTTP/1.0 200 OK
    Allow: GET, POST, HEAD, OPTIONS
    Content-Type: application/json
    Date: Thu, 05 May 2016 16:15:52 GMT
    Server: WSGIServer/0.2 CPython/3.5.1
    Vary: Accept, Cookie
    X-Frame-Options: SAMEORIGIN

    [
        {
            "alias": "default currency",
            "creation_time": "2016-05-05T15:57:52.353654Z",
            "creation_user": 1,
            "deleted": false,
            "description": null,
            "effective_user": 1,
            "enabled": true,
            "id": 2,
            "iso_code": "USD",
            "name": "US Dollar",
            "site": 1,
            "update_time": "2016-05-05T16:06:55.460644Z",
            "update_user": 1,
            "uuid": "81fa9654-e799-4074-a8c1-a047ebf9e6ff",
            "version": 2
        },
        {
            "alias": null,
            "creation_time": "2016-05-05T16:13:09.766046Z",
            "creation_user": 1,
            "deleted": false,
            "description": null,
            "effective_user": 1,
            "enabled": true,
            "id": 3,
            "iso_code": "JPY",
            "name": "Yen",
            "site": 1,
            "update_time": "2016-05-05T16:13:09.766161Z",
            "update_user": 1,
            "uuid": "4e0b23ed-b4cd-443a-99b0-52cf5d886b97",
            "version": 1
        }
    ]

### Browser scenarios

These scenarios were executed using a browser navigating Django Rest Framework urls.

#### Show list of end points

Request:

    http://127.0.0.1:8000/api/root/end-points/

Response:

    GET /api/root/end-points/

    HTTP 200 OK
    Allow: OPTIONS, GET
    Content-Type: application/json
    Vary: Accept

    {
        "address-types": "http://127.0.0.1:8000/api/locations/address-types/",
        "addresses": "http://127.0.0.1:8000/api/locations/addresses/",
        "ages": "http://127.0.0.1:8000/api/demographics/ages/",
        "annotations": "http://127.0.0.1:8000/api/core-models/annotations/",
        "categories": "http://127.0.0.1:8000/api/core-models/categories/",
        "child-count": "http://127.0.0.1:8000/api/demographics/child-count/",
        "cities": "http://127.0.0.1:8000/api/locations/cities/",
        "countries": "http://127.0.0.1:8000/api/locations/countries/",
        "currencies": "http://127.0.0.1:8000/api/core-models/currencies/",
        "demographic-regions": "http://127.0.0.1:8000/api/demographics/demographic-regions/",
        "distance-units": "http://127.0.0.1:8000/api/locations/distance-units/",
        "document-orientations": "http://127.0.0.1:8000/api/images/document-orientations/",
        "education-levels": "http://127.0.0.1:8000/api/demographics/education-levels/",
        "email-types": "http://127.0.0.1:8000/api/social-media/email-types/",
        "ethnicities": "http://127.0.0.1:8000/api/demographics/ethnicities/",
        "formatted-names": "http://127.0.0.1:8000/api/social-media/formatted-names/",
        "gender": "http://127.0.0.1:8000/api/demographics/gender/",
        "geographic-location": "http://127.0.0.1:8000/api/locations/geographic-locations/",
        "geographic-location-types": "http://127.0.0.1:8000/api/locations/geographic-location-types/",
        "groups": "http://127.0.0.1:8000/api/social-media/groups/",
        "household-size": "http://127.0.0.1:8000/api/demographics/household-size/",
        "image-formats": "http://127.0.0.1:8000/api/images/image-formats/",
        "images": "http://127.0.0.1:8000/api/images/images/",
        "incomes": "http://127.0.0.1:8000/api/demographics/incomes/",
        "instant-messaging-types": "http://127.0.0.1:8000/api/social-media/instant-message-types/",
        "language-types": "http://127.0.0.1:8000/api/locations/language-types/",
        "languages": "http://127.0.0.1:8000/api/locations/languages/",
        "logo-types": "http://127.0.0.1:8000/api/social-media/logo-types/",
        "names": "http://127.0.0.1:8000/api/social-media/names/",
        "nickname-types": "http://127.0.0.1:8000/api/social-media/nickname-types/",
        "organization-types": "http://127.0.0.1:8000/api/organizations/organization-types/",
        "organization-units": "http://127.0.0.1:8000/api/organizations/organization-units/",
        "organizations": "http://127.0.0.1:8000/api/organizations/organizations/",
        "phone-types": "http://127.0.0.1:8000/api/social-media/phone-types/",
        "photo-types": "http://127.0.0.1:8000/api/social-media/photo-types/",
        "provinces": "http://127.0.0.1:8000/api/locations/proninces/",
        "roles": "http://127.0.0.1:8000/api/organizations/roles/",
        "states": "http://127.0.0.1:8000/api/locations/states/",
        "timezone-types": "http://127.0.0.1:8000/api/locations/timezone-types/",
        "timezones": "http://127.0.0.1:8000/api/locations/timezones/",
        "titles": "http://127.0.0.1:8000/api/organizations/titles/",
        "url-types": "http://127.0.0.1:8000/api/social-media/url-types/",
        "users": "http://127.0.0.1:8000/api/root/users/"
    }

#### Show list of currencies

Request:

    http://127.0.0.1:8000/api/core-models/currencies/

Response:

    GET /api/core-models/currencies/

    HTTP 200 OK
    Allow: GET, POST, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept

    [
        {
            "id": 2,
            "uuid": "81fa9654-e799-4074-a8c1-a047ebf9e6ff",
            "version": 2,
            "enabled": true,
            "deleted": false,
            "creation_time": "2016-05-05T15:57:52.353654Z",
            "update_time": "2016-05-05T16:06:55.460644Z",
            "creation_user": 1,
            "update_user": 1,
            "effective_user": 1,
            "site": 1,
            "name": "US Dollar",
            "alias": "default currency",
            "description": null,
            "iso_code": "USD"
        },
        {
            "id": 3,
            "uuid": "4e0b23ed-b4cd-443a-99b0-52cf5d886b97",
            "version": 1,
            "enabled": true,
            "deleted": false,
            "creation_time": "2016-05-05T16:13:09.766046Z",
            "update_time": "2016-05-05T16:13:09.766161Z",
            "creation_user": 1,
            "update_user": 1,
            "effective_user": 1,
            "site": 1,
            "name": "Yen",
            "alias": null,
            "description": null,
            "iso_code": "JPY"
        }
    ]

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

To do
-----

-   Generate sphinix and/or markup documentation.
-   Organize docker files under a sub-directory without getting directory access exceptions.
-   Revisit approach to hand crafted models, admin, djangorestframework serializers, and unit tests. While some of these can be generated dynamically, often one faces incomparability issues with underlying django and djangorestframework upgrades.
-   References to other objects when using the rest api are by primary key, and not url.
-   Put requests require all fields used in validation, even when only a subset of these are to be updated. The root cause is the need to call model clean method from the serializer validate function because of the desire to avoid duplicating the model validation logic.

