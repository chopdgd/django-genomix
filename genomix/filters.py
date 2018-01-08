# -*- coding: utf-8 -*-
from collections import OrderedDict

from django.conf import settings
from django_filters import TypedChoiceFilter


class DisplayChoiceFilter(TypedChoiceFilter):

    def __init__(self, *args, **kwargs):
        empty_label = getattr(settings, 'NULL_CHOICE_LABEL', '---------')
        empty_value = getattr(settings, 'NULL_CHOICE_VALUE', None)

        choices = kwargs.pop('choices')
        kwargs['choices'] = [(empty_value, empty_label)] + [(y, y) for x, y in choices]
        kwargs['coerce'] = lambda x: self.coerce(x, choices)

        super(DisplayChoiceFilter, self).__init__(*args, **kwargs)

    @staticmethod
    def coerce(x, choices):
        for key, value in OrderedDict(choices).items():
            if value.lower() == x.lower():
                return key
