# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from genomix.urls import urlpatterns as genomix_urls

urlpatterns = [
    url(r'^', include(genomix_urls, namespace='genomix')),
]
