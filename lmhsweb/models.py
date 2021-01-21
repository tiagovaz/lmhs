# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
import os
from django.conf import settings


COTE_PREFIXE_LISTE = [
    ["Affiche","A"],
    ["Annonce de concours","CONC"],
    ["Article de périodique","ART"],
    ["Catalogue","CAT"],
    ["Conférence","CONF"],
    ["Document non publié","DNP"],
    ["Extrait de livre","EXT"],
    ["Iconographie","ICO"],
    ["Livre","L"],
    ["Matériel audiovisuel","MA"],
    ["Partition","MUS"],
    ["Périodique","PER"],
    ["Photographie","ICO"],
    ["Programme","PROG"],
    ["Référence","REF"]
]


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

# cette liste sert uniquement à la recherche (filters)
SOURCES_CHOICES = (
    (
        "L'Action française",
        "L'Action française"
    ),
    (
        "Angers-artiste",
        "Angers-artiste"
    ),
    (
        "Comoedia illustré",
        "Comoedia illustré"
    ),
    (
        "Contrepoints",
        "Contrepoints"
    ),
    (
        "Courrier musical",
        "Courrier musical"
    ),
    (
        "Le Courrier Musical et Théâtral",
        "Le Courrier Musical et Théâtral"
    ),
    (
        "Le courrier Musical, Théâtral, Cinématographique",
        "Le courrier Musical, Théâtral, Cinématographique"
    ),
    (
        "Le Devoir",
        "Le Devoir"
    ),
    (
        "L'Écho de Paris",
        "L'Écho de Paris"
    ),
    (
        "Europe",
        "Europe"
    ),
    (
        "Jazz Hot",
        "Jazz Hot"
    ),
    (
        "Le Figaro",
        "Le Figaro"
    ),
    (
        "Le Gaulois",
        "Le Gaulois"
    ),
    (
        "Le Guide du concert",
        "Le Guide du concert"
    ),
    (
        "L'Intransigeant",
        "L'Intransigeant"
    ),
    (
        "Journal des débats",
        "Journal des débats"
    ),
    (
        "Mémoire et Histoire : la Résistance",
        "Mémoire et Histoire : la Résistance"
    ),
    (
        "Le Ménestrel",
        "Le Ménestrel"
    ),
    (
        "Mercure de France",
        "Mercure de France"
    ),
    (
        "Le Mercure musical",
        "Le Mercure musical"
    ),
    (
        "Modern Music",
        "Modern Music"
    ),
    (
        "Le Monde musical",
        "Le Monde musical"
    ),
    (
        "Musique,", # La virgule (,) évite de faire sortir tous les sources contenant 'Musique'
        "Musique"
    ),
    (
        "La Musique pendant la guerre",
        "La Musique pendant la guerre"
    ),
    (
        "Le Petit Journal",
        "Le Petit Journal"
    ),
    (
        "Le Petit Parisien",
        "Le Petit Parisien"
    ),
    (
        "La Presse",
        "La Presse"
    ),
    (
        "La Revue musicale,",
        "La Revue musicale"
    ),
    (
        "La Revue musicale de Lyon",
        "La Revue musicale de Lyon"
    ),
    (
        "Revue musicale de Suisse Romande",
        "Revue musicale de Suisse Romande"
    ),
    (
        "Revue musicale (histoire et critique)",
        "Revue musicale (histoire et critique)"
    ),
    (
        "Revue musicale SIM",
        "Revue musicale SIM"
    ),
     (
        "Revue Pleyel",
        "Revue Pleyel"
    ),
    (
        "Revue bleue",
        "La Revue politique et littéraire «Revue bleue»"
    ),
    (
        "La Revue de Paris",
        "La Revue de Paris"
    ),
    (
        "Le Temps",
        "Le Temps"
    ),
)


@python_2_unicode_compatible
class Auteur(models.Model):
    nom = models.CharField(max_length=200, unique=False)
    cote = models.CharField(max_length=200, unique=False, null=True, default=None, blank=True)

    def __str__(self):
       if self.cote:
           return self.nom + " (" + self.cote + ")"
       else:
           return self.nom

    class Meta:
        verbose_name = "Auteur"


@python_2_unicode_compatible
class CoteAuteur(models.Model):
    cote = models.CharField(max_length=200, unique=False, null=True, default=None, blank=True)
#    auteur = models.ForeignKey("Auteur", null=True, blank=True, unique=False)

    def __str__(self):
       return self.cote

    class Meta:
        verbose_name = "Cote auteur"
        verbose_name_plural = "Cotes auteurs"


@python_2_unicode_compatible
class CotePrefixe(models.Model):
    cote = models.CharField(max_length=20, unique=False, null=True, default=None, blank=True)

    def __str__(self):
       return self.cote

    class Meta:
        verbose_name = "Cote préfixe"
        verbose_name_plural = "Cotes préfixes"


@python_2_unicode_compatible
class Collection(models.Model):
    nom = models.CharField(max_length=20, unique=True)

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = "Collection"


@python_2_unicode_compatible
class Corpus(models.Model):
    nom = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Corpus"
        verbose_name_plural = "Corpus"


@python_2_unicode_compatible
class Fonds(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = "Fond"


@python_2_unicode_compatible
class Genre(models.Model):
    nom = models.CharField(max_length=200, unique=False)

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
        verbose_name_plural = "Langues d'origines"


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
        verbose_name_plural = "Types d'événements"


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
        verbose_name_plural = "Noms d'organismes"


@python_2_unicode_compatible
class MethodeReproduction(models.Model):
    nom = models.CharField(max_length=200, unique=False)

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = "Méthode de reproduction"
        verbose_name_plural = "Méthodes de reproductions"


@python_2_unicode_compatible
class MaisonEdition(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = "Maison d'édition"
        verbose_name_plural = "Maisons d'éditions"


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
        verbose_name_plural = "Directeurs de collections"


@python_2_unicode_compatible
class DirecteurPublication(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = "Directeur de publication"
        verbose_name_plural = "Directeurs de publications"


@python_2_unicode_compatible
class Editeur(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = "Editeur"


@python_2_unicode_compatible
class MotCle(models.Model):
    nom = models.CharField(max_length=200, unique=False)

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = "Mot clé"
        verbose_name_plural = "Mots clés"


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
class Utilisateur(models.Model):
    user_pk = models.PositiveIntegerField()
    nom = models.CharField(max_length=100)
    institution = models.CharField(max_length=400)
    statut = models.CharField(max_length=400)
    courriel = models.EmailField(max_length=254)
    telephone = models.CharField(max_length=50, null=True, blank=True)
    raison = models.TextField()
    date = models.DateField(auto_now_add=True)
    etat = models.CharField(max_length = 20, default="En attente", verbose_name="État de la demande")

    def __str__(self):
        return self.nom + " (" + str(self.user_pk) + ")"


@python_2_unicode_compatible
class Main(models.Model):
    annee_1re_publication = models.IntegerField(blank=True, null=True)
    annee_enregistrement = models.IntegerField(blank=True, null=True)
    annee_production = models.IntegerField(blank=True, null=True)
    auteur = models.ManyToManyField('Auteur', blank=True, verbose_name="Auteur(s)")
    cote_auteur = models.ForeignKey("Auteur", null=True, default=None, blank=True, related_name="Cote_Auteur")
    collection = models.ForeignKey("Collection", null=True, blank=True)
    corpus = models.ManyToManyField('Corpus', blank=True)
    commentaire = models.TextField(null=True, blank=True)
    cote_annee = models.CharField(blank=True, null=True, max_length=100)
    cote_calcul = models.CharField(max_length=100, null=True, blank=True)
    cote_numero = models.CharField(blank=True, null=True, max_length=100)
    cote_prefixe = models.ForeignKey("CotePrefixe", blank=True, null=True, default=None, editable = False)
    cote_calcul_url = models.CharField(max_length=50, null=True, blank=True, editable = False)
    protection_droit_auteur = models.NullBooleanField(db_column='Protection_droit_auteur', blank=True, null=True, default=None)  # Field name made lowercase.
    date = models.CharField(blank=True, null=True, max_length=100)
    date_ajout = models.DateTimeField(null=True, editable = False, auto_now_add = True)
    date_fin = models.CharField(blank=True, null=True, max_length=100)
    depouillement = models.TextField(null=True, blank=True)
    directeur_collection = models.ManyToManyField('DirecteurCollection', blank=True)
    directeur_publication = models.ManyToManyField('DirecteurPublication', blank=True)
    editeur = models.ManyToManyField('Editeur', blank=True, verbose_name="Éditeur")
    en_collection = models.TextField(blank=True, null=True)
    fonds = models.ForeignKey("Fonds", null=True, blank=True, verbose_name="Fonds")
    genre = models.ForeignKey("Genre", null=True, blank=True, verbose_name="Genre")
    instrumentation = models.TextField(null=True, blank=True)
    interprete = models.CharField(null=True, blank=True, max_length=200)
    langue_origine = models.ForeignKey("LangueOrigine", null=True, blank=True)
    lien = models.URLField("Lien vers l'article", blank = True)
    lieu = models.CharField("Lieu", max_length=200, null=True, blank=True)
    lieu_conservation = models.CharField("Lieu de conservation", blank=True, max_length=200)
    localisation = models.ForeignKey("Localisation", null=True, blank=True)
    maison_edition = models.ForeignKey("MaisonEdition", null=True, blank=True)
    medium = models.ForeignKey("Medium", null=True, blank=True)
    methode_reproduction = models.ForeignKey("MethodeReproduction", null=True, blank=True)
    mot_cle = models.ManyToManyField('MotCle', blank=True)
    nb_exemplaire = models.IntegerField(blank=True, null=True)
    nb_page = models.CharField(blank=True, max_length=20)
    nb_volume = models.CharField(blank=True, max_length=20)
    no_page = models.CharField(blank=True, max_length=20)
    no_volume = models.CharField(blank=True, max_length=20)
    notice_id = models.CharField(max_length=100, null=True, blank=True, editable = False)
    nom_org = models.ManyToManyField("NomOrg", blank=True)
    projet = models.ManyToManyField("Projet",  blank=True)
    source = models.CharField(blank=True, max_length=200, null=True)
    sujet = models.TextField(null=True, blank=True)
    support = models.ManyToManyField('Support', blank=True)
    titre = models.CharField(max_length=600)
    traducteur = models.ManyToManyField('Traducteur', blank=True)

    pdf_file = models.FileField(upload_to='public/documents',
                                blank=True,
                                null=True
                                )
    pdf_prive = models.BooleanField(default = False, verbose_name="PDF seulement accessible aux utilisateurs connectés")
    pdf_text = models.TextField(blank=True, null=True)



    type = models.CharField(
        choices=TYPE_CHOICES,
        max_length=100,
        null=False,
        verbose_name="Type"
    )

    type_evenement = models.ForeignKey("TypeEvenement", null=True, blank=True)

    def convert_pdf_to_txt(self, path):
        rsrcmgr = PDFResourceManager()
        retstr = StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
        fp = file(path, 'rb')
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        password = ""
        maxpages = 0
        caching = True
        pagenos=set()
        for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
            interpreter.process_page(page)
        fp.close()
        device.close()
        str = retstr.getvalue()
        retstr.close()
        return str

    __original_pdf_file_name = None

    def __init__(self, *args, **kwargs):
        super(Main, self).__init__(*args, **kwargs)
        self.__original_pdf_file_name = self.pdf_file.name

    def save(self):
        resave_pdf = False
        if self.pdf_file.name != self.__original_pdf_file_name:
            resave_pdf = True

        # build cotes
        for cote in COTE_PREFIXE_LISTE:
            if cote[0] == self.type:
                self.cote_prefixe = CotePrefixe.objects.get(cote=cote[1])
    
        if self.cote_auteur.cote != None:
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
        super(Main, self).save()

        if self.pdf_file:
            # si pas privé, enregistrer le pdf dans le dossier public (et renommer)
            if not self.pdf_prive:
                os.rename(os.path.join(settings.MEDIA_ROOT, self.pdf_file.name), os.path.join(settings.MEDIA_ROOT, "public/documents", self.cote_calcul_url+".pdf"))
                self.pdf_file.name = "public/documents/" + self.cote_calcul_url + ".pdf"

            # sinon (si privé) enregistrer le pdf dans le dossier privé (et renommer)
            else:
                os.rename(os.path.join(settings.MEDIA_ROOT, self.pdf_file.name),
                          os.path.join(settings.MEDIA_ROOT, "prive/documents", self.cote_calcul_url + ".pdf"))
                self.pdf_file.name = "prive/documents/" + self.cote_calcul_url + ".pdf"

            # extract pdf text.
            if self.pdf_text == "" or resave_pdf == True:
                if self.pdf_file:
                    self.pdf_text = self.convert_pdf_to_txt(str(os.path.join(settings.MEDIA_ROOT, self.pdf_file.name)))

        # save 'mots-clés'
#        if self.mot_cle:
#            mot_cle_list = self.mot_cle.split(";")
#            self.mot_cle.add(*MotCle.objects.filter(nom__in=mot_cle_list))

        super(Main, self).save()

    class Meta:
        verbose_name = "Principale"

    def __str__(self):
        return self.titre
