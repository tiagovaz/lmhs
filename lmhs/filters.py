# -*- coding: utf-8 -*-

import django_filters
from lmhsweb.models import Main


class MainFilter(django_filters.FilterSet):
    class Meta:
        model = Main
        fields = [
        ]