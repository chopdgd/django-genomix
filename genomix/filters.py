# -*- coding: utf-8 -*-
from django.conf import settings
from django_filters import TypedChoiceFilter


class DisplayChoiceFilter(TypedChoiceFilter):

    def __init__(self, *args, **kwargs):
        empty_label = getattr(settings, 'NULL_CHOICE_LABEL', '---------')
        empty_value = getattr(settings, 'NULL_CHOICE_VALUE', None)

        choices = kwargs.pop('choices')
        kwargs['choices'] = [(empty_value, empty_label)] + [(y, y) for x, y in choices]
        kwargs['coerce'] = lambda x: getattr(choices, x)

        super(DisplayChoiceFilter, self).__init__(*args, **kwargs)
