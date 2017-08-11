"""lmhs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.contrib.auth import views as auth_views
from lmhsweb.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^delete/(?P<pk>\d+)/$', NoticeDelete.as_view(), name="delete_notice"),
    url(r'^deleteauteur/(?P<pk>\d+)/$', AuteurDelete.as_view(), name="delete_auteur"),
    url(r'^deletemotcle/(?P<pk>\d+)/$', MotCleDelete.as_view(), name="delete_motcle"),

    url(r'^admin/', admin.site.urls),
    url(
      r'^list/$',
      MainList.as_view(),
      name='event_list'
    ),
    url(
      r'^$',
      SearchForm.as_view(),
      name='event'
    ),

    url('^login/$', auth_views.LoginView.as_view(), name='login'),
    url('^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^search/$', SearchForm.as_view()),
    url(r'^create/(?P<type>\w{0,50})$', CreateForm.as_view()),
    url(r'^update/(?P<pk>\d+)/$', UpdateForm.as_view(), name='update'),
    url(r'^type_evenement-autocomplete/$', TypeEvenementAutocomplete.as_view(), name='type_evenement-autocomplete', ),
    url(r'^auteur-autocomplete/$', AuteurAutocomplete.as_view(), name='auteur-autocomplete', ),
    url(r'^cote_prefixe-autocomplete/$', CotePrefixeAutocomplete.as_view(), name='cote_prefixe-autocomplete', ),
    url(r'^directeur_collection-autocomplete/$', DirecteurCollectionAutocomplete.as_view(), name='directeur_collection-autocomplete', ),
    url(r'^directeur_publication-autocomplete/$', DirecteurPublicationAutocomplete.as_view(), name='directeur_publication-autocomplete', ),
    url(r'^editeur-autocomplete/$', EditeurAutocomplete.as_view(), name='editeur-autocomplete', ),
    url(r'^mot_cle-autocomplete/$', MotCleAutocomplete.as_view(), name='mot_cle-autocomplete', ),
    url(r'^support-autocomplete/$', SupportAutocomplete.as_view(), name='support-autocomplete', ),
    url(r'^traducteur-autocomplete/$', TraducteurAutocomplete.as_view(), name='traducteur-autocomplete', ),
    url(r'^collection-autocomplete/$', CollectionAutocomplete.as_view(), name='collection-autocomplete', ),
    url(r'^fonds-autocomplete/$', FondsAutocomplete.as_view(), name='fonds-autocomplete', ),
    url(r'^genre-autocomplete/$', GenreAutocomplete.as_view(), name='genre-autocomplete', ),
    url(r'^langue_origine-autocomplete/$', LangueOrigineAutocomplete.as_view(), name='langue_origine-autocomplete', ),
    url(r'^localisation-autocomplete/$', LocalisationAutocomplete.as_view(), name='localisation-autocomplete', ),
    url(r'^maison_edition-autocomplete/$', MaisonEditionAutocomplete.as_view(), name='maison_edition-autocomplete', ),
    url(r'^medium-autocomplete/$', MediumAutocomplete.as_view(), name='medium-autocomplete', ),
    url(r'^methode_reproduction-autocomplete/$', MethodeReproductionAutocomplete.as_view(), name='methode_reproduction-autocomplete', ),
    url(r'^nom_org-autocomplete/$', NomOrgAutocomplete.as_view(), name='nom_org-autocomplete', ),
    url(r'^projet-autocomplete/$', ProjetAutocomplete.as_view(), name='projet-autocomplete', ),
    url(r'^gerer_auteurs/$', GererAuteurs.as_view(), name='gerer_auteurs'),
    url(r'^gerer_motcles/$', GererMotsCles.as_view(), name='gerer_motcles'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
