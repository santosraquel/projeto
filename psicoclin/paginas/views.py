from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Estado, Cidade, Pessoa
# Create your views here.


############################# CREATE VIEW #########################
class Index(TemplateView):
    template_name = 'paginas/index.html'


class EstadoCreate(LoginRequiredMixin, CreateView):
    model = Estado
    fields = ['nome', 'sigla']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-estado')


class CidadeCreate(LoginRequiredMixin, CreateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-cidade')


class PessoaCreate(LoginRequiredMixin, CreateView):
    model = Pessoa
    fields = ['nome', 'data_nascimento', 'email', 'cidade']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')


############################# UPDATE VIEW #########################

class EstadoUpdate(LoginRequiredMixin, UpdateView):
    model = Estado
    fields = ['nome', 'sigla']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-estado')


class CidadeUpdate(LoginRequiredMixin, UpdateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-cidade')


class PessoaUpdate(LoginRequiredMixin, UpdateView):
    model = Pessoa
    fields = ['nome', 'data_nascimento', 'email', 'cidade']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')

######################### DELETE VIEW ##################################


class EstadoDelete(LoginRequiredMixin, DeleteView):
    model = Estado
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('listar-estado')


class CidadeDelete(LoginRequiredMixin, DeleteView):
    model = Cidade
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('listar-cidade')


class PessoaDelete(LoginRequiredMixin, DeleteView):
    model = Pessoa
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('index')


######################### LIST VIEW ###############

class EstadoList(ListView):
    model = Estado
    template_name = 'paginas/listas/estados.html'

class CidadeList(ListView):
    model = Cidade
    template_name = 'paginas/listas/cidades.html'
