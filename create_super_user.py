#!/usr/bin/env python
"""
.. module::  create_super_user
   :synopsis:  crate default super user.

crate default super user

"""
# @TODO: provide the ability to pass parameters on the command line
# of settings file, user name, email, password
from __future__ import print_function
import os
from django.db.utils import IntegrityError

import django

DJANGO_SETTINGS_MODULE = "DJANGO_SETTINGS_MODULE"
os.environ[DJANGO_SETTINGS_MODULE] = os.environ.get(
    DJANGO_SETTINGS_MODULE, "django_core_models.settings")

_username = 'admin'
_password = _username + '123'
_domain = 'example.com'
_email = '%s@%s' % (_username, _domain)


def _create_super_user(username, email, password):
    from django.contrib.auth.models import User
    try:
        User.objects.create_superuser(username=username,
                                      email=email,
                                      password=password)
        print("user '%s' created" % username)
    except IntegrityError:
        print("user '%s' already exists in the database" % username)


if __name__ == "__main__":
    if hasattr(django, 'setup'):
        django.setup()
    _create_super_user(_username, _email, _password)
