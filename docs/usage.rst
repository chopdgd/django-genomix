=====
Usage
=====

To use django-genomix in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'genomix.apps.GenomixConfig',
        ...
    )

Add django-genomix's URL patterns:

.. code-block:: python

    from genomix import urls as genomix_urls


    urlpatterns = [
        ...
        url(r'^', include(genomix_urls)),
        ...
    ]
