from django.urls import path

from .views import Index, EstadoCreate, CidadeCreate, PacienteCreate, FuncaoCreate, MedicoCreate,  FuncionarioCreate, ConsultaCreate
from .views import EstadoUpdate, CidadeUpdate, PacienteUpdate, FuncaoUpdate, MedicoUpdate, FuncionarioUpdate, ConsultaUpdate
from .views import EstadoDelete, CidadeDelete, PacienteDelete, FuncaoDelete, MedicoDelete, FuncionarioDelete, ConsultaDelete
from .views import EstadoList, CidadeList, PacienteList, FuncaoList, MedicoList, FuncionarioList, ConsultaList


urlpatterns = [
    path('', Index.as_view(), name="index"),

    path('cadastrar/estado', EstadoCreate.as_view(), name="cadastrar-estado"),
    path('cadastrar/cidade', CidadeCreate.as_view(), name="cadastrar-cidade"),
    path('cadastrar/paciente', PacienteCreate.as_view(), name="cadastrar-paciente"),
    path('cadastrar/funcao', FuncaoCreate.as_view(), name="cadastrar-funcao"),
    path('cadastrar/medico', MedicoCreate.as_view(), name="cadastrar-medico"),
    path('cadastrar/funcionario', FuncionarioCreate.as_view(), name="cadastrar-funcionario"),
    path('cadastrar/consulta', ConsultaCreate.as_view(), name="cadastrar-consulta"),

    path('editar/estado/<int:pk>/', EstadoUpdate.as_view(), name="editar-estado"),
    path('editar/cidade/<int:pk>/', CidadeUpdate.as_view(), name="editar-cidade"),
    path('editar/paciente/<int:pk>/', PacienteUpdate.as_view(), name="editar-paciente"),
    path('editar/funcao/<int:pk>/', FuncaoUpdate.as_view(), name="editar-funcao"),
    path('editar/medico/<int:pk>/', MedicoUpdate.as_view(), name="editar-medico"),
    path('editar/funcionario/<int:pk>/', FuncionarioUpdate.as_view(), name="editar-funcionario"),
    path('editar/consulta/<int:pk>/', ConsultaUpdate.as_view(), name="editar-consulta"),

    path('excluir/estado/<int:pk>/', EstadoDelete.as_view(), name="excluir-estado"),
    path('excluir/cidade/<int:pk>/', CidadeDelete.as_view(), name="excluir-cidade"),
    path('excluir/paciente/<int:pk>/', PacienteDelete.as_view(), name="excluir-paciente"),
    path('excluir/funcao/<int:pk>/', FuncaoDelete.as_view(), name="excluir-funcao"),
    path('excluir/medico/<int:pk>/', MedicoDelete.as_view(), name="excluir-medico"),
    path('excluir/funcionario/<int:pk>/', FuncionarioDelete.as_view(), name="excluir-funcionario"),
    path('excluir/consulta/<int:pk>/', ConsultaDelete.as_view(), name="excluir-consulta"),

    path('listar/estado/', EstadoList.as_view(), name="listar-estado"),
    path('listar/cidade/', CidadeList.as_view(), name="listar-cidade"),
    path('listar/paciente/', PacienteList.as_view(), name="listar-paciente"),
    path('listar/funcao/', FuncaoList.as_view(), name="listar-funcao"),
    path('listar/medico/', MedicoList.as_view(), name="listar-medico"),
    path('listar/funcionario/', FuncionarioList.as_view(), name="listar-funcionario"),
    path('listar/consulta/', ConsultaList.as_view(), name="listar-consulta"),
]