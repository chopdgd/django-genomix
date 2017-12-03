from django.apps import apps

from genomix.apps import GenomixConfig


def test_apps():
    assert GenomixConfig.name == 'genomix'
    assert apps.get_app_config('genomix').name == 'genomix'
