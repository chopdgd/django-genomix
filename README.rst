=============================
Django GenomiX
=============================

.. image:: https://badge.fury.io/py/django-genomix.svg
    :target: https://badge.fury.io/py/django-genomix

.. image:: https://travis-ci.org/genomics-geek/django-genomix.svg?branch=master
    :target: https://travis-ci.org/genomics-geek/django-genomix

.. image:: https://codecov.io/gh/genomics-geek/django-genomix/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/genomics-geek/django-genomix

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
        'genomix.apps.GenomixConfig',
        ...
    )

Add Django GenomiX's URL patterns:

.. code-block:: python

    from genomix import urls as genomix_urls


    urlpatterns = [
        ...
        url(r'^', include(genomix_urls)),
        ...
    ]

Features
--------

* TODO

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
