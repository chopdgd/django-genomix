=====
Usage
=====

To use Django GenomiX in a project, add it to your `INSTALLED_APPS`:

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
