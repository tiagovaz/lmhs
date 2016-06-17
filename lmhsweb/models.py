# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Auteur(models.Model):
    cote_auteur = models.CharField(max_length=20)
    nom_auteur = models.CharField(max_length=200)

    def __str__(self):
       return self.nom_auteur

    class Meta:
        verbose_name = "Auteur"

@python_2_unicode_compatible
class Collection(models.Model):
    nom = models.CharField(max_length=20)

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = "Collection"

@python_2_unicode_compatible
class Fonds(models.Model):
    nom = models.CharField(max_length=200)

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = "Fonds"

@python_2_unicode_compatible
class Genre(models.Model):
    nom = models.CharField(max_length=200)

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = "Genre"

@python_2_unicode_compatible
class LangueOrigine(models.Model):
    nom = models.CharField(max_length=200)

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = "Langue d'origine"

@python_2_unicode_compatible
class City(models.Model):
    name = models.CharField("Nom de la ville", max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ville"
        verbose_name_plural = "Ville"

@python_2_unicode_compatible
class State(models.Model):
    name = models.CharField("Nom de la province", max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Province"
        verbose_name_plural = "Provinces"

@python_2_unicode_compatible
class Country(models.Model):
    name = models.CharField("Nom du pays", max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Pays"
        verbose_name_plural = "Pays"

@python_2_unicode_compatible
class Place(models.Model):
    venue = models.CharField("Lieu", max_length=200)
    city = models.ForeignKey('City', null=True)
    state = models.ForeignKey('State', null=True)
    country = models.ForeignKey('Country', null=True)

    def __str__(self):
        #return "%s, %s, %s, %s" % (self.venue, self.city, self.province, self.country)
        return self.venue

    class Meta:
        verbose_name = "Lieu"
        verbose_name_plural = "Lieu"

@python_2_unicode_compatible
class Localisation(models.Model):
    nom = models.CharField(max_length=200)

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = "Localisation"

@python_2_unicode_compatible
class Type(models.Model):
    nom = models.CharField(max_length=200)

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = "Type"


@python_2_unicode_compatible
class TypeEvenement(models.Model):
    nom = models.CharField(max_length=200)

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = "Type d'événement"

@python_2_unicode_compatible
class Projet(models.Model):
    nom = models.CharField(max_length=200)

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = "Projet"


@python_2_unicode_compatible
class NomOrg(models.Model):
    nom = models.CharField(max_length=200)

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = "Nom de l'organisme"

@python_2_unicode_compatible
class MethodeReproduction(models.Model):
    nom = models.CharField(max_length=200)

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = "Méthode de réproduction"

@python_2_unicode_compatible
class MaisonEdition(models.Model):
    nom = models.CharField(max_length=200)

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = "Maison d'édition"

@python_2_unicode_compatible
class Medium(models.Model):
    nom = models.CharField(max_length=200)

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = "Medium"

@python_2_unicode_compatible
class DirecteurCollection(models.Model):
    nom = models.CharField(max_length=200)

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = "Directeur de collection"

@python_2_unicode_compatible
class DirecteurPublication(models.Model):
    nom = models.CharField(max_length=200)

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = "Directeur de publication"

@python_2_unicode_compatible
class Editeur(models.Model):
    nom = models.CharField(max_length=200)

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = "Editeur"

@python_2_unicode_compatible
class MotCle(models.Model):
    nom = models.CharField(max_length=200)

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = "Mot clé"

@python_2_unicode_compatible
class Support(models.Model):
    nom = models.CharField(max_length=200)

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = "Support"

@python_2_unicode_compatible
class Traducteur(models.Model):
    nom = models.CharField(max_length=200)

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = "Traducteur"

@python_2_unicode_compatible
class Main(models.Model):
    annee_1re_publication = models.IntegerField(blank=True, null=True)
    annee_enregistrement = models.IntegerField(blank=True, null=True)
    annee_production = models.IntegerField(blank=True, null=True)
    auteur = models.ManyToManyField('Auteur')
    collection = models.ForeignKey("Collection", null=True)
    commentaire = models.TextField(null=True)
    cote_annee = models.IntegerField()
    cote_numero = models.IntegerField(blank=True, null=True)
    cote_prefixe = models.CharField(max_length=20)
    protection_droit_auteur = models.BooleanField(db_column='Protection_droit_auteur', blank=True, default=False)  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)
    date_fin = models.DateField(blank=True, null=True)
    depouillement = models.TextField(null=True)
    directeur_collection = models.ManyToManyField('DirecteurCollection')
    directeur_publication = models.ManyToManyField('DirecteurPublication')
    editeur = models.ManyToManyField('Editeur')
    en_collection = models.CharField(blank=True, max_length=200)
    fonds = models.ForeignKey("Fonds", null=True)
    genre = models.ForeignKey("Genre", null=True)
    instrumentation = models.TextField(null=True)
    interprete = models.CharField(null=True, max_length=200)
    langue_origine = models.ForeignKey("LangueOrigine", null=True)
    lieu = models.ForeignKey("Place", null=True)
    lieu_conservation = models.CharField(blank=True, max_length=200)
    localisation = models.ForeignKey("Localisation", null=True)
    maison_edition = models.ForeignKey("MaisonEdition", null=True)
    medium = models.ForeignKey("Medium", null=True)
    methode_reproduction = models.ForeignKey("MethodeReproduction", null=True)
    mot_cle = models.ManyToManyField('MotCle')
    nb_exemplaire = models.IntegerField(blank=True, null=True)
    nb_page = models.CharField(blank=True, max_length=20)
    nb_volume = models.CharField(blank=True, max_length=20)
    no_page = models.CharField(blank=True, max_length=20)
    no_volume = models.CharField(blank=True, max_length=20)
    nom_org = models.ForeignKey("NomOrg", null=True)
    projet = models.ForeignKey("Projet", null=True)
    source = models.CharField(blank=True, max_length=200)
    sujet = models.TextField(null=True)
    support = models.ManyToManyField('Support')
    titre = models.CharField(blank=True, max_length=50)
    traducteur = models.ManyToManyField('Traducteur')
    type = models.ForeignKey("Type", null=True)
    type_evenement = models.ForeignKey("TypeEvenement", null=True)

    class Meta:
        verbose_name = "Principale"

    def __str__(self):
        return self.titre
