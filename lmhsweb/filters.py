# -*- coding: utf-8 -*-

import django_filters
from lmhsweb.models import Main, TYPE_CHOICES, Projet
from django.db.models.fields import BLANK_CHOICE_DASH


'''class MultiValueCharFilter(django_filters.BaseCSVFilter, django_filters.CharFilter):
    def filter(self, qs, value):
        # value is either a list or an 'empty' value
        values = value or []

        for value in values:
            qs = super(MultiValueCharFilter, self).filter(qs, value)

        return qs
'''

class MainFilter(django_filters.FilterSet):
    PROJECT_CHOICES = Projet.objects.all().values_list("nom", "nom")
    PROJECT_CHOICES_FILTER = BLANK_CHOICE_DASH + list(PROJECT_CHOICES)
    TYPE_CHOICES_FILTER = BLANK_CHOICE_DASH + list(TYPE_CHOICES)

    titre = django_filters.CharFilter(label="Titre", lookup_expr='icontains', required=False)
    #auteur__nom = MultiValueCharFilter(label="Auteur", lookup_expr='icontains')
    auteur__nom = django_filters.CharFilter(label='Auteur', lookup_expr='icontains')
    mot_cle__nom = django_filters.CharFilter(label="Mot clé", lookup_expr='icontains')
    pdf_text = django_filters.CharFilter(label="Recherche PDF", lookup_expr='icontains')
    source = django_filters.CharFilter(label="Source", lookup_expr='icontains')
    date = django_filters.CharFilter(label="Date", lookup_expr='icontains')
    type = django_filters.ChoiceFilter(label="Type", choices=TYPE_CHOICES_FILTER, lookup_expr='icontains')
    projet__nom = django_filters.ChoiceFilter(label="Projet", choices=PROJECT_CHOICES_FILTER, lookup_expr='icontains')

    class Meta:
        model = Main
        fields = [
            'titre',
            'type',
            'source',
            'projet__nom',
            'auteur__nom',
            'mot_cle__nom',
            'date'
        ]
