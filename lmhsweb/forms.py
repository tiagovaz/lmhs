#!/usr/bin/python
 # -*- coding: utf-8 -*-
from dal import autocomplete
from django import forms
from models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field, Div


class Search(forms.ModelForm):
    recherche_pdf = forms.CharField(label="Recherche plein text")
    tousIndex_calcul = forms.CharField(label="Tous")
    auteur = forms.CharField(label="Auteur")
    mot_cle = forms.CharField(label="Mot-clé")

    class Meta:
        model = Main
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Search, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper = FormHelper()
        self.helper.form_method = 'GET'
        self.helper.form_action = '/list/'
        self.helper.add_input(Submit('submit', 'Chercher'))
        self.helper.layout = Layout (
                    Div(
                            Div( 'auteur', css_class='col-sm-6'),
                            Div( 'recherche_pdf', css_class='col-sm-6'),
                            css_class='row'
                    ),
                    Div(

                            Div( 'titre', css_class='col-sm-6'),
                            Div( 'tousIndex_calcul', css_class='col-sm-6'),
                            css_class='row'
                    ),
                    Div(
                            Div( 'date', css_class='col-sm-6'),
                            Div( 'projet', css_class='col-sm-6'),
                            css_class='row'
                    ),
                    Div(
                            Div( 'mot_cle', css_class='col-sm-6'),
                            Div( 'type', css_class='col-sm-6'),
                            css_class='row'
                    ),
            )


class MainAdminForm(forms.ModelForm):
    class Meta:
        model = Main
        fields = ('__all__')
        widgets = {
            'type_evenement': autocomplete.ModelSelect2('type_evenement-autocomplete'),
            'projet': autocomplete.ModelSelect2('projet-autocomplete'),
            'nom_org': autocomplete.ModelSelect2('nom_org-autocomplete'),
            'methode_reproduction': autocomplete.ModelSelect2('methode_reproduction-autocomplete'),
            'medium': autocomplete.ModelSelect2('medium-autocomplete'),
            'maison_edition': autocomplete.ModelSelect2('maison_edition-autocomplete'),
            'localisation': autocomplete.ModelSelect2('localisation-autocomplete'),
            'lieu': autocomplete.ModelSelect2('lieu-autocomplete'),
            'langue_origine': autocomplete.ModelSelect2('langue_origine-autocomplete'),
            'genre': autocomplete.ModelSelect2('genre-autocomplete'),
            'fonds': autocomplete.ModelSelect2('fonds-autocomplete'),
            'collection': autocomplete.ModelSelect2('collection-autocomplete'),
            'auteur': autocomplete.ModelSelect2Multiple('auteur-autocomplete'),
            'directeur_collection': autocomplete.ModelSelect2Multiple('directeur_collection-autocomplete'),
            'directeur_publication': autocomplete.ModelSelect2Multiple('directeur_publication-autocomplete'),
            'editeur': autocomplete.ModelSelect2Multiple('editeur-autocomplete'),
            'mot_cle': autocomplete.ModelSelect2Multiple('mot_cle-autocomplete'),
            'support': autocomplete.ModelSelect2Multiple('support-autocomplete'),
            'traducteur': autocomplete.ModelSelect2Multiple('traducteur-autocomplete'),
        }

