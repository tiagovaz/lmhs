#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import json

PYTHONIOENCODING='utf-8'

cote_auteur_list = []
cote_prefixe_list = []
type_evenement_list = []
author_list = ['Anonyme']
project_list = []
directeur_collection_list = []
directeur_publication_list = []
collection_list = []
editeur_list = []
traducteur_list = []
nom_org_list = []
mot_cle_list = []
support_list = []
fonds_list = []
genre_list = []
langue_origine_list = []
localisation_list = []
projet_list = []
nom_org_list = []
methode_reproduction_list = []
maison_edition_list = []
medium_list = []

count = 0

type_list = []
sources_list = []

with open('principal.csv', 'rb') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')

    with open('fixtures_principal.json', 'w') as fixtures_file:

        fixtures_file.write('[')
        for row in reader:
            
            main_fixture = {}
            fields = {}

            if row['type'] == 'Livre':
                for f in row:
                    if row[f] != "":
                        print f, row[f]
                        break
                    else:
                        print f, "None"
                        type_list.append(f)
            

##################
# Boolfields #
##################

            if row['Protection_droit_auteur']:
                if row['Protection_droit_auteur'] == "0":
                    fields['protection_droit_auteur'] = "False"
                else:
                    fields['protection_droit_auteur'] = "True"

##############
# Intfields #
##############

            if row['cote_annee']:
                fields['cote_annee'] = int(row['cote_annee'])

##############
# Charfields #
##############

            if row['commentaire']:
                fields['commentaire'] = row['commentaire']

            if row['cote_annee']:
                fields['cote_annee'] = row['cote_annee']

            if row['cote_numero']:
                fields['cote_numero'] = row['cote_numero']

            if row['cote_calcul']:
                fields['cote_calcul'] = row['cote_calcul']

            if row['cote_calcul_url']:
                fields['cote_calcul_url'] = row['cote_calcul_url']
               
            if row['notice_ID']:
                fields['notice_id'] = row['notice_ID']

            if row['date']:
                fields['date'] = row['date']
                
            if row['date_fin']:
                fields['date_fin'] = row['date_fin']
                
            if row['depouillement']:
                fields['depouillement'] = row['depouillement']
                
            if row['en_collection']:
                fields['en_collection'] = row['en_collection']
                
            if row['instrumentation']:
                fields['instrumentation'] = row['instrumentation']
                
            if row['interprete']:
                fields['interprete'] = row['interprete']
                
            if row['lieu_conservation']:
                fields['lieu_conservation'] = row['lieu_conservation']
                
            if row['nb_exemplaire']:
                fields['nb_exemplaire'] = row['nb_exemplaire']
                
            if row['nb_page']:
                fields['nb_page'] = row['nb_page']
                
            if row['no_page']:
                fields['no_page'] = row['no_page']                

            if row['source']:
                fields['source'] = row['source']
                
            if row['sujet']:
                fields['sujet'] = row['sujet']
                
            if row['titre']:
                fields['titre'] = row['titre']
                
            if row['type']:
                fields['type'] = row['type']
                
#######################
# Many-to-many fields #
#######################

            nom_org_string = row['nom_org']
            nom_org_split = nom_org_string.splitlines()
            row_nom_org = [a.strip() for a in nom_org_split if a]

            if row_nom_org:
                for nom_org in row_nom_org:
                    if nom_org not in nom_org_list:
                        nom_org_list.append(nom_org)
                        nom_org_id = nom_org_list.index(nom_org)+1
                        nom_org_fixture = """
{
  "model": "lmhsweb.nomorg",
  "pk": %d,
  "fields":
  {
    "nom": "%s"
  }
},""" % (nom_org_id,nom_org)
                        fixtures_file.write(nom_org_fixture)

                fields['nom_org'] = [nom_org_list.index(nom_org)+1 for nom_org in row_nom_org]

            traducteur_string = row['traducteur']
            traducteur_split = traducteur_string.splitlines()
            row_traducteur = [a.strip() for a in traducteur_split if a]

            if row_traducteur:
                for traducteur in row_traducteur:
                    if traducteur not in traducteur_list:
                        traducteur_list.append(traducteur)
                        traducteur_id = traducteur_list.index(traducteur)+1
                        traducteur_fixture = """
{
  "model": "lmhsweb.traducteur",
  "pk": %d,
  "fields":
  {
    "nom": "%s"
  }
},""" % (traducteur_id,traducteur)
                        fixtures_file.write(traducteur_fixture)

                fields['traducteur'] = [traducteur_list.index(traducteur)+1 for traducteur in row_traducteur]

# ===========


            support_string = row['support']
            support_split = support_string.splitlines()
            row_support = [a.strip() for a in support_split if a]

            if row_support:
                for support in row_support:
                    if support not in support_list:
                        support_list.append(support)
                        support_id = support_list.index(support)+1
                        support_fixture = """
{
  "model": "lmhsweb.support",
  "pk": %d,
  "fields":
  {
    "nom": "%s"
  }
},""" % (support_id,support)
                        fixtures_file.write(support_fixture)

                fields['support'] = [support_list.index(support)+1 for support in row_support]

# ===========

            authors_string = row['auteur']
            authors_split = authors_string.split(';')
            row_authors = [a.strip() for a in authors_split if a]

            if row_authors:
                for author in row_authors:
                    if author not in author_list:
                        author_list.append(author)
                        author_id = author_list.index(author)+1
                        author_fixture = """
{
  "model": "lmhsweb.auteur",
  "pk": %d,
  "fields":
  {
    "nom": "%s"
  }
},""" % (author_id,author)
                        fixtures_file.write(author_fixture)

                fields['auteur'] = [author_list.index(author)+1 for author in row_authors]
# ===========

            projects_string = row['projet']
            projects_split = projects_string.split(';')
            row_projects = [a.strip() for a in projects_split if a]

            if row_projects:
                for project in row_projects:
                    if project not in project_list:
                        project_list.append(project)
                        project_id = project_list.index(project)+1
                        project_fixture = """
{
  "model": "lmhsweb.projet",
  "pk": %d,
  "fields":
  {
    "nom": "%s"
  }
},""" % (project_id,project)
                        fixtures_file.write(project_fixture)

                fields['projet'] = [project_list.index(project)+1 for project in row_projects]


# ===========


            mot_cle_string = row['mot_cle']
            mot_cle_split = mot_cle_string.split(';')
            row_mot_cle = [a.strip().strip('"') for a in mot_cle_split if a]

            if row_mot_cle:
                for mot_cle in row_mot_cle:
                    if mot_cle not in mot_cle_list:
                        mot_cle_list.append(mot_cle)
                        mot_cle_id = mot_cle_list.index(mot_cle)+1
                        mot_cle_fixture = """
{
  "model": "lmhsweb.motcle",
  "pk": %d,
  "fields":
  {
    "nom": "%s"
  }
},""" % (mot_cle_id, mot_cle)
                        fixtures_file.write(mot_cle_fixture)

                fields['mot_cle'] = [mot_cle_list.index(mot_cle)+1 for mot_cle in row_mot_cle]

# ===========

            editeur_string = row['editeur']
            editeur_split = editeur_string.split(';')
            row_editeur = [a.strip() for a in editeur_split if a]

            if row_editeur:
                for editeur in row_editeur:
                    if editeur not in editeur_list:
                        editeur_list.append(editeur)
                        editeur_id = editeur_list.index(editeur)+1
                        editeur_fixture = """
{
  "model": "lmhsweb.editeur",
  "pk": %d,
  "fields":
  {
    "nom": "%s"
  }
},""" % (editeur_id,editeur)
                        fixtures_file.write(editeur_fixture)

                fields['editeur'] = [editeur_list.index(editeur)+1 for editeur in row_editeur]

# ===========

            directeur_collection_string = row['directeur_collection']
            directeur_collection_split = directeur_collection_string.split(';')
            row_directeur_collection = [a.strip() for a in directeur_collection_split if a]


            if row_directeur_collection:
                for directeur_collection in row_directeur_collection:
                    if directeur_collection not in directeur_collection_list:
                        directeur_collection_list.append(directeur_collection)
                        directeur_collection_id = directeur_collection_list.index(directeur_collection)+1
                        directeur_collection_fixture = """
{
  "model": "lmhsweb.directeurcollection",
  "pk": %d,
  "fields":
  {
    "nom": "%s"
  }
},""" % (directeur_collection_id, directeur_collection)
                        fixtures_file.write(directeur_collection_fixture)

                fields['directeur_collection'] = [directeur_collection_list.index(directeur_collection)+1 for directeur_collection in row_directeur_collection]

# ==========

            directeur_publication_string = row['directeur_publication']
            directeur_publication_split = directeur_publication_string.split(';')
            row_directeur_publication = [a.strip() for a in directeur_publication_split if a]

            if row_directeur_publication:
                for directeur_publication in row_directeur_publication:
                    if directeur_publication not in directeur_publication_list:
                        directeur_publication_list.append(directeur_publication)
                        directeur_publication_id = directeur_publication_list.index(directeur_publication)+1
                        directeur_publication_fixture = """
{
  "model": "lmhsweb.directeurpublication",
  "pk": %d,
  "fields":
  {
    "nom": "%s"
  }
},""" % (directeur_publication_id, directeur_publication)
                        fixtures_file.write(directeur_publication_fixture)

                fields['directeur_publication'] = [directeur_publication_list.index(directeur_publication)+1 for directeur_publication in row_directeur_publication]

#######################
# Foreign-key fields #
#######################
            cote_prefixe = row['cote_prefixe'].strip()
            if cote_prefixe.strip():
                if cote_prefixe not in cote_prefixe_list:
                    cote_prefixe_list.append(cote_prefixe)
                    cote_prefixe_id = cote_prefixe_list.index(cote_prefixe)+1
                    cote_prefixe_fixture = """
{
  "model": "lmhsweb.coteprefixe",
  "pk": %d,
  "fields":
  {
    "cote": "%s"
  }
},""" % (cote_prefixe_id,cote_prefixe.strip())

                    fixtures_file.write(cote_prefixe_fixture)
                fields['cote_prefixe'] = cote_prefixe_id

            cote_auteur = row['cote_auteur'].strip()
            if cote_auteur.strip():
                if cote_auteur not in cote_auteur_list:
                    cote_auteur_list.append(cote_auteur)
                    cote_auteur_id = cote_auteur_list.index(cote_auteur)+1
                    cote_auteur_fixture = """
{
  "model": "lmhsweb.coteauteur",
  "pk": %d,
  "fields":
  {
    "cote": "%s"
  }
},""" % (cote_auteur_id,cote_auteur.strip())

                    fixtures_file.write(cote_auteur_fixture)
                fields['cote_auteur'] = cote_auteur_id

            type_evenement = row['type_evenement']
            if type_evenement.strip():
                if type_evenement not in type_evenement_list:
                    type_evenement_list.append(type_evenement)
                    type_evenement_id = type_evenement_list.index(type_evenement)+1
                    type_evenement_fixture = """
{
  "model": "lmhsweb.typeevenement",
  "pk": %d,
  "fields":
  {
    "nom": "%s"
  }
},""" % (type_evenement_id,type_evenement.strip())

                    fixtures_file.write(type_evenement_fixture)
                fields['type_evenement'] = type_evenement_id

            collection = row['collection']
            if collection.strip():
                if collection not in collection_list:
                    collection_list.append(collection)
                    collection_id = collection_list.index(collection)+1
                    collection_fixture = """
{
  "model": "lmhsweb.collection",
  "pk": %d,
  "fields":
  {
    "nom": "%s"
  }
},""" % (collection_id,collection.strip())

                    fixtures_file.write(collection_fixture)
                fields['collection'] = collection_id

            fonds = row['fonds']
            if fonds.strip():
                if fonds not in fonds_list:
                    fonds_list.append(fonds)
                    fonds_id = fonds_list.index(fonds)+1
                    fonds_fixture = """
{
  "model": "lmhsweb.fonds",
  "pk": %d,
  "fields":
  {
    "nom": "%s"
  }
},""" % (fonds_id,fonds.strip())

                    fixtures_file.write(fonds_fixture)
                fields['fonds'] = fonds_id

            genre = row['genre']
            if genre.strip():
                if genre not in genre_list:
                    genre_list.append(genre)
                    genre_id = genre_list.index(genre)+1
                    genre_fixture = """
{
  "model": "lmhsweb.genre",
  "pk": %d,
  "fields":
  {
    "nom": "%s"
  }
},""" % (genre_id,genre.strip())

                    fixtures_file.write(genre_fixture)
                fields['genre'] = genre_id

            langue_origine = row['langue_origine']
            if langue_origine.strip():
                if langue_origine not in langue_origine_list:
                    langue_origine_list.append(langue_origine)
                    langue_origine_id = langue_origine_list.index(langue_origine)+1
                    langue_origine_fixture = """
{
  "model": "lmhsweb.langueorigine",
  "pk": %d,
  "fields":
  {
    "nom": "%s"
  }
},""" % (langue_origine_id,langue_origine.strip())

                    fixtures_file.write(langue_origine_fixture)
                fields['langue_origine'] = langue_origine_id
                     
            localisation = row['localisation']
            if localisation.strip():
                if localisation not in localisation_list:
                    localisation_list.append(localisation)
                    localisation_id = localisation_list.index(localisation)+1
                    localisation_fixture = """
{
  "model": "lmhsweb.localisation",
  "pk": %d,
  "fields":
  {
    "nom": "%s"
  }
},""" % (localisation_id,localisation.strip())

                    fixtures_file.write(localisation_fixture)
                fields['localisation'] = localisation_id
                     
            methode_reproduction = row['methode_reproduction'].strip()
            if methode_reproduction.strip():
                if methode_reproduction not in methode_reproduction_list:
                    methode_reproduction_list.append(methode_reproduction)
                    methode_reproduction_id = methode_reproduction_list.index(methode_reproduction)+1
                    methode_reproduction_fixture = """
{
  "model": "lmhsweb.methodereproduction",
  "pk": %d,
  "fields":
  {
    "nom": "%s"
  }
},""" % (methode_reproduction_id,methode_reproduction.strip())

                    fixtures_file.write(methode_reproduction_fixture)
                fields['methode_reproduction'] = methode_reproduction_id
                     
            maison_edition = row['maison_edition']
            if maison_edition.strip():
                if maison_edition not in maison_edition_list:
                    maison_edition_list.append(maison_edition)
                    maison_edition_id = maison_edition_list.index(maison_edition)+1
                    maison_edition_fixture = """
{
  "model": "lmhsweb.maisonedition",
  "pk": %d,
  "fields":
  {
    "nom": "%s"
  }
},""" % (maison_edition_id,maison_edition.strip())

                    fixtures_file.write(maison_edition_fixture)
                fields['maison_edition'] = maison_edition_id

            medium = row['medium']
            if medium.strip():
                if medium not in medium_list:
                    medium_list.append(medium)
                    medium_id = medium_list.index(medium)+1
                    medium_fixture = """
{
  "model": "lmhsweb.medium",
  "pk": %d,
  "fields":
  {
    "nom": "%s"
  }
},""" % (medium_id,medium.strip())

                    fixtures_file.write(medium_fixture)
                fields['medium'] = medium_id

            if fields:
                count += 1
                main_fixture['model'] = "lmhsweb.main"
                main_fixture['pk'] = count
                main_fixture['fields'] = fields
                fixtures_file.write('\n')
                fixtures_file.write(json.JSONEncoder().encode(main_fixture))
                fixtures_file.write(',')

#            main_fixture = """
#{
#  "model": "lmhsweb.main",
#  "pk": 1,
#  "fields":
#  {
#    "collection": %d,
#    "commentaire": "%s",
#    "cote_annee": %s,
#    "cote_numero": %s,
#    "cote_prefixe": "%s",
#    "protection_droit_auteur": %s,
#    "date": "%s",
#    "date_fin": "%s",
#    "depouillement": "%s",
#    "en_collection": "%s",
#    "fonds": %d,
#    "genre": %d,
#    "instrumentation": "%s",
#    "interprete": "%s",
#    "langue_origine": %d,
#    "lieu_conservation": "%s",
#    "localisation": %d,
#    "maison_edition": %d,
#    "medium": %d,
#    "methode_reproduction": %d,
#    "nb_exemplaire": %s,
#    "nb_page": "%s",
#    "no_page": "%s",
#    "nom_org": %d,
#    "projet": %d,
#    "source": "%s",
#    "sujet": "%s",
#    "titre": "%s",
#    "type": "%s",
#    "type_evenement": "%s",
#    "auteur": [%s],
#    "directeur_collection": [%s],
#    "directeur_publication": [%s],
#    "editeur": [%s],
#    "mot_cle": [%s],
#    "support": [%s],
#    "traducteur": [%s]
#  }
#},""" % (collection_id,commentaire,cote_annee,cote_numero,
#         cote_prefixe,protection_droit_auteur,date,date_fin,
#         depouillement,en_collection,fonds_id,genre_id,
#         instrumentation,interprete,langue_origine_id,
#         lieu_conservation,localisation_id,maison_edition_id,medium_id,
#         methode_reproduction_id,nb_exemplaire,nb_page,
#         no_page,nom_org_id,projet_id,source,sujet,
#         titre,type,type_evenement,authors_ids,
#         "",
#         "",
#         "",
#         "",
#         "", 
#         "")
#
#            fixtures_file.write(main_fixture)
#

        fixtures_file.seek(fixtures_file.tell()-1)
        fixtures_file.write('\n]')

print list(set(type_list))


