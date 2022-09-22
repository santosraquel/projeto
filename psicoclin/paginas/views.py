from paginas.models import Estado
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Estado, Cidade, Funcao, Medico, Funcionario, Consulta, Paciente
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

class FuncaoCreate(LoginRequiredMixin, CreateView):
    model = Funcao
    group_required = u"Administrador"
    fields = ['funcao', 'descricao']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-funcao')


class MedicoCreate(LoginRequiredMixin, CreateView):
    model = Medico
    group_required = u"Administrador"
    fields = ['nome', 'nascimento', 'rg', 'crm', 'rua', 'bairro', 'numero', 'cidade', 'telefone', 'funcao', 'status']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-medico')

class PacienteCreate(LoginRequiredMixin, CreateView):
    model = Paciente
    group_required = u"Administrador"
    fields = ['nome', 'titular', 'nascimento', 'rg', 'cpf', 'rua', 'bairro', 'numero', 'cidade', 'telefone',  'status']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-paciente')

class FuncionarioCreate(LoginRequiredMixin, CreateView):
    model = Funcionario
    group_required = u"Administrador"
    fields = ['nome', 'nascimento', 'rg', 'cpf', 'rua', 'bairro', 'numero', 'cidade', 'telefone',  'status']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-funcionario')


class ConsultaCreate(LoginRequiredMixin, CreateView):
    model = Consulta
    group_required = u"Administrador"
    fields = ['paciente', 'medico', 'data', 'hora', 'valor', 'status']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-consulta')

############################# UPDATE VIEW #########################

class EstadoUpdate(LoginRequiredMixin, UpdateView):
    model = Estado
    fields = ['nome', 'sigla']
    group_required = u"Administrador"
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-estado')


class CidadeUpdate(LoginRequiredMixin, UpdateView):
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



class FuncaoUpdate(LoginRequiredMixin, UpdateView):
    model = Funcao
    fields = ['funcao', 'descricao']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-funcao')


class MedicoUpdate(LoginRequiredMixin, UpdateView):
    model = Medico
    group_required = [u"Administrador", u"Editor"]
    fields = ['nome', 'nascimento', 'rg', 'crm', 'rua', 'bairro', 'numero', 'cidade', 'telefone', 'funcao', 'status']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-medico')

class PacienteUpdate(LoginRequiredMixin, UpdateView):
    model = Paciente
    group_required = [u"Administrador", u"Editor"]
    fields = ['nome', 'titular', 'nascimento', 'rg', 'cpf', 'rua', 'bairro', 'numero', 'cidade', 'telefone',  'status']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-paciente')

class FuncionarioUpdate(LoginRequiredMixin, UpdateView):
    model = Funcionario
    group_required = [u"Administrador", u"Editor"]
    fields = ['nome', 'nascimento', 'rg', 'cpf', 'rua', 'bairro', 'numero', 'cidade', 'telefone',  'status']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-funcionario')


class ConsultaUpdate(LoginRequiredMixin, CreateView):
    model = Consulta
    group_required = u"Administrador"
    fields = ['paciente', 'medico', 'data', 'hora', 'valor', 'status']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-consulta')

######################### DELETE VIEW ##################################


class EstadoDelete(LoginRequiredMixin, DeleteView):
    model = Estado
    group_required = u"Administrador"
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('listar-estado')


class CidadeDelete(LoginRequiredMixin, DeleteView):
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



class FuncaoDelete(LoginRequiredMixin, DeleteView):
    model = Funcao
    group_required = u"Administrador"
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('listar-funcao')


class MedicoDelete(LoginRequiredMixin, DeleteView):
    model = Medico
    group_required = [u"Administrador", u"Editor"]
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('listar-medico')

class PacienteDelete(LoginRequiredMixin, DeleteView):
    model = Paciente
    group_required = [u"Administrador", u"Editor"]
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('listar-paciente')

class FuncionarioDelete(LoginRequiredMixin, DeleteView):
    model = Funcionario
    group_required = [u"Administrador", u"Editor"]
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('listar-funcionario')


class ConsultaDelete(LoginRequiredMixin, DeleteView):
    model = Consulta
    group_required = [u"Administrador", u"Editor"]
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('listar-consulta')

######################### LIST VIEW ###############

class EstadoList(ListView):
    model = Estado
    group_required =[ u"Administrador", u"Editor"]
    template_name = 'paginas/listas/estados.html'


class CidadeList(ListView):
    model = Cidade
    group_required = [u"Administrador", u"Editor"]
    template_name = 'paginas/listas/cidades.html'

    # filter() retorna uma lista
    def get_queryset(self): # filtrando objetos
        # self.object_list = Cidade.objects.all(nome="Paranavaí") # listando todas as cidades que tem o nome Paranavaí
        # self.object_list = Cidade.objects.all(nome__icontents="Paranavaí") # listando todas as cidades que contém Paranavaí
        self.object_list = Cidade.objects.filter(usuario=self.request.user) # listando as cidades do usuário logado
        return self.object_list
    
class FuncaoList(ListView):
    model = Funcao
    group_required =[ u"Administrador", u"Editor"]
    template_name = 'paginas/listas/funcoes.html'


class MedicoList(ListView):
    model = Medico
    group_required = [u"Administrador", u"Editor"]
    template_name = 'paginas/listas/medicos.html'

class PacienteList(ListView):
    model = Paciente
    group_required = [u"Administrador", u"Editor"]
    template_name = 'paginas/listas/pacientes.html'

class FuncionarioList(ListView):
    model = Funcionario
    group_required = [u"Administrador", u"Editor"]
    template_name = 'paginas/listas/funcionarios.html'


class ConsultaList(ListView):
    model = Consulta
    group_required = [u"Administrador", u"Editor"]
    template_name = 'paginas/listas/consultas.html'

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
