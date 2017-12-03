from django.test import TestCase

from mock import MagicMock
from rest_framework.routers import SimpleRouter

from genomix import routers


class TestDefaultRouter(TestCase):

    def setUp(self):
        self.DefaultRouter = routers.DefaultRouter()
        self.router = MagicMock(spec=SimpleRouter, registry=['url'])

    def test_extend(self):
        self.DefaultRouter.extend(self.router)
        assert self.DefaultRouter.registry == ['url']
