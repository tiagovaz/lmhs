# -*- coding: utf-8 -*-

import django_filters
from lmhsweb.models import Main, TYPE_CHOICES, Projet

class MainFilter(django_filters.FilterSet):

    TYPE_CHOICES_FILTER = [ ('', 'Tous')]
    TYPE_CHOICES_FILTER.extend(list(TYPE_CHOICES))

    #PROJECT_CHOICES = Projet.objects.all().values_list("id", "nom")
    #PROJECT_CHOICES_FILTER = [('', 'Tous')]
    #PROJECT_CHOICES_FILTER.extend(list(PROJECT_CHOICES))

    titre = django_filters.CharFilter(label="Titre", lookup_expr='icontains')
    auteur__nom = django_filters.CharFilter(label="Auteur", lookup_expr='icontains')
    projet__nom = django_filters.CharFilter(label="Projet", lookup_expr='icontains')
    mot_cle__nom = django_filters.CharFilter(label="Mot clé", lookup_expr='icontains')
    pdf_text = django_filters.CharFilter(label="Recherche PDF", lookup_expr='icontains')
    source = django_filters.CharFilter(label="Source", lookup_expr='icontains')
    type = django_filters.ChoiceFilter(label="Type", choices=TYPE_CHOICES_FILTER, lookup_expr='icontains')

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
