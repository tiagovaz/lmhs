from dal import autocomplete
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import generic

from lmhsweb.filters import MainFilter
from lmhsweb.forms import Search
from lmhsweb.models import Main, TypeEvenement, Auteur, DirecteurCollection, DirecteurPublication, Editeur, MotCle, \
    Support, Traducteur, Collection, Fonds, LangueOrigine, Place, Localisation, MaisonEdition, Medium, \
    MethodeReproduction, NomOrg, Projet, Genre


class MainList(generic.View):
    def get(self, request):
        titre = request.GET.get('titre', '')
        auteur = request.GET.get('auteur', '')
        projet = request.GET.get('projet', '')
        type = request.GET.get('type', '')
        date = request.GET.get('date', '')
        mot_cle = request.GET.get('mot_cle', '')
        #tousindex_calcul = request.GET['tousIndex_calcul']

        data = Main.objects.filter(titre__icontains=titre, auteur__nom__icontains=auteur, projet__nom__icontains=projet, type__icontains=type, date__icontains=date, mot_cle__nom__icontains=mot_cle).distinct()
        all_main_registers = MainFilter(self.request.GET, queryset=Main.objects.all())

        print data

        paginator = Paginator(data, 25)
        page = request.GET.get('page')
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)
        return render(request, 'result.html', {'items': items, 'data': data, 'form' : all_main_registers.form})


# class MainList(generic.ListView):
#     template_name = 'list.html'
#     context_object_name = 'main_registers'
#     model = Main
#
#     def get_queryset(self):
#         return MainFilter(self.request.GET, queryset=Main.objects.all())
#
#     @method_decorator(login_required)
#     def dispatch(self, *args, **kwargs):
#         return super(MainList, self).dispatch(*args, **kwargs)
#
#     def get_context_data(self, **kwargs):
#         context = super(MainList, self).get_context_data(**kwargs)
#
#         all_main_registers = MainFilter(self.request.GET, queryset=Main.objects.all())
#         context['view'] = "main_registers"
#         context['form'] = all_main_registers.form
#
#         return context

class SearchForm(generic.CreateView):
    model = Main
    template_name = 'search.html'
    form_class = Search

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SearchForm, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return self.object.get_absolute_url()

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

        qs = Auteur.objects.all()

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

        qs = MotCle.objects.all()

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

class LieuAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Place.objects.none()

        qs = Place.objects.all()

        if self.q:
            qs = qs.filter(venue__icontains=self.q)

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