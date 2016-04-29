===========
core-models
===========

*django-core-models* is a Django project which defines common models for applications
requiring contact related functionality.  During the development of a contact
application inspired  by  `VCARD RFC6350  <https://tools.ietf.org/html/rfc6350/>`_
quite a few low level models which were candidate for reuse by
applications in related domains were identified.  The  choices were:

* Leave them bundled with the contact application.
* Separate the domains (i.e. location, demographics) into multiple packages.  A POC
  verified that this approach is feasible.
* Create a separate application for each of the underlying domains (i.e. Image, Demographics).
  This is the implementation choice that was taken at this time, primarily driven by the focus
  on ease of reuse.

The applications were implemented with internationalization in mind.  This approach is
manifested in the *models*, *text*, *forms* application modules.

The intention is to create a data driven application, where no code deployments will be required
to support underlying data changes (i.e. new country).  Each of the abstractions is derived from
*VersionedModel*, providing an audit trail of which user made the change, and when it was made. 

*pycountry* is used to validate language, country, state, and province data.

It was developed using Django 1.9.4 for python 2.7, python 3.5, sqlite, MySql and Postgres.
*tox*, *Travis*, *Docker* and *coverage* are used for unit test execution.

Detailed documentation may be found in the "docs" directory.

Build Status
------------

.. image:: https://travis-ci.org/ajaniv/django-core-utils.svg?branch=master
    :target: https://travis-ci.org/ajaniv/django-core-utils

Domains
-------

Core
^^^^
* Annotation
* Category

Demographics
^^^^^^^^^^^^

* Gender

Image
^^^^^
* DocumentOrientation
* Image
* ImageFormat


Location
^^^^^^^^
* Address
* AddressType
* Country
* GeographicLocationType
* GeographichLocation
* Language
* LanguageType
* Province
* Region
* State
* Timezone
* TimezoneType


Organization
^^^^^^^^^^^^
* Organization
* OrganizationType
* OrganizationUnit
* Role
* Title


Social Media
^^^^^^^^^^^^
* EmailType
* FormattedName
* Group
* InstantMessagingType
* LogoType
* Name
* NicknameType
* PhoneType
* PhotoType
* UrlType



Quick start
-----------

1. Add the relevant applications to your INSTALLED_APPS setting like this::

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

Runtime
^^^^^^^
* `pycountry <https://pypi.python.org/pypi/pycountry>`_.
* `django-core-utils  <https://github.com/ajaniv/django-core-utils/>`_.
* `python-core-utils  <https://github.com/ajaniv/python-core-utils/>`_.


Testing
^^^^^^^
* `django-core-utils-tests  <https://github.com/ajaniv/django-core-utils-tests/>`_.


Development
^^^^^^^^^^^

* coverage
* flake8
* tox
* virtualenv

Docker unit test execution
--------------------------
To run unit tests in docker environment:

* sqlite: `docker-compose -f docker-sqlite-compose-test.yml up --abort-on-container-exit` .
* postgres: `docker-compose -f docker-postgres-compose-test.yml up --abort-on-container-exit` .
* mysql: `docker-compose -f docker-mysql-compose-test.yml up --abort-on-container-exit` .

Docker container execution
--------------------------
To run browser against a docker container:

* sqlite: `docker-compose -f docker-sqlite-compose.yml up -d` .
* postgres: `docker-compose -f docker-postgres-compose.yml up -d` .
* mysql: `docker-compose -f docker-mysql-compose.yml up -d`.

Set the browser address to the ip address returned from `docker-machine ip`.
For example: `http://192.168.99.100:8000/`

Docker notes
------------

* In order to configure command line docker environment:

    #. docker-machine restart default
    #. eval $(docker-machine env default)


* To remove all containers: `docker rm $(docker ps -a -q)`
* To remove all images: `docker rmi -f $(docker images -q)`

Data management
---------------
Fixtures were used to help test aspects of  application usability.
These are not automatically loaded during migration or testing.
Sample fixtures are stored in the `fixtures` directory. 

Fixture files can be created per application as outlined below:

* `python manage.py dumpdata --natural-foreign --natural-primary -o fixtures/locations.json locations`


Fixtures can be loaded per application as outlined below:

* `python manage.py loaddata fixtures/locations.json`

Other
-----

* pandoc was used to convert from .rst to .md:

  ``pandoc -f rst -t markdown_github -o README.md README.rst``
  
* check-manifest was run from the command line.  Could not get it
  to work from within tox.  There was an error in handling '~'
  with gitconfig when running:
  
  ``git ls-files -z``    
  
* To create admin super user: `create_super_user.py`

Todo
----

* Organize docker files under a sub-directory without getting directory access exceptions.
