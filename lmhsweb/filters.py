# -*- coding: utf-8 -*-

import django_filters
from lmhsweb.models import Main


class MainFilter(django_filters.FilterSet):
    titre = django_filters.CharFilter(label="Titre", lookup_expr='icontains')

    class Meta:
        model = Main
        fields = [
            'titre',
            'type',
            'support',
        ]