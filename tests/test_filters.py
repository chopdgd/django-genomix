from django.utils.translation import ugettext_lazy as _

from model_utils import Choices
import pytest

from genomix import filters


def test_DisplayChoiceFilter():
    test_choices = Choices((1, 'TEST1', _('TEST1')),)
    test_filter = filters.DisplayChoiceFilter(choices=test_choices)
    assert test_filter.field.choices == [(None, '---------'), ('TEST1', 'TEST1')]
    assert test_filter.field.coerce('TEST1') == 1
