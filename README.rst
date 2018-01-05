=============================
Django GenomiX
=============================

.. image:: https://badge.fury.io/py/django-genomix.svg
    :target: https://badge.fury.io/py/django-genomix

.. image:: https://travis-ci.org/chopdgd/django-genomix.svg?branch=develop
    :target: https://travis-ci.org/chopdgd/django-genomix

.. image:: https://codecov.io/gh/chopdgd/django-genomix/branch/develop/graph/badge.svg
    :target: https://codecov.io/gh/chopdgd/django-genomix

.. image:: https://pyup.io/repos/github/chopdgd/django-genomix/shield.svg
     :target: https://pyup.io/repos/github/chopdgd/django-genomix/
     :alt: Updates

.. image:: https://pyup.io/repos/github/chopdgd/django-genomix/python-3-shield.svg
      :target: https://pyup.io/repos/github/chopdgd/django-genomix/
      :alt: Python 3

Core library for Nexus django projects

Documentation
-------------

The full documentation is at https://django-genomix.readthedocs.io.

Quickstart
----------

Install Django GenomiX::

    pip install django-genomix

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'genomix',
        ...
    )


Features
--------

1. DisplayChoiceField - display representation values for choice fields in REST APIs.::

.. code-block:: python

    from genomix.fields import DisplayChoiceField
    from rest_framework import serializers

    from . import choices


    class ExampleSerializer(serializers.ModelSerializer):

        status = DisplayChoiceField(choices=choices.STATUS_OPTIONS)

2. UserRelatedField - display username for a REST API with a user relation.::

.. code-block:: python
    from django.contrib.auth import get_user_model

    from genomix.fields import UserRelatedField
    from rest_framework import serializers


    class ExampleSerializer(serializers.ModelSerializer):

        user = UserRelatedField(queryset=get_user_model().objects.all())


3. ContentRelatedField - display ContentType model for a REST API using a generic relation.::

.. code-block:: python
    from django.contrib.auth import get_user_model
    from django.contrib.contenttypes.models import ContentType

    from genomix.fields import ContentRelatedField
    from rest_framework import serializers


    class ExampleSerializer(serializers.ModelSerializer):

        content_type = ContentRelatedField(queryset=ContentType.objects.all())

4. DisplayChoiceFilter - Filter by representation values in a REST API.::

.. code-block:: python

    import django_filters
    from genomix.filters import DisplayChoiceFilter

    from . import choices


    class ExampleFilter(django_filters.rest_framework.FilterSet):

        source = DisplayChoiceFilter(choices=choices.SOURCES)

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
