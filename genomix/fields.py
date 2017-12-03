from collections import OrderedDict

from django.apps import apps
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import serializers


class DisplayChoiceField(serializers.ChoiceField):

    def __init__(self, *args, **kwargs):
        choices = kwargs.get('choices')
        self._choices = OrderedDict(choices)
        super(DisplayChoiceField, self).__init__(*args, **kwargs)

    def to_representation(self, value):
        try:
            return self._choices[value]
        except KeyError:
            raise Exception('Value: {0} not valid!'.format(value))

    def to_internal_value(self, value):
        for key, key_value in self._choices.items():
            if key_value.strip().lower() == value.strip().lower():
                return key

        raise Exception('Value: {0} not supported!'.format(value))


class UserRelatedField(serializers.RelatedField):

    def to_representation(self, value):
        model = apps.get_model(getattr(settings, 'AUTH_USER_MODEL'))
        try:
            return str(model.objects.get(id=value.id))
        except ObjectDoesNotExist:
            raise Exception('User Id: {0} not found!'.format(value.id))

    def to_internal_value(self, value):
        model = apps.get_model(getattr(settings, 'AUTH_USER_MODEL'))
        try:
            return model.objects.get(username=value)
        except ObjectDoesNotExist:
            raise Exception('Username: {0} not found!'.format(value))


class ContentRelatedField(serializers.RelatedField):
    """
    A custom field to use for the `tagged_object` generic relationship.
    """

    def to_representation(self, value):
        try:
            return str(ContentType.objects.get(id=value.id))
        except ObjectDoesNotExist:
            raise Exception('ContentType Id: {0} not found!'.format(value.id))

    def to_internal_value(self, value):
        try:
            return ContentType.objects.get(model=value.replace(" ", "").lower())
        except ObjectDoesNotExist:
            raise Exception('ContentType Model: {0} not found!'.format(value))
