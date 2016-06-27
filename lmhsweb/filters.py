# -*- coding: utf-8 -*-

import django_filters
from lmhsweb.models import Main, TYPE_CHOICES


class MainFilter(django_filters.FilterSet):

    TYPE_CHOICES_FILTER = [ ('', 'Tous')]
    TYPE_CHOICES_FILTER.extend(list(TYPE_CHOICES))

    titre = django_filters.CharFilter(label="Titre", lookup_expr='icontains')
    auteur__nom = django_filters.CharFilter(label="Auteur", lookup_expr='icontains')
    mot_cle__nom = django_filters.CharFilter(label="Mot clé", lookup_expr='icontains')
    type = django_filters.ChoiceFilter(label="Type", choices=TYPE_CHOICES_FILTER, lookup_expr='icontains')

    class Meta:
        model = Main
        fields = [
            'titre',
            'type',
            'projet',
            'auteur__nom',
            'mot_cle__nom',
            'date'
        ]