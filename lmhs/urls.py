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
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, \
    password_reset_confirm, password_reset_complete
from lmhsweb.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^delete/(?P<pk>\d+)/$', admin.views.decorators.staff_member_required(NoticeDelete.as_view()), name="delete_notice"),
    url(r'^delete_auteur/(?P<pk>\d+)/$', admin.views.decorators.staff_member_required(AuteurDelete.as_view()), name="delete_auteur"),
    url(r'^delete_motcle/(?P<pk>\d+)/$', admin.views.decorators.staff_member_required(MotCleDelete.as_view()), name="delete_motcle"),
    url(r'^delete_projet/(?P<pk>\d+)/$', admin.views.decorators.staff_member_required(ProjetDelete.as_view()), name="delete_motcle"),
    url(r'^delete_corpus/(?P<pk>\d+)/$', admin.views.decorators.staff_member_required(CorpusDelete.as_view()), name="delete_corpus"),

    url(r'^admin/', admin.site.urls),
    url(r'^list/$',MainList.as_view(),name='event_list'),
    url(r'^$',SearchForm.as_view(),name='event'),
    url(r'^login/',login, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name="logout"),
    url(r'^search/$', SearchForm.as_view()),
    url(r'^create/(?P<type>\w{0,50})$', CreateForm.as_view()),
    url(r'^update/(?P<pk>\d+)/$', UpdateForm.as_view(), name='update'),

    url(r'^inscription/$', inscription, name='inscription'),
    url(r'^inscription/erreur/$', TemplateView.as_view(template_name='inscription/inscrition_erreur.html')),
    url(r'^inscription/succes/$', TemplateView.as_view(template_name='inscription/inscription_succes.html')),
    url(r'^utilisateur/(?P<pk>[0-9]+)/$', UserDetail.as_view(), name='user_detail'),
    url(r'^accepter/(?P<pk>[0-9]+)/$', acceptation_utilisateur, name='acceptation_utilisateur'),
    url(r'^refuser/(?P<pk>[0-9]+)/$', refus_utilisateur, name='refus_utilisateur'),

    url(r'^password_reset/$', password_reset, name='password_reset'),
    url(r'^password_reset/done/$', password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', password_reset_complete, name='password_reset_complete'),

    url(r'^gerer_auteurs/$', GererAuteurs.as_view(), name='gerer_auteurs'),
    url(r'^gerer_motcle/$', GererMotsCles.as_view(), name='gerer_motcle'),
    url(r'^gerer_projet/$', GererProjets.as_view(), name='gerer_projet'),
    url(r'^gerer_utilisateurs/$', GererUtilisateurs.as_view(),name='gerer_utilisateurs'),
    url(r'^gerer_corpus/$', GererCorpus.as_view(), name='gerer_corpus'),

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
    url(r'^corpus-autocomplete/$', CorpusAutocomplete.as_view(), name='corpus-autocomplete', ),

    url(r'^motcle_autocomplete/$', SearchAutocompleteMotCle.as_view(), name="autocomplete-motcle-search"),
    url(r'^auteur_autocomplete/$', SearchAutocompleteAuteur.as_view(), name="autocomplete-auteur-search"),

    url(r'^media/prive/documents/(?P<file>.*)$', serve_protected_document, name='serve_protected_document'),
    url(r'^media/(?P<file>.*)$', media_redirect, name='media_redirect')


              ] + static(settings.MEDIA_URL + "public/", document_root=settings.MEDIA_ROOT + "/public/")