# -*- coding: utf-8 -*-

import django_filters
from lmhsweb.models import Main, TYPE_CHOICES, SOURCES_CHOICES, Projet, Auteur
from django.db.models.fields import BLANK_CHOICE_DASH
from collections import Iterable
from itertools import chain
from re import search, sub
from django_filters.widgets import BaseCSVWidget, CSVWidget
from django_filters.fields import BaseCSVField
from dal import autocomplete


class MultiValueCharFilter(django_filters.BaseCSVFilter, django_filters.CharFilter):

    def filter(self, qs, value):
        # value is either a list or an 'empty' value
        values = value or []

        for value in values:
            qs = super(MultiValueCharFilter, self).filter(qs, value)

        return qs


class MainFilter(django_filters.FilterSet):

    PROJECT_CHOICES = Projet.objects.all().values_list("nom", "nom")
    PROJECT_CHOICES_FILTER = BLANK_CHOICE_DASH + list(PROJECT_CHOICES)
    TYPE_CHOICES_FILTER = BLANK_CHOICE_DASH + list(TYPE_CHOICES)
    SOURCES_CHOICES_FILTER = BLANK_CHOICE_DASH + list(SOURCES_CHOICES)

    titre = MultiValueCharFilter(widget= CSVWidget, name="titre", label='Titre', lookup_expr='icontains')
    #auteur__nom = MultiValueCharFilter(widget=CSVWidget, name="auteur__nom",label='Auteur', lookup_expr='icontains')
    auteur__nom = django_filters.CharFilter(label='Auteur', lookup_expr='icontains')
    mot_cle__nom = django_filters.CharFilter(label="Mot clé", lookup_expr='icontains')
    pdf_text = django_filters.CharFilter(label="Recherche PDF", lookup_expr='icontains')
    source_liste = django_filters.ChoiceFilter(name = 'source', label = "Source (choisir)", choices = SOURCES_CHOICES_FILTER, lookup_expr='icontains')
    source_texte = django_filters.CharFilter(name = 'source', label = "Source (écrire)", lookup_expr='icontains')
    date = django_filters.CharFilter(label="Date", lookup_expr='icontains')
    type = django_filters.ChoiceFilter(label="Type", choices=TYPE_CHOICES_FILTER, lookup_expr='icontains')
    projet__nom = django_filters.ChoiceFilter(label="Projet", choices=PROJECT_CHOICES_FILTER, lookup_expr='icontains')
    cote_calcul = django_filters.CharFilter(label = "Cote", lookup_expr='iexact')

    class Meta:
        model = Main
        fields = [
            'titre',
            'type',
            'source',
            'projet__nom',
            'auteur__nom',
            'mot_cle__nom',
            'date',
            'cote_calcul'
        ]
