#!/usr/bin/python
 # -*- coding: utf-8 -*-
from dal import autocomplete
from django import forms
from django.db.models.fields import BLANK_CHOICE_DASH
from models import *
from django.utils.safestring import mark_safe


class Search(forms.ModelForm):
    pdf_text = forms.CharField(label="Recherche plein texte", required=False)
    tousIndex_calcul = forms.CharField(label="Tous", required=False)
    auteur__nom = forms.CharField(label="Auteur", required=False)
    titre = forms.CharField(label="Titre", required=False)

    PROJECT_CHOICES = Projet.objects.all().values_list("nom", "nom")
    CORPUS_CHOICES = Corpus.objects.values_list('nom','nom')

    projet__nom = forms.ChoiceField(widget=forms.Select,
                                    choices=BLANK_CHOICE_DASH + list(PROJECT_CHOICES), label="Projet", required=False)
    source_liste = forms.ChoiceField(widget=forms.Select,
                                     choices=BLANK_CHOICE_DASH + list(SOURCES_CHOICES), label='Source (choisir)', required=False)
    source_texte = forms.CharField(label="Source (écrire)", required=False)
    mot_cle__nom = forms.CharField(label="Mot-clé",
                                   help_text = mark_safe('Pour le projet "Esthétique musicale en France (1900-1950)", on peut se référer à cette <a href="https://docs.google.com/document/d/1g53UmT3EvQzWZBjj8L3y0jiUERFHTlp1RQq7hlDsoTA/edit?ts=59945456" target="_blank">'
                                                         'liste de mots clés</a> regroupés par catégories. <br>Pour le projet "Jazz dans la presse musicale française", on peut se référer à cette <a href="https://docs.google.com/document/d/17uadPoPP_xZLoxqsmPrqPptptoemvFFqiGrjkb5yjWo/edit?usp=sharing" target="_blank"> liste de mots clés</a> regroupés par catégories.'),
                                   required = False)
    corpus__nom = forms.ChoiceField(widget=forms.Select,
                                    choices=BLANK_CHOICE_DASH + list(CORPUS_CHOICES), label="Corpus", required=False)
    type = forms.ChoiceField(widget=forms.Select, choices = BLANK_CHOICE_DASH + list(TYPE_CHOICES), required=False)
    cote_calcul = forms.CharField(label="Cote", help_text='Ex. ART BARa 1928 01', required=False)

    class Meta:
        model = Main
        fields = [
                    'auteur__nom',
                    'titre', 'date',
                    'mot_cle__nom',
                    'corpus__nom',
                    'pdf_text',
                    'source_liste',
                    'source_texte',
                    'tousIndex_calcul',
                    'projet__nom',
                    'type',
                    'cote_calcul',
                  ]


class Create(forms.ModelForm):
    def __init__( self, type, *args, **kwargs ):
        super(Create, self).__init__(*args, **kwargs)
        self.fields['type'] = forms.CharField(widget=forms.HiddenInput(), initial=type)
        self.fields['pdf_file'] = forms.FileField(label='Sélectionnez le fichier PDF', required=False)

    class Meta:
        model = Main
        fields = '__all__'
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
            'corpus': autocomplete.ModelSelect2Multiple('corpus-autocomplete'),
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


STATUS_CHOICES = (
    ("Étudiant", "Étudiant"),
    ("Chercheur indépendant", "Chercheur indépendant"),
    ("Professeur", "Professeur"),
    ("Autre", "Autre")
)


class InscrireForm(forms.Form):
    nom = forms.CharField(label='Nom', required=True)
    prenom = forms.CharField(label='Prénom', required=True)
    institution = forms.CharField(label="Institution d'attache (institution et département)", required=True)
    statut = forms.ChoiceField(choices=BLANK_CHOICE_DASH + list(STATUS_CHOICES), required=True)
    statut_autre = forms.CharField(label="Autre, précisez", required=False)
    courriel = forms.EmailField(label='Adresse courriel', required=True)
    telephone = forms.CharField(label='Numéro de téléphone (optionnel)',required=False)
    raison = forms.CharField(widget=forms.Textarea, required=True, label="Raison de la demande")