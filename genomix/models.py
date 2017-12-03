# -*- coding: utf-8 -*-
from django.db import models
from django.utils.text import slugify

from model_utils.models import TimeStampedModel


class TimeStampedLabelModel(TimeStampedModel):
    """An abstract base class model that provides label, description, active."""
    label = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=50, unique=True)
    active = models.NullBooleanField(default=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.label

    def save(self, **kwargs):
        self.slug = slugify(self.label)
        super(TimeStampedLabelModel, self).save(**kwargs)
