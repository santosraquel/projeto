from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Estado, Cidade, Pessoa
from braces.views import GroupRequiredMixin
# Create your views here.


############################# CREATE VIEW #########################
class Index(TemplateView):
    template_name = 'paginas/index.html'


class EstadoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Estado
    group_required = u"Administrador"
    fields = ['nome', 'sigla']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-estado')


class CidadeCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Cidade
    group_required = u"Administrador"
    fields = ['nome', 'estado']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-cidade')


class PessoaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Pessoa
    group_required = u"Administrador"
    fields = ['nome', 'data_nascimento', 'email', 'cidade']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')


############################# UPDATE VIEW #########################

class EstadoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Estado
    fields = ['nome', 'sigla']
    group_required = u"Administrador"
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-estado')


class CidadeUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Cidade
    fields = ['nome', 'estado']
    group_required = u"Administrador"
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-cidade')


class PessoaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Pessoa
    group_required = [u"Administrador", u"Editor"]
    fields = ['nome', 'data_nascimento', 'email', 'cidade']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')

######################### DELETE VIEW ##################################


class EstadoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Estado
    group_required = u"Administrador"
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('listar-estado')


class CidadeDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Cidade
    group_required = u"Administrador"
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('listar-cidade')


class PessoaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Pessoa
    group_required = [u"Administrador", u"Editor"]
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('index')


######################### LIST VIEW ###############

class EstadoList(GroupRequiredMixin, ListView):
    model = Estado
    group_required =[ u"Administrador", u"Editor"]
    template_name = 'paginas/listas/estados.html'


class CidadeList(GroupRequiredMixin, ListView):
    model = Cidade
    group_required = [u"Administrador", u"Editor"]
    template_name = 'paginas/listas/cidades.html'

class PessoaList(GroupRequiredMixin, ListView):
    model = Pessoa
    group_required = [u"Administrador", u"Editor"]
    template_name = 'paginas/listas/pessoas.html'
