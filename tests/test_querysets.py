from django.test import TestCase
from genomix import querysets
import pytest


class QuerySetTestCase(TestCase):
    queryset = None

    def test_raises_exception(self):
        if self.queryset:
            with pytest.raises(Exception):
                self.queryset.update()


class TestUpdateDisabledQuerySet(QuerySetTestCase):

    def setUp(self):
        self.queryset = querysets.UpdateDisabledQuerySet
        self.test_raises_exception
