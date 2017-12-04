from collections import OrderedDict

from django.apps import apps
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import serializers


class DisplayChoiceField(serializers.ChoiceField):
    """A custom serializer field to use for a choice field."""

    def __init__(self, *args, **kwargs):
        choices = kwargs.get('choices')
        self._choices = OrderedDict(choices)
        super(DisplayChoiceField, self).__init__(*args, **kwargs)

    def to_representation(self, value):
        """Convert a choice internal value to the representation value

        Args:
            value (int): Internal value

        Returns:
            str: Representation value
        """
        try:
            return self._choices[value]
        except KeyError:
            raise Exception('Value: {0} not valid!'.format(value))

    def to_internal_value(self, value):
        """Convert a choice representation value to an internal value

        Args:
            value (str): Representation value

        Returns:
            int: Internal value
        """
        for key, key_value in self._choices.items():
            if key_value.strip().lower() == value.strip().lower():
                return key

        raise Exception('Value: {0} not supported!'.format(value))


class UserRelatedField(serializers.RelatedField):
    """A custom serializer field to use for the `user` relationship."""

    def to_representation(self, value):
        """Convert a User instance to representation (model)

        Args:
            value: User model instance

        Returns:
            str: username
        """
        model = apps.get_model(getattr(settings, 'AUTH_USER_MODEL'))
        try:
            return str(model.objects.get(id=value.id))
        except ObjectDoesNotExist:
            raise Exception('User Id: {0} not found!'.format(value.id))

    def to_internal_value(self, value):
        """Convert a username to a User model instance

        Args:
            value (str): username

        Returns:
            User: User model instance
        """
        model = apps.get_model(getattr(settings, 'AUTH_USER_MODEL'))
        try:
            return model.objects.get(username=value)
        except ObjectDoesNotExist:
            raise Exception('Username: {0} not found!'.format(value))


class ContentRelatedField(serializers.RelatedField):
    """A custom serializer field to use for the `content_type` generic relationship."""

    def to_representation(self, value):
        """Convert a ContentType instance to representation (model)

        Args:
            value: ContentType model instance

        Returns:
            str: model
        """
        try:
            return str(ContentType.objects.get(id=value.id))
        except ObjectDoesNotExist:
            raise Exception('ContentType Id: {0} not found!'.format(value.id))

    def to_internal_value(self, value):
        """Convert a model to a ContentType model instance

        Args:
            value (str): model

        Returns:
            ContentType: ContentType model instance
        """
        try:
            return ContentType.objects.get(model=value.replace(" ", "").lower())
        except ObjectDoesNotExist:
            raise Exception('ContentType Model: {0} not found!'.format(value))
