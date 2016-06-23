from django.contrib import admin

from lmhsweb.forms import MainAdminForm
from models import *


class MainAdmin(admin.ModelAdmin):
    form = MainAdminForm
admin.site.register(Main, MainAdmin)

admin.site.register(Auteur)
admin.site.register(Collection)
admin.site.register(Place)
admin.site.register(Fonds)
admin.site.register(Genre)
admin.site.register(LangueOrigine)
admin.site.register(Localisation)
admin.site.register(MaisonEdition)
admin.site.register(Medium)
admin.site.register(MethodeReproduction)
admin.site.register(NomOrg)
admin.site.register(Projet)
admin.site.register(TypeEvenement)
admin.site.register(DirecteurCollection)
admin.site.register(DirecteurPublication)
admin.site.register(Editeur)
admin.site.register(Support)
admin.site.register(Traducteur)
admin.site.register(City)
admin.site.register(State)
admin.site.register(Country)
admin.site.register(MotCle)
