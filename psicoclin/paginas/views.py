from paginas.models import Estado
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Estado, Cidade, Pessoa, Funcao
from braces.views import GroupRequiredMixin
# Create your views here.


############################# CREATE VIEW #########################
class Index(GroupRequiredMixin, TemplateView):
    group_required = u"Visualizador"
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

    def form_valid(self, form):
        # pegando os dados do usuário que está logado e atribui ao usuário
        form.instance.usuario = self.request.user
        url = super().form_valid(form)  # persiste os dados no banco de dados
        self.object.codigo = hash(self.object.pk)
        self.object.save()  # salvando o objeto que foi alterado
        return url


class PessoaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Pessoa
    group_required = u"Administrador"
    fields = ['nome', 'data_nascimento', 'email', 'cidade']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')

class FuncaoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Funcao
    group_required = u"Administrador"
    fields = ['nome', 'descrição']
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

    # get() retorna um objeto
    def get_object(self):  # filtrando objetos
        # listando as cidades do usuário logado
        self.object_list = get_object_or_404( Cidade, usuario=self.request.user,  pk=self.kwargs['pk'])
        return self.object_list


class PessoaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Pessoa
    group_required = [u"Administrador", u"Editor"]
    fields = ['nome', 'data_nascimento', 'email', 'cidade']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')

class FuncaoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Funcao
    fields = ['nome', 'descricao']
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

    # get() retorna um objeto
    def get_object(self):  # filtrando objetos
        # listando as cidades do usuário logado
        self.object_list = get_object_or_404(
            Cidade, usuario=self.request.user,  pk=self.kwargs['pk'])
        return self.object_list


class PessoaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Pessoa
    group_required = [u"Administrador", u"Editor"]
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('index')

class FuncaoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Funcao
    group_required = u"Administrador"
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('listar-funcao')


######################### LIST VIEW ###############

class EstadoList(GroupRequiredMixin, ListView):
    model = Estado
    group_required =[ u"Administrador", u"Editor"]
    template_name = 'paginas/listas/estados.html'


class CidadeList(GroupRequiredMixin, ListView):
    model = Cidade
    group_required = [u"Administrador", u"Editor"]
    template_name = 'paginas/listas/cidades.html'

    # filter() retorna uma lista
    def get_queryset(self): # filtrando objetos
        # self.object_list = Cidade.objects.all(nome="Paranavaí") # listando todas as cidades que tem o nome Paranavaí
        # self.object_list = Cidade.objects.all(nome__icontents="Paranavaí") # listando todas as cidades que contém Paranavaí
        self.object_list = Cidade.objects.filter(usuario=self.request.user) # listando as cidades do usuário logado
        return self.object_list
    

class PessoaList(GroupRequiredMixin, ListView):
    model = Pessoa
    group_required = [u"Administrador", u"Editor"]
    template_name = 'paginas/listas/pessoas.html'


class FuncaoList(GroupRequiredMixin, ListView):
    model = Funcao
    group_required =[ u"Administrador", u"Editor"]
    template_name = 'paginas/listas/funcoes.html'


# Create your views here.

class PaginaInicialView(TemplateView):
    template_name = 'paginas/index.html'

    # de uma maneira geral, envia dados para o template html
    def get_context_data(self, *args, **kwargs):
        # Executa da classe pai para ter dados padrão
        dados = super().get_context_data(*args, **kwargs)

        # Cria um dado na posição teste
        dados["teste"] = "Mah oeee"

        # Verifica se o usuário está logado
        if(self.request.user.is_authenticated):
            # Cria a posição parcelas_vencidas com uma contagem de parcela que não foram pagas
            dados["name"] = Estado.objects.filter(
                estado__usuario=self.request.user,
            ).count()

        return dados
