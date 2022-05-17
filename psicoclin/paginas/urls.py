from django.urls import path

from .views import Index, EstadoCreate, CidadeCreate, PessoaCreate
from .views import EstadoUpdate, CidadeUpdate, PessoaUpdate
from .views import EstadoDelete, CidadeDelete, PessoaDelete
from .views import EstadoList


urlpatterns = [
    path('', Index.as_view(), name="index"),

    path('cadastrar/estado', EstadoCreate.as_view(), name="cadastrar-estado"),
    path('cadastrar/cidade', CidadeCreate.as_view(), name="cadastrar-cidade"),
    path('cadastrar/pessoa', PessoaCreate.as_view(), name="cadastrar-pessoa"),

    path('editar/estado/<int:pk>/', EstadoUpdate.as_view(), name="editar-estado"),
    path('editar/cidade/<int:pk>/', CidadeUpdate.as_view(), name="editar-cidade"),
    path('editar/pessoa/<int:pk>/', PessoaUpdate.as_view(), name="editar-pessoa"),

    path('excluir/estado/<int:pk>/', EstadoDelete.as_view(), name="excluir-estado"),
    path('excluir/cidade/<int:pk>/', CidadeDelete.as_view(), name="excluir-cidade"),
    path('excluir/pessoa/<int:pk>/', PessoaDelete.as_view(), name="excluir-pessoa"),

    path('listar/estado/', EstadoList.as_view(), name="listar-estado"),
]