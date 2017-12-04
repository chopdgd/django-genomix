=============================
Django GenomiX
=============================

.. image:: https://badge.fury.io/py/django-genomix.svg
    :target: https://badge.fury.io/py/django-genomix

.. image:: https://travis-ci.org/chopdgd/django-genomix.svg?branch=master
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
        'genomix.apps.GenomixConfig',
        ...
    )


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
