#!/usr/bin/python
 # -*- coding: utf-8 -*-
from dal import autocomplete
from django import forms
from models import *


class Search(forms.ModelForm):
    recherche_pdf = forms.CharField(label="Recherche plein text")
    tousIndex_calcul = forms.CharField(label="Tous")
    auteur__nom = forms.CharField(label="Auteur")
    mot_cle__nom = forms.CharField(label="Mot-clé")

    class Meta:
        model = Main
        fields = ['auteur__nom', 'titre', 'date', 'mot_cle__nom', 'recherche_pdf', 'tousIndex_calcul', 'projet', 'type']


class Create(forms.ModelForm):

    #projet = forms.CharField(widget=forms.HiddenInput(), required=False)

    # langue_origine = forms.ModelChoiceField(
    #     queryset=LangueOrigine.objects.all(),
    #     widget=autocomplete.ModelSelect2(url='langue_origine-autocomplete')
    # )

    def __init__( self, type, *args, **kwargs ):
         super(Create, self).__init__( *args, **kwargs )
         self.fields['type'] = forms.CharField(widget=forms.HiddenInput(), initial=type)
    #     self.type = type
    #
    #     if self.type == "LivreX":
    #         del self.fields['annee_enregistrement']
    #         del self.fields['annee_production']
    #         del self.fields['cote_calcul']
    #         del self.fields['cote_calcul_url']
    #         del self.fields['date_fin']
    #         del self.fields['depouillement']
    #         del self.fields['en_collection']
    #         del self.fields['genre']
    #         del self.fields['instrumentation']
    #         del self.fields['interprete']
    #         del self.fields['lieu_conservation']
    #         del self.fields['localisation']
    #         del self.fields['medium']
    #         del self.fields['methode_reproduction']
    #         del self.fields['no_page']
    #         del self.fields['no_volume']
    #         del self.fields['notice_id']
    #         del self.fields['nom_org']
    #         del self.fields['projet']
    #         del self.fields['source']
    #         del self.fields['sujet']
    #         del self.fields['support']
    #         del self.fields['type_evenement']

    class Meta:
        model = Main

        fields = ('__all__')

        widgets = {
            'type_evenement': autocomplete.ModelSelect2('type_evenement-autocomplete'),
            'projet': autocomplete.ModelSelect2(url='projet-autocomplete'),
            'nom_org': autocomplete.ModelSelect2('nom_org-autocomplete'),
            'methode_reproduction': autocomplete.ModelSelect2('methode_reproduction-autocomplete'),
            'medium': autocomplete.ModelSelect2('medium-autocomplete'),
            'maison_edition': autocomplete.ModelSelect2('maison_edition-autocomplete'),
            'localisation': autocomplete.ModelSelect2('localisation-autocomplete'),
            'langue_origine': autocomplete.ModelSelect2('langue_origine-autocomplete'),
            'genre': autocomplete.ModelSelect2('genre-autocomplete'),
            'fonds': autocomplete.ModelSelect2('fonds-autocomplete'),
            'collection': autocomplete.ModelSelect2('collection-autocomplete'),
            'cote_prefixe': autocomplete.ModelSelect2('cote_prefixe-autocomplete'),
            'cote_auteur': autocomplete.ModelSelect2('cote_auteur-autocomplete'),
            'auteur': autocomplete.ModelSelect2Multiple('auteur-autocomplete'),
            'directeur_collection': autocomplete.ModelSelect2Multiple('directeur_collection-autocomplete'),
            'directeur_publication': autocomplete.ModelSelect2Multiple('directeur_publication-autocomplete'),
            'editeur': autocomplete.ModelSelect2Multiple('editeur-autocomplete'),
            'mot_cle': autocomplete.ModelSelect2Multiple('mot_cle-autocomplete'),
            'support': autocomplete.ModelSelect2Multiple('support-autocomplete'),
            'traducteur': autocomplete.ModelSelect2Multiple('traducteur-autocomplete'),
        }


