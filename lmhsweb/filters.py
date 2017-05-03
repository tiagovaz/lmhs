# -*- coding: utf-8 -*-

import django_filters
from lmhsweb.models import Main, TYPE_CHOICES, Projet, Source
from django.db.models.fields import BLANK_CHOICE_DASH


class MainFilter(django_filters.FilterSet):

    PROJECT_CHOICES = Projet.objects.all().values_list("nom", "nom")
    PROJECT_CHOICES_FILTER = BLANK_CHOICE_DASH + list(PROJECT_CHOICES)
    TYPE_CHOICES_FILTER = BLANK_CHOICE_DASH
    TYPE_CHOICES_FILTER.extend(list(TYPE_CHOICES))
    SOURCES_CHOICES = Source.objects.all().values_list("nom", "nom")
    SOURCES_CHOICES_FILTER = BLANK_CHOICE_DASH + list(SOURCES_CHOICES)


    #PROJECT_CHOICES = Projet.objects.all().values_list("id", "nom")
    #PROJECT_CHOICES_FILTER = [('', 'Tous')]
    #PROJECT_CHOICES_FILTER.extend(list(PROJECT_CHOICES))
    titreList = titre.split(' ')
    for i in range(titreList.lenght):
        titreList[i] = django_filters.CharFilter(label="Titre", lookup_expr='icontains')
    auteur_list = auteur__nom.split(' ')
    for i in range(auteur_list.lenght):
        auteur_list[i] = django_filters.CharFilter(label="Auteur", lookup_expr='icontains')
#    projet__nom = django_filters.CharFilter(label="Projet", lookup_expr='icontains')
    mot_cle__nom = django_filters.CharFilter(label="Mot clé", lookup_expr='icontains')
    pdf_text = django_filters.CharFilter(label="Recherche PDF", lookup_expr='icontains')
    source = django_filters.ChoiceFilter(label="Source", choices=SOURCES_CHOICES_FILTER, lookup_expr='icontains')
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
