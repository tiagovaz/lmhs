from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic

from lmhs.filters import MainFilter
from lmhsweb.models import Main

class MainList(generic.ListView):
    template_name = 'list.html'
    context_object_name = 'main_registers'
    model = Main

    def get_queryset(self):
        return MainFilter(self.request.GET, queryset=Main.objects.all())

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MainList, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(MainList, self).get_context_data(**kwargs)

        all_main_registers = MainFilter(self.request.GET, queryset=Main.objects.all())
        context['view'] = "main_registers"
        context['form'] = all_main_registers.form

        return context

class Login(generic.TemplateView):
    template_name = 'registration/login.html'
