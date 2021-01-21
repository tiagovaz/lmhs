# -*- coding: utf-8 -*-
from dal import autocomplete
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import generic

from django.db.models import Q
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy, resolve

from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
from django.contrib.auth.models import User

from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.http import FileResponse, HttpResponse

from lmhsweb.filters import MainFilter
from lmhsweb.forms import Search, Create, InscrireForm
from lmhsweb.models import *

from operator import itemgetter
import os
import json


class NoticeDelete(DeleteView):
    model = Main
    success_url = reverse_lazy('event') # This is where this view will redirect the user


class AuteurDelete(DeleteView):
    model = Auteur
    success_url = reverse_lazy('gerer_auteurs')


class MotCleDelete(DeleteView):
    model = MotCle
    success_url = reverse_lazy('gerer_motcle')


class ProjetDelete(DeleteView):
    model = Projet
    success_url = reverse_lazy('gerer_projet')


class CorpusDelete(DeleteView):
    model = Corpus
    success_url = reverse_lazy('gerer_corpus')


class MainList(generic.View):
    def get(self, request):

        sort = request.GET.get('sort', 'date')
        orders = [sort, 'no_page']

        data = MainFilter(self.request.GET, queryset=Main.objects.all().order_by(*orders))
        data_total = data.qs.count()
        all_main_registers = MainFilter(self.request.GET, queryset=Main.objects.all().order_by('date'))
        #all_main_registers = MainFilter(self.request.GET, queryset=Main.objects.all().order_by(*orders))

        paginator = Paginator(data.qs, 25)
        page = request.GET.get('page')
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)
        return render(request, 'result.html', {'items': items, 'all': all_main_registers, 'form' : all_main_registers.form, 'data_total' : data_total})


class SearchForm(generic.View):
    def get(self, request):
        search_form = Search()
        return render(request, 'search.html', {'form': search_form})

    def post(self, request):
        pass


class CreateForm(generic.CreateView):
    model = Main
    template_name = 'create.html'
    form_class = Create

    def get_form_kwargs(self):
        kwargs = super(CreateForm, self).get_form_kwargs()
        kwargs['type'] = self.request.GET.get('type', '')
        return kwargs

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(CreateForm, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return '/list/?cote_calcul=' + self.object.cote_calcul


class UpdateForm(generic.UpdateView):
    model = Main
    template_name = "update.html"
    form_class = Create
    #fields = ('__all__')

    def get_form_kwargs(self):
        kwargs = super(UpdateForm, self ).get_form_kwargs()
        kwargs['type'] = self.request.GET.get('type', '')
        return kwargs

    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        main = get_object_or_404(
            Main,
            id=kwargs['pk']
        )
        return super(UpdateForm, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return '/list/'


class Login(generic.TemplateView):
    template_name = 'registration/login.html'


def inscription(request):
    form_class = InscrireForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            nom = request.POST.get('nom', '')
            prenom = request.POST.get('prenom', '')
            institution = request.POST.get('institution', '')
            statut = request.POST.get('statut', '')
            statut_autre = request.POST.get('statut_autre','')
            courriel = request.POST.get('courriel', '')
            telephone = request.POST.get('telephone', '')
            raison = request.POST.get('raison', '')

            utilisateurs_existants = []
            for i in User.objects.all():
                utilisateurs_existants.append(i.username)

            if courriel not in utilisateurs_existants:

                user = User.objects.create_user(courriel, email=courriel, password=User.objects.make_random_password(),
                                                is_active=False)
                user.first_name = prenom
                user.last_name = nom
                user.is_staff = False
                user.save()
                if statut != "Autre":
                    utilisateur = Utilisateur(user_pk=user.pk,nom=prenom + " " + nom, institution=institution,
                                              statut=statut,courriel=courriel,telephone=telephone,raison=raison)
                else:
                    utilisateur = Utilisateur(user_pk=user.pk, nom=prenom + " " + nom, institution=institution,
                                              statut=statut_autre, courriel=courriel, telephone=telephone, raison=raison)
                utilisateur.save()

                template = get_template('inscription/inscription_email_template.txt')

                context = {
                    'nom': nom,
                    'prenom': prenom,
                    'institution': institution,
                    'statut' : statut,
                    'statut_autre' : statut_autre,
                    'courriel' : courriel,
                    'telephone' : telephone,
                    'raison' : raison,
                    'pk' : user.pk,
                    'domain' : get_current_site(request).domain
                }
                content = template.render(context)

                email = EmailMessage(
                    "Nouvelle demande d'inscription à la banque de donnée du lmhs",
                    content,
                    'connectionlmhs@gmail.com',
                    ['c.campeaubedford@hotmail.com']
                    # ['judy-ann.desrosiers@umontreal.ca']
                )
                email.send()
                return redirect('/inscription/succes')
            else:
                return redirect('/inscription/erreur')
        else:
            return redirect('/inscription/erreur')

    return render(request, 'inscription/inscription_form.html', {'form': form_class})


class UserDetail(generic.DetailView):
    template_name = 'inscription/user_acceptation_form.html'
    queryset = User.objects.all()

    def get_context_data(self,**kwargs):
        context = super(UserDetail, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        demandeur = get_object_or_404(User, pk=self.kwargs.get('pk'))
        context['demandeur'] = demandeur
        context['info'] = Utilisateur.objects.get(user_pk=demandeur.pk)
        return context


def acceptation_utilisateur(request, pk):
    utilisateur = get_object_or_404(User, pk=pk)
    info = Utilisateur.objects.get(user_pk=utilisateur.pk)

    if request.method == 'POST':
        utilisateur.is_active = True
        utilisateur.save()
        # changer "en attente" pour acceptée
        info.etat = "Acceptée"
        info.save()
        template = get_template('inscription/inscription_acceptee.txt')
        context = {
            'username': utilisateur.username,
            'password': utilisateur.password,
            'nom' : utilisateur.first_name + " " + utilisateur.last_name,
            'uid': urlsafe_base64_encode(force_bytes(utilisateur.pk)),
            'token': default_token_generator.make_token(utilisateur),
            'domain': get_current_site(request).domain
        }
        contenu = template.render(context)
        email = EmailMessage("Demande d'inscription à la base de donnée du LMHS",
                             contenu,
                             'connectionlmhs@gmail.com',
                             [utilisateur.email]
                             )
        email.send()
        return redirect('/utilisateur/' + pk)


def refus_utilisateur(request, pk):
    utilisateur = get_object_or_404(User, pk=pk)
    info = Utilisateur.objects.get(user_pk = pk)

    if request.method == 'POST':
        utilisateur.delete()
        info.delete()
        return redirect('/')


class GererAuteurs(generic.ListView):
    model = Auteur
    template_name = 'gerer_auteur.html'

    def get_context_data(self, **kwargs):
        context = super(GererAuteurs, self).get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        context['nom'] = 'auteur'
        context['verbose'] = 'auteurs'
        return context

    def get_queryset(self):
        query = self.request.GET.get('q', None)
        if query == None:
            liste = Auteur.objects.filter(nom__istartswith='a').order_by('nom')
        else:
            liste = Auteur.objects.filter(nom__istartswith=query).order_by('nom')
        return liste


class GererMotsCles(generic.ListView):
    model = MotCle
    template_name = 'gerer.html'

    def get_context_data(self, **kwargs):
        context = super(GererMotsCles, self).get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        context['nom'] = 'motcle'
        context['lien'] = 'mot_cle'
        context['verbose'] = 'mot-clé'
        return context

    def get_queryset(self):
        query = self.request.GET.get('q', None)
        if query == None:
            liste = MotCle.objects.filter(nom__istartswith='a').order_by('nom')
        else:
            if query == "digit":
                liste = MotCle.objects.filter((Q(nom__istartswith='0') |
                                               Q(nom__istartswith='1') |
                                               Q(nom__istartswith='2') |
                                               Q(nom__istartswith='3') |
                                               Q(nom__istartswith='4') |
                                               Q(nom__istartswith='5') |
                                               Q(nom__istartswith='6') |
                                               Q(nom__istartswith='7') |
                                               Q(nom__istartswith='8') |
                                               Q(nom__istartswith='9'))).order_by('nom')
            else:
                liste = MotCle.objects.filter(nom__istartswith=query).order_by('nom')
        return liste


class GererProjets(generic.ListView):
    model = Projet
    template_name = 'gerer.html'

    def get_context_data(self, **kwargs):
        context = super(GererProjets, self).get_context_data(**kwargs)
        context['liste'] = Projet.objects.order_by('nom')
        context['nom'] = context['lien'] = 'projet'
        context['verbose'] = 'projet'
        return context

class GererCorpus(generic.ListView):
    model = Corpus
    template_name = 'gerer.html'

    def get_context_data(self, **kwargs):
        context = super(GererCorpus,self).get_context_data(**kwargs)
        context['liste'] = Corpus.objects.order_by('nom')
        context['nom'] = context['lien'] = 'corpus'
        context['verbose'] = 'corpus'
        return context


class GererUtilisateurs(generic.ListView):
    model = Utilisateur
    template_name = 'gerer_utilisateurs.html'

    def get_context_data(self, **kwargs):
        context = super(GererUtilisateurs, self).get_context_data(**kwargs)
        context['liste'] = Utilisateur.objects.order_by('date')
        return context


@login_required()
def serve_protected_document(request, file):
    document = get_object_or_404(Main, pdf_file="prive/documents/" + file)

    # Split the elements of the path
    path, file_name = os.path.split(file)

    response = FileResponse(document.pdf_file,)
    response["Content-Disposition"] = "attachment; filename=" + file_name

    return response


## pour rediriger les anciens liens de PDFs vers les nouveaux
def media_redirect(request, file):
    file_name = file
    if "/documents" not in file_name:
        file_name = 'public/documents/'+ file_name
        return redirect(file_name)


class SearchAutocompleteMotCle(generic.FormView):
    def get(self, request, *args, **kwargs):
        data = request.GET
        term = data.get("term")
        term = term.split(", ").pop()
        results = []

        if term:
            motcle = MotCle.objects.filter(nom__icontains=term)
        else:
            motcle = MotCle.objects.all()

        for term in motcle:
            term_json = {}
            term_json['label'] = term.nom
            term_json['value'] = term.nom
            results.append(term_json)
        results = [dict(t) for t in {tuple(d.items()) for d in results}]
        results.sort(key=itemgetter('label'))
        data = json.dumps(results)
        mimetype = 'application/json'
        return HttpResponse(data, mimetype)


class SearchAutocompleteAuteur(generic.FormView):
    def get(self, request, *args, **kwargs):
        data = request.GET
        term = data.get("term")
        results = []
        tout = []
        for i in Auteur.objects.values_list('nom'):
            tout.append(i[0])

        #mettre sous format [Prénom] [Nom] au lien de [Nom], [Prénom]
        for i in tout:
            label = i
            label = label.split(', ')
            label.reverse()
            nom = ""
            for j in label:
                if label.index(j) == len(label) - 1:
                    nom += j
                else:
                    nom += j
                    nom += " "
            tout[tout.index(i)] = nom

        for obj in tout:
            if term.upper() in obj.upper():
                term_json = {}
                term_json['label'] = obj
                term_json['value'] = obj
                results.append(term_json)

        results = [dict(t) for t in {tuple(d.items()) for d in results}]
        results.sort(key=itemgetter('label'))
        data = json.dumps(results)
        mimetype = 'application/json'
        return HttpResponse(data, mimetype)


class TypeEvenementAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return TypeEvenement.objects.none()

        qs = TypeEvenement.objects.order_by('nom')

        if self.q:
            qs = qs.filter(nom__icontains=self.q)

        return qs


class AuteurAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Auteur.objects.none()

        qs = Auteur.objects.order_by('cote').exclude(cote__exact='').exclude(cote__isnull=True)

        if self.q:
            qs = qs.filter(nom__icontains=self.q)

        return qs


class DirecteurCollectionAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return DirecteurCollection.objects.none()

        qs = DirecteurCollection.objects.order_by('nom')

        if self.q:
            qs = qs.filter(nom__icontains=self.q)

        return qs


class DirecteurPublicationAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return DirecteurPublication.objects.none()

        qs = DirecteurPublication.objects.order_by('nom')

        if self.q:
            qs = qs.filter(nom__icontains=self.q)

        return qs


class EditeurAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Editeur.objects.none()

        qs = Editeur.objects.order_by('nom')

        if self.q:
            qs = qs.filter(nom__icontains=self.q)

        return qs


class MotCleAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return MotCle.objects.none()

        qs = MotCle.objects.all().order_by('nom')

        if self.q:
            qs = qs.filter(nom__icontains=self.q)

        return qs


class SupportAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Support.objects.none()

        qs = Support.objects.order_by('nom')

        if self.q:
            qs = qs.filter(nom__icontains=self.q)

        return qs


class TraducteurAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Traducteur.objects.none()

        qs = Traducteur.objects.order_by('nom')

        if self.q:
            qs = qs.filter(nom__icontains=self.q)

        return qs


class CollectionAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Collection.objects.none()

        qs = Collection.objects.order_by('nom')

        if self.q:
            qs = qs.filter(nom__icontains=self.q)

        return qs


class FondsAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Fonds.objects.none()

        qs = Fonds.objects.order_by('nom')

        if self.q:
            qs = qs.filter(nom__icontains=self.q)

        return qs


class LangueOrigineAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return LangueOrigine.objects.none()

        qs = LangueOrigine.objects.order_by('nom')

        if self.q:
            qs = qs.filter(nom__icontains=self.q)

        return qs


class LocalisationAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Localisation.objects.none()

        qs = Localisation.objects.order_by('nom')

        if self.q:
            qs = qs.filter(nom__icontains=self.q)

        return qs


class MaisonEditionAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return MaisonEdition.objects.none()

        qs = MaisonEdition.objects.order_by('nom')

        if self.q:
            qs = qs.filter(nom__icontains=self.q)

        return qs


class MediumAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Medium.objects.none()

        qs = Medium.objects.order_by('nom')

        if self.q:
            qs = qs.filter(nom__icontains=self.q)

        return qs


class MethodeReproductionAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return MethodeReproduction.objects.none()

        qs = MethodeReproduction.objects.order_by('nom')

        if self.q:
            qs = qs.filter(nom__icontains=self.q)

        return qs


class NomOrgAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return NomOrg.objects.none()

        qs = NomOrg.objects.order_by('nom')

        if self.q:
            qs = qs.filter(nom__icontains=self.q)

        return qs


class ProjetAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Projet.objects.none()

        qs = Projet.objects.order_by('nom')

        if self.q:
            qs = qs.filter(nom__icontains=self.q)

        return qs


class GenreAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Genre.objects.none()

        qs = Genre.objects.order_by('nom')

        if self.q:
            qs = qs.filter(nom__icontains=self.q)

        return qs


class CotePrefixeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return CotePrefixe.objects.none()

        qs = CotePrefixe.objects.order_by('cote')

        if self.q:
            qs = qs.filter(cote__icontains=self.q)

        return qs


class CorpusAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Corpus.objects.none()

        qs = Corpus.objects.order_by('nom')

        if self.q:
            qs = qs.filter(nom__icontains=self.q)

        return qs