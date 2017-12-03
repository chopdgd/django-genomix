from django.contrib.contenttypes.models import ContentType
from django.test import TestCase
from django.utils.translation import ugettext_lazy as _

from mock import MagicMock
from model_mommy import mommy
from model_utils import Choices
import pytest

from genomix import fields


@pytest.fixture()
def DisplayChoiceField():
    choices = Choices(
        (0, 'choice', _('Choice')),
    )
    return fields.DisplayChoiceField(choices=choices)


@pytest.fixture()
def UserRelatedField():
    return fields.UserRelatedField(read_only=True)


@pytest.fixture()
def ContentRelatedField():
    return fields.ContentRelatedField(read_only=True)


@pytest.fixture()
def User():
    return mommy.make(
        'auth.User',
        id=1,
        username='username',
    )


class FieldTestCase(TestCase):
    field = None

    def test_to_representation(self):
        if self.field:
            assert self.field.to_representation(self.internal_value) == self.display_value

    def test_to_representation_failure(self):
        if self.field:
            with pytest.raises(Exception):
                self.field.to_representation(self.bad_internal_value)

    def test_to_internal_value(self):
        if self.field:
            assert self.field.to_internal_value(self.display_value) == self.internal_value

    def test_to_internal_value_failure(self):
        if self.field:
            with pytest.raises(Exception):
                self.field.to_internal_value(self.bad_display_value)


class TestDisplayChoiceField(FieldTestCase):

    def setUp(self):
        self.field = DisplayChoiceField()
        self.internal_value = 0
        self.bad_internal_value = 1
        self.display_value = 'Choice'
        self.bad_display_value = "NA"


class TestUserRelatedField(FieldTestCase):

    def setUp(self):
        self.field = UserRelatedField()
        self.internal_value = User()
        self.bad_internal_value = MagicMock(spec=User(), id=99)
        self.display_value = 'username'
        self.bad_display_value = 'bad-username'


class TestContentRelatedField(FieldTestCase):

    def setUp(self):
        self.field = ContentRelatedField()
        self.internal_value = ContentType.objects.create(id=99, model='model', app_label='app_label')
        self.bad_internal_value = MagicMock(spec=ContentType(), id=100)
        self.display_value = 'model'
        self.bad_display_value = 'bad-model'
