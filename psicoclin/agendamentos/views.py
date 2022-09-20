from django.shortcuts import render

from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Consulta
from braces.views import GroupRequiredMixin
# Create your views here.


############################# CREATE VIEW #########################

class ConsultaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Consulta
    group_required = u"Administrador"
    # fields = ['dataConsulta', 'horaConsulta', 'valorConsulta', 'status', 'medico', 'paciente']
    fields = ['dataConsulta', 'horaConsulta', 'valorConsulta', 'status']
    template_name = 'agendamentos/form.html'
    success_url = reverse_lazy('listar-consulta')

    def form_valid(self, form):
        # pegando os dados do usuário que está logado e atribui ao usuário
        form.instance.usuario = self.request.user
        url = super().form_valid(form)  # persiste os dados no banco de dados
        self.object.codigo = hash(self.object.pk)
        self.object.save()  # salvando o objeto que foi alterado
        return url


############################# UPDATE VIEW #########################

class ConsultaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Consulta
    # fields = ['dataConsulta', 'horaConsulta',
    #           'valorConsulta', 'status', 'medico', 'paciente']
    fields = ['dataConsulta', 'horaConsulta',
              'valorConsulta', 'status']
    group_required = u"Administrador"
    template_name = 'agendamentos/form.html'
    success_url = reverse_lazy('listar-consulta')

    # get() retorna um objeto
    def get_object(self):  # filtrando objetos
        # listando as consultas do usuário logado
        self.object_list = get_object_or_404(
            Consulta, usuario=self.request.user,  pk=self.kwargs['pk'])
        return self.object_list







######################### DELETE VIEW ##################################

class ConsultaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Consulta
    group_required = u"Administrador"
    template_name = 'agendamentos/form-delete.html'
    success_url = reverse_lazy('listar-consulta')

    # get() retorna um objeto
    def get_object(self):  # filtrando objetos
        # listando as cidades do usuário logado
        self.object_list = get_object_or_404(
            Consulta, usuario=self.request.user,  pk=self.kwargs['pk'])
        return self.object_list

######################### LIST VIEW ###############

class ConsultaList(GroupRequiredMixin, ListView):
    model = Consulta
    group_required = [u"Administrador", u"Editor"]
    template_name = 'agendamentos/listas/consultas.html'

    # filter() retorna uma lista
    def get_queryset(self):  # filtrando objetos
        # self.object_list = Cidade.objects.all(nome="Paranavaí") # listando todas as cidades que tem o nome Paranavaí
        # self.object_list = Cidade.objects.all(nome__icontents="Paranavaí") # listando todas as cidades que contém Paranavaí
        # listando as cidades do usuário logado
        self.object_list = Consulta.objects.filter(usuario=self.request.user)
        return self.object_list


