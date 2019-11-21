# -*- coding: utf-8 -*-
from django.db.models import QuerySet
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class UpdateDisabledQuerySet(QuerySet):
    def update(self, *args, **kwargs):
        raise ValidationError(_('Update method is disabled'), code='disabled')
