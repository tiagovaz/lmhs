# -*- coding: utf-8 -*-

import django_filters
from lmhsweb.models import Main, TYPE_CHOICES, Projet, Auteur
from django.db.models.fields import BLANK_CHOICE_DASH
from collections import Iterable
from itertools import chain
from re import search, sub
from django_filters.widgets import BaseCSVWidget, CSVWidget
from django_filters.fields import BaseCSVField
from dal import autocomplete


from django import forms
from django.forms.utils import flatatt
from django.utils.datastructures import MultiValueDict
from django.utils.encoding import force_text
from django.utils.http import urlencode
from django.utils.safestring import mark_safe
from django.utils.six import string_types
from django.utils.translation import ugettext as _
from django_filters.compat import format_value


class MultiValueCharFilter(django_filters.BaseCSVFilter, django_filters.CharFilter):
    #field_class = django_filters.fields.BaseCSVField

    def filter(self, qs, value):
        # value is either a list or an 'empty' value
        values = value or []

        for value in values:
            qs = super(MultiValueCharFilter, self).filter(qs, value)

        return qs


'''SOURCES_CHOICES = [
    "Courrier musical",
    "Europe",
    "Le Guide du concert",
    "Le Ménestrel",
    "Mercure de France",
    "Le Mercure musical",
    "Modern Music",
    "Le Monde musical",
    "Musique",
    "La Musique pendant la guerre",
    "La Revue musicale",
    "Revue musicale de Suisse Romande",
    "Revue musicale (histoire et critique)",
    "Revue musicale SIM",
    "Revue Pleyel",
    "La Revue politique et littéraire «Revue bleue»",
    "Le Temps",
] '''



class MainFilter(django_filters.FilterSet):
    dal_fields = {'auteur__nom': 'auteur-autocomplete'}


    PROJECT_CHOICES = Projet.objects.all().values_list("nom", "nom")
    PROJECT_CHOICES_FILTER = BLANK_CHOICE_DASH + list(PROJECT_CHOICES)
    TYPE_CHOICES_FILTER = BLANK_CHOICE_DASH + list(TYPE_CHOICES)
    #SOURCES_CHOICES_FILTER = BLANK_CHOICE_DASH + SOURCES_CHOICES

    titre = MultiValueCharFilter(widget= CSVWidget, name="titre", label='Titre', lookup_expr='icontains')
    #titre = django_filters.CharFilter(label="Titre", lookup_expr='icontains', required=False)
    #auteur__nom = MultiValueCharFilter(widget=CSVWidget, name="auteur__nom",label='Auteur', lookup_expr='icontains')
    auteur__nom = django_filters.CharFilter(label='Auteur', lookup_expr='icontains')
    mot_cle__nom = django_filters.CharFilter(label="Mot clé", lookup_expr='icontains')
    pdf_text = django_filters.CharFilter(label="Recherche PDF", lookup_expr='icontains')
    #source = django_filters.ChoiceFilter(label="Source", choices = SOURCES_CHOICES_FILTER, lookup_expr='icontains')
    source = django_filters.CharFilter(label="Source", lookup_expr='icontains')
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
