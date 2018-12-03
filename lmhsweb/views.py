# -*- coding: utf-8 -*-
from dal import autocomplete
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import generic
from django.db.models import Count

from lmhsweb.filters import MainFilter
from lmhsweb.forms import Search, Create
from lmhsweb.models import Main, TypeEvenement, Auteur, DirecteurCollection, DirecteurPublication, Editeur, MotCle, \
    Support, Traducteur, Collection, Fonds, LangueOrigine, Localisation, MaisonEdition, Medium, \
    MethodeReproduction, NomOrg, Projet, Genre, CotePrefixe, CoteAuteur

from django.db.models import Q
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy, resolve



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
        context['verbose'] = 'mots-clés'
        return context

    def get_queryset(self):
        query = self.request.GET.get('q', None)
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
        context['verbose'] = 'projets'
        return context


class NoticeDelete(DeleteView):
    model = Main
    success_url = reverse_lazy('event_list') # This is where this view will
                                            # redirect the user
    template_name = 'delete_notice.html'


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
        '''
        if request.user.is_authenticated():
            search_form = Search_User()
        else:
            search_form = Search()
        '''
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

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CreateForm, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return '/list/'


class UpdateForm(generic.UpdateView):
    model = Main
    template_name = "update.html"
    form_class = Create
    #fields = ('__all__')

    def get_form_kwargs(self):
        kwargs = super(UpdateForm, self ).get_form_kwargs()
        kwargs['type'] = self.request.GET.get('type', '')
        return kwargs

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        main = get_object_or_404(
            Main,
            id=kwargs['pk']
        )
        return super(UpdateForm, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return '/list/'
        # return reverse_lazy(
        #     'result',
        #     kwargs={'pk': self.kwargs['pk']}
        # )


class Login(generic.TemplateView):
    template_name = 'registration/login.html'


class TypeEvenementAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return TypeEvenement.objects.none()

        qs = TypeEvenement.objects.all()

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

        qs = DirecteurCollection.objects.all()

        if self.q:
            qs = qs.filter(nom__icontains=self.q)

        return qs


class DirecteurPublicationAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return DirecteurPublication.objects.none()

        qs = DirecteurPublication.objects.all()

        if self.q:
            qs = qs.filter(nom__icontains=self.q)

        return qs


class EditeurAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Editeur.objects.none()

        qs = Editeur.objects.all()

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

        qs = Support.objects.all()

        if self.q:
            qs = qs.filter(nom__icontains=self.q)

        return qs


class TraducteurAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Traducteur.objects.none()

        qs = Traducteur.objects.all()

        if self.q:
            qs = qs.filter(nom__icontains=self.q)

        return qs


class CollectionAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Collection.objects.none()

        qs = Collection.objects.all()

        if self.q:
            qs = qs.filter(nom__icontains=self.q)

        return qs


class FondsAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Fonds.objects.none()

        qs = Fonds.objects.all()

        if self.q:
            qs = qs.filter(nom__icontains=self.q)

        return qs


class LangueOrigineAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return LangueOrigine.objects.none()

        qs = LangueOrigine.objects.all()

        if self.q:
            qs = qs.filter(nom__icontains=self.q)

        return qs


class LocalisationAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Localisation.objects.none()

        qs = Localisation.objects.all()

        if self.q:
            qs = qs.filter(nom__icontains=self.q)

        return qs


class MaisonEditionAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return MaisonEdition.objects.none()

        qs = MaisonEdition.objects.all()

        if self.q:
            qs = qs.filter(nom__icontains=self.q)

        return qs


class MediumAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Medium.objects.none()

        qs = Medium.objects.all()

        if self.q:
            qs = qs.filter(nom__icontains=self.q)

        return qs


class MethodeReproductionAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return MethodeReproduction.objects.none()

        qs = MethodeReproduction.objects.all()

        if self.q:
            qs = qs.filter(nom__icontains=self.q)

        return qs


class NomOrgAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return NomOrg.objects.none()

        qs = NomOrg.objects.all()

        if self.q:
            qs = qs.filter(nom__icontains=self.q)

        return qs


class ProjetAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Projet.objects.none()

        qs = Projet.objects.all()

        if self.q:
            qs = qs.filter(nom__icontains=self.q)

        return qs


class GenreAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Genre.objects.none()

        qs = Genre.objects.all()

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
