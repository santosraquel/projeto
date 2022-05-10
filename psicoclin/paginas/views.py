from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView

from .models import Estado, Cidade, Pessoa
# Create your views here.


############################# CREATE VIEW #########################
class Index(TemplateView):
    template_name = 'paginas/index.html'

class EstadoCreate(CreateView):
    model = Estado
    fields = ['nome', 'sigla']
    template_name = 'paginas/form.html'
    sucess_url = reverse_lazy('index')

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
    sucess_url = reverse_lazy('index')


class PessoaUpdate(UpdateView):
    model = Pessoa
    fields = ['nome', 'data_nascimento', 'email', 'cidade']
    template_name = 'paginas/form.html'
    sucess_url = reverse_lazy('index')
