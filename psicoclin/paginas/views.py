from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView


from .models import Estado, Cidade, Pessoa
# Create your views here.


############################# CREATE VIEW #########################
class Index(TemplateView):
    template_name = 'paginas/index.html'

class EstadoCreate(CreateView):
    model = Estado
    fields = ['nome', 'sigla']
    template_name = 'paginas/form.html'
    sucess_url = reverse_lazy('listar-estado')

class CidadeCreate(CreateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'paginas/form.html'
    sucess_url = reverse_lazy('index')

class PessoaCreate(CreateView):
    model = Pessoa
    fields = ['nome', 'data_nascimento', 'email', 'cidade']
    template_name = 'paginas/form.html'
    sucess_url = reverse_lazy('index')


############################# UPDATE VIEW #########################

class EstadoUpdate(UpdateView):
    model = Estado
    fields = ['nome', 'sigla']
    template_name = 'paginas/form.html'
    sucess_url = reverse_lazy('index')


class CidadeUpdate(UpdateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'paginas/form.html'
    sucess_url = reverse_lazy('listar-estado')


class PessoaUpdate(UpdateView):
    model = Pessoa
    fields = ['nome', 'data_nascimento', 'email', 'cidade']
    template_name = 'paginas/form.html'
    sucess_url = reverse_lazy('index')

######################### DELETE VIEW ##################################
class EstadoDelete(DeleteView):
    model = Estado
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('listar-estado')


class CidadeDelete(DeleteView):
    model = Cidade
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('index')


class PessoaDelete(DeleteView):
    model = Pessoa
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('index')


######################### LIST VIEW ###############

class EstadoList(ListView):
    model = Estado
    template_name = 'paginas/listas/estados.html'
