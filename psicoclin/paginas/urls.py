from django.urls import path

from .views import Index, EstadoCreate, CidadeCreate, PessoaCreate, FuncaoCreate
from .views import EstadoUpdate, CidadeUpdate, PessoaUpdate, FuncaoUpdate
from .views import EstadoDelete, CidadeDelete, PessoaDelete, FuncaoDelete
from .views import EstadoList, CidadeList, PessoaList, FuncaoList


urlpatterns = [
    path('', Index.as_view(), name="index"),

    path('cadastrar/estado', EstadoCreate.as_view(), name="cadastrar-estado"),
    path('cadastrar/cidade', CidadeCreate.as_view(), name="cadastrar-cidade"),
    path('cadastrar/pessoa', PessoaCreate.as_view(), name="cadastrar-pessoa"),
    path('cadastrar/funcao', FuncaoCreate.as_view(), name="cadastrar-funcao"),

    path('editar/estado/<int:pk>/', EstadoUpdate.as_view(), name="editar-estado"),
    path('editar/cidade/<int:pk>/', CidadeUpdate.as_view(), name="editar-cidade"),
    path('editar/pessoa/<int:pk>/', PessoaUpdate.as_view(), name="editar-pessoa"),
    path('editar/funcao/<int:pk>/', FuncaoUpdate.as_view(), name="editar-funcao"),

    path('excluir/estado/<int:pk>/', EstadoDelete.as_view(), name="excluir-estado"),
    path('excluir/cidade/<int:pk>/', CidadeDelete.as_view(), name="excluir-cidade"),
    path('excluir/pessoa/<int:pk>/', PessoaDelete.as_view(), name="excluir-pessoa"),
      path('excluir/funcao/<int:pk>/', FuncaoDelete.as_view(), name="excluir-funcao"),

    path('listar/estado/', EstadoList.as_view(), name="listar-estado"),
    path('listar/cidade/', CidadeList.as_view(), name="listar-cidade"),
    path('listar/pessoa/', PessoaList.as_view(), name="listar-pessoa"),
    path('listar/funcao/', FuncaoList.as_view(), name="listar-funcao"),
]