# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

TYPE_CHOICES = (
    (
        "Affiche",
        "Affiche",
    ),
    (
        "Annonce de concours",
        "Annonce de concours",
    ),
    (
        "Article de périodique",
        "Article de périodique",
    ),
    (
        "Catalogue",
        "Catalogue",
    ),
    (
        "Conférence",
        "Conférence",
    ),
    (
        "Document non publié",
        "Document non publié",
    ),
    (
        "Extrait de livre",
        "Extrait de livre",
    ),
    (
        "Iconographie",
        "Iconographie",
    ),
    (
        "Livre",
        "Livre",
    ),
    (
        "Matériel audiovisuel",
        "Matériel audiovisuel",
    ),
    (
        "Partition",
        "Partition",
    ),
    (
        "Périodique",
        "Périodique",
    ),
    (
        "Photographie",
        "Photographie",
    ),
    (
        "Programme",
        "Programme",
    ),
    (
        "Référence",
        "Référence",
    ),
)

@python_2_unicode_compatible
class Auteur(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = "Auteur"

@python_2_unicode_compatible
class CoteAuteur(models.Model):
    cote = models.CharField(max_length=200, unique=True, null=True, default=None, blank=True)

    def __str__(self):
       return self.cote

    class Meta:
        verbose_name = "Cote auteur"

@python_2_unicode_compatible
class CotePrefixe(models.Model):
    cote = models.CharField(max_length=20, unique=True, null=True, default=None, blank=True)

    def __str__(self):
       return self.cote

    class Meta:
        verbose_name = "Cote prefixe"

@python_2_unicode_compatible
class Collection(models.Model):
    nom = models.CharField(max_length=20, unique=True)

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = "Collection"

@python_2_unicode_compatible
class Fonds(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = "Fonds"

@python_2_unicode_compatible
class Genre(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = "Genre"

@python_2_unicode_compatible
class LangueOrigine(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = "Langue d'origine"

@python_2_unicode_compatible
class City(models.Model):
    name = models.CharField("Nom de la ville", max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ville"
        verbose_name_plural = "Ville"

@python_2_unicode_compatible
class State(models.Model):
    name = models.CharField("Nom de la province", max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Province"
        verbose_name_plural = "Provinces"

@python_2_unicode_compatible
class Country(models.Model):
    name = models.CharField("Nom du pays", max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Pays"
        verbose_name_plural = "Pays"

@python_2_unicode_compatible
class Localisation(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = "Localisation"

@python_2_unicode_compatible
class TypeEvenement(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = "Type d'événement"

@python_2_unicode_compatible
class Projet(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = "Projet"


@python_2_unicode_compatible
class NomOrg(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = "Nom de l'organisme"

@python_2_unicode_compatible
class MethodeReproduction(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = "Méthode de réproduction"

@python_2_unicode_compatible
class MaisonEdition(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = "Maison d'édition"

@python_2_unicode_compatible
class Medium(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = "Medium"

@python_2_unicode_compatible
class DirecteurCollection(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = "Directeur de collection"

@python_2_unicode_compatible
class DirecteurPublication(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = "Directeur de publication"

@python_2_unicode_compatible
class Editeur(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = "Editeur"

@python_2_unicode_compatible
class MotCle(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = "Mot clé"

@python_2_unicode_compatible
class Support(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = "Support"

@python_2_unicode_compatible
class Traducteur(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = "Traducteur"

@python_2_unicode_compatible
class Main(models.Model):
    annee_1re_publication = models.IntegerField(blank=True, null=True)
    annee_enregistrement = models.IntegerField(blank=True, null=True)
    annee_production = models.IntegerField(blank=True, null=True)
    auteur = models.ManyToManyField('Auteur', null=True, blank=True)
    collection = models.ForeignKey("Collection", null=True, blank=True)
    commentaire = models.TextField(null=True, blank=True)
    cote_annee = models.CharField(blank=True, null=True, max_length=100)
    cote_auteur = models.ForeignKey("CoteAuteur", null=True, default=None, blank=True)
    cote_calcul = models.CharField(max_length=100, null=True, blank=True)
    cote_numero = models.CharField(blank=True, null=True, max_length=100)
    cote_prefixe = models.ForeignKey("CotePrefixe", blank=True, null=True, default=None)
    cote_calcul_url = models.CharField(max_length=20, null=True, blank=True)
    protection_droit_auteur = models.NullBooleanField(db_column='Protection_droit_auteur', blank=True, null=True, default=None)  # Field name made lowercase.
    date = models.CharField(blank=True, null=True, max_length=100)
    date_fin = models.CharField(blank=True, null=True, max_length=100)
    depouillement = models.TextField(null=True, blank=True)
    directeur_collection = models.ManyToManyField('DirecteurCollection', null=True, blank=True)
    directeur_publication = models.ManyToManyField('DirecteurPublication', null=True, blank=True)
    editeur = models.ManyToManyField('Editeur', null=True, blank=True, verbose_name="Éditeur")
    en_collection = models.CharField(blank=True, max_length=200)
    fonds = models.ForeignKey("Fonds", null=True, blank=True, verbose_name="Fonds")
    genre = models.ForeignKey("Genre", null=True, blank=True, verbose_name="Genre")
    instrumentation = models.TextField(null=True, blank=True)
    interprete = models.CharField(null=True, blank=True, max_length=200)
    langue_origine = models.ForeignKey("LangueOrigine", null=True, blank=True)
    lieu = models.CharField("Lieu", max_length=200, null=True, blank=True)
    lieu_conservation = models.CharField("Lieu de conservation", blank=True, max_length=200)
    localisation = models.ForeignKey("Localisation", null=True, blank=True)
    maison_edition = models.ForeignKey("MaisonEdition", null=True, blank=True)
    medium = models.ForeignKey("Medium", null=True, blank=True)
    methode_reproduction = models.ForeignKey("MethodeReproduction", null=True, blank=True)
    mot_cle = models.ManyToManyField('MotCle', null=True, blank=True)
    nb_exemplaire = models.IntegerField(blank=True, null=True)
    nb_page = models.CharField(blank=True, max_length=20)
    nb_volume = models.CharField(blank=True, max_length=20)
    no_page = models.CharField(blank=True, max_length=20)
    no_volume = models.CharField(blank=True, max_length=20)
    notice_id = models.CharField(max_length=100, null=True, blank=True)
    nom_org = models.ForeignKey("NomOrg", null=True, blank=True)
    projet = models.ForeignKey("Projet", null=True, blank=True)
    source = models.CharField(blank=True, max_length=200, null=True)
    sujet = models.TextField(null=True, blank=True)
    support = models.ManyToManyField('Support', null=True, blank=True)
    titre = models.CharField(max_length=100)
    traducteur = models.ManyToManyField('Traducteur', null=True, blank=True)

    # city = models.ForeignKey('City', null=True, blank=True)
    # state = models.ForeignKey('State', null=True, blank=True)
    # country = models.ForeignKey('Country', null=True, blank=True)

    type = models.CharField(
        choices=TYPE_CHOICES,
        max_length=100,
        null=False,
        verbose_name="Type"
    )

    type_evenement = models.ForeignKey("TypeEvenement", null=True, blank=True)

    def get_absolute_url(self):
        return reverse_lazy('notice', args=[self.id])

    def save(self):
        if self.cote_auteur:
            notice_id = self.cote_prefixe.cote + str(self.cote_auteur.cote)
            cote_calcul = self.cote_prefixe.cote + " " + str(self.cote_auteur.cote)
            cote_calcul_url = self.cote_prefixe.cote + "-" + str(self.cote_auteur.cote)
        else:
            notice_id = cote_calcul = cote_calcul_url = self.cote_prefixe.cote
        if self.cote_annee:
            notice_id = notice_id + str(self.cote_annee)
            cote_calcul = cote_calcul + " " + str(self.cote_annee)
            cote_calcul_url = cote_calcul_url + "-" + str(self.cote_annee)
        if self.cote_numero:
            notice_id = notice_id + str(self.cote_numero).zfill(2)
            cote_calcul = cote_calcul + " " + str(self.cote_numero).zfill(2)
            cote_calcul_url = cote_calcul_url + "-" + str(self.cote_numero).zfill(2)

        self.notice_id = notice_id
        self.cote_calcul = cote_calcul
        self.cote_calcul_url = cote_calcul_url

        print self.notice_id

        super(Main, self).save()

    class Meta:
        verbose_name = "Principale"

    def __str__(self):
        return self.titre
