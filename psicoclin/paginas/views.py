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
class Index(TemplateView):
    template_name = 'paginas/index.html'


class EstadoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Estado
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    fields = ['nome', 'sigla']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-estado')


class CidadeCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Cidade
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    fields = ['nome', 'estado']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-cidade')

class FuncaoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Funcao
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    fields = ['funcao', 'descricao']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-funcao')


class MedicoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Medico
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    fields = ['nome', 'nascimento', 'rg', 'crm', 'rua', 'bairro', 'numero', 'cidade', 'telefone', 'funcao', 'status']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-medico')

class PacienteCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Paciente
    group_required = [u"Administrador", u"Funcionario"]
    fields = ['nome', 'titular', 'nascimento', 'rg', 'cpf', 'rua', 'bairro', 'numero', 'cidade', 'telefone',  'status']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-paciente')

    def form_valid(self, form):
        # pegando os dados do usuário que está logado e atribui ao usuário
        form.instance.usuario = self.request.user
        url = super().form_valid(form)  # persiste os dados no banco de dados
        self.object.codigo = hash(self.object.pk)
        self.object.save()  # salvando o objeto que foi alterado
        return url

class FuncionarioCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Funcionario
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    fields = ['nome', 'nascimento', 'rg', 'cpf', 'rua', 'bairro', 'numero', 'cidade', 'telefone',  'status']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-funcionario')


class ConsultaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Consulta
    login_url = reverse_lazy('login')
    group_required =[ u"Administrador", u"Funcionario"]
    fields = ['paciente', 'medico', 'data', 'hora', 'valor', 'status']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-consulta')

    def form_valid(self, form):
        # pegando os dados do usuário que está logado e atribui ao usuário
        form.instance.usuario = self.request.user
        url = super().form_valid(form)  # persiste os dados no banco de dados
        self.object.codigo = hash(self.object.pk)
        self.object.save()  # salvando o objeto que foi alterado
        return url

############################# UPDATE VIEW #########################

class EstadoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Estado
    login_url = reverse_lazy('login')
    fields = ['nome', 'sigla']
    group_required = u"Administrador"
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-estado')

class CidadeUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Cidade
    login_url = reverse_lazy('login')
    fields = ['nome', 'estado']
    group_required = u"Administrador"
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-cidade')

class FuncaoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Funcao
    login_url = reverse_lazy('login')
    fields = ['funcao', 'descricao']
    group_required = u"Administrador"
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-funcao')

class MedicoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Medico
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    fields = ['nome', 'nascimento', 'rg', 'crm', 'rua', 'bairro', 'numero', 'cidade', 'telefone', 'funcao', 'status']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-medico')

class PacienteUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Paciente
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Funcionario"]
    fields = ['nome', 'titular', 'nascimento', 'rg', 'cpf', 'rua', 'bairro', 'numero', 'cidade', 'telefone',  'status']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-paciente')

    def get_object(self):
        self.object = get_object_or_404(
                            Paciente,
                            usuario=self.request.user,
                            pk=self.kwargs['pk']
                        )
        return self.object

class FuncionarioUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Funcionario
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    fields = ['nome', 'nascimento', 'rg', 'cpf', 'rua', 'bairro', 'numero', 'cidade', 'telefone',  'status']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-funcionario')

class ConsultaUpdate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Consulta
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Funcionario"]
    fields = ['paciente', 'medico', 'data', 'hora', 'valor', 'status']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-consulta')

    def get_object(self):
        self.object = get_object_or_404(
                            Consulta,
                            usuario=self.request.user,
                            pk=self.kwargs['pk']
                        )
        return self.object

######################### DELETE VIEW ##################################


class EstadoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Estado
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('listar-estado')

class CidadeDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Cidade
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('listar-cidade')

class FuncaoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Funcao
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('listar-funcao')

class MedicoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Medico
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('listar-medico')

class PacienteDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Paciente
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Funcionario"]
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('listar-paciente')

    def get_object(self):
        self.object = get_object_or_404(
            Paciente,
            usuario=self.request.user,
            pk=self.kwargs['pk']
        )
        return self.object

class FuncionarioDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Funcionario
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('listar-funcionario')

class ConsultaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Consulta
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Funcionario"]
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('listar-consulta')

    def get_object(self):
        self.object = get_object_or_404(
            Consulta,
            usuario=self.request.user,
            pk=self.kwargs['pk']
        )
        return self.object

######################### LIST VIEW ###############

class EstadoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Estado
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Funcionario"]
    template_name = 'paginas/listas/estados.html'

class CidadeList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Cidade
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Funcionario"]
    template_name = 'paginas/listas/cidades.html'
    
class FuncaoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Funcao
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Funcionario"]
    template_name = 'paginas/listas/funcoes.html'

class MedicoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Medico
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Funcionario"]
    template_name = 'paginas/listas/medicos.html'

class PacienteList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Paciente
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Funcionario"]
    template_name = 'paginas/listas/pacientes.html'

    def get_queryset(self):
        # armazena a lista e retorna ela
        self.object_list = Paciente.objects.filter(usuario=self.request.user)
        return self.object_list

class FuncionarioList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Funcionario
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Funcionario"]
    template_name = 'paginas/listas/funcionarios.html'

class ConsultaList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Consulta
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Funcionario"]
    template_name = 'paginas/listas/consultas.html'

    def get_queryset(self):
        # armazena a lista e retorna ela
        self.object_list = Consulta.objects.filter(usuario=self.request.user)
        return self.object_list

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
