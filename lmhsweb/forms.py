#!/usr/bin/python
 # -*- coding: utf-8 -*-
from dal import autocomplete
from django import forms
from django.db.models.fields import BLANK_CHOICE_DASH
from models import *


class Search(forms.ModelForm):
    pdf_text = forms.CharField(label="Recherche plein texte")
    tousIndex_calcul = forms.CharField(label="Tous")
    auteur__nom = forms.CharField(label="Auteur")

    PROJECT_CHOICES = Projet.objects.all().values_list("nom", "nom")

    projet__nom = forms.ChoiceField(widget=forms.Select, choices=BLANK_CHOICE_DASH + list(PROJECT_CHOICES), required=False, label="Projet")
    mot_cle__nom = forms.CharField(label="Mot-clé")

    class Meta:
        model = Main
        fields = ['auteur__nom', 'titre', 'date', 'mot_cle__nom', 'pdf_text', 'source', 'tousIndex_calcul', 'projet__nom', 'type']

class Create(forms.ModelForm):

    def __init__( self, type, *args, **kwargs ):
         super(Create, self).__init__( *args, **kwargs )
         self.fields['type'] = forms.CharField(widget=forms.HiddenInput(), initial=type)
         self.fields['pdf_file'] = forms.FileField(label='Sélectionnez le fichier PDF')
    class Meta:
        model = Main
        fields = ('__all__')
        widgets = {
            'type_evenement': autocomplete.ModelSelect2('type_evenement-autocomplete'),
            'projet': autocomplete.ModelSelect2Multiple(url='projet-autocomplete'),
            'nom_org': autocomplete.ModelSelect2Multiple('nom_org-autocomplete'),
            'methode_reproduction': autocomplete.ModelSelect2('methode_reproduction-autocomplete'),
            'medium': autocomplete.ModelSelect2('medium-autocomplete'),
            'maison_edition': autocomplete.ModelSelect2('maison_edition-autocomplete'),
            'localisation': autocomplete.ModelSelect2('localisation-autocomplete'),
            'langue_origine': autocomplete.ModelSelect2('langue_origine-autocomplete'),
            'genre': autocomplete.ModelSelect2('genre-autocomplete'),
            'fonds': autocomplete.ModelSelect2('fonds-autocomplete'),
            'collection': autocomplete.ModelSelect2('collection-autocomplete'),
            'cote_prefixe': autocomplete.ModelSelect2('cote_prefixe-autocomplete'),
#            'cote_auteur': autocomplete.ModelSelect2('cote_auteur-autocomplete'),
            'auteur': autocomplete.ModelSelect2Multiple('auteur-autocomplete'),
            'directeur_collection': autocomplete.ModelSelect2Multiple('directeur_collection-autocomplete'),
            'directeur_publication': autocomplete.ModelSelect2Multiple('directeur_publication-autocomplete'),
            'editeur': autocomplete.ModelSelect2Multiple('editeur-autocomplete'),
            'mot_cle': autocomplete.ModelSelect2Multiple('mot_cle-autocomplete'),
            'pdf_file': forms.FileField(label='Sélectionnez le fichier PDF'),
            'support': autocomplete.ModelSelect2Multiple('support-autocomplete'),
            'traducteur': autocomplete.ModelSelect2Multiple('traducteur-autocomplete'),
        }


