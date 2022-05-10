from django.urls import path

from .views import Index, EstadoCreate, CidadeCreate, PessoaCreate
from .views import EstadoUpdate, CidadeUpdate, PessoaUpdate


urlpatterns = [
    path('', Index.as_view(), name="index"),

    path('cadastrar/estado', EstadoCreate.as_view(), name="cadastrar-estado"),
    path('cadastrar/cidade', CidadeCreate.as_view(), name="cadastrar-cidade"),
    path('cadastrar/pessoa', PessoaCreate.as_view(), name="cadastrar-pessoa"),

    path('editar/estado/<int:pk>/', EstadoUpdate.as_view(), name="editar-estado"),
    path('editar/cidade/<int:pk>/', CidadeUpdate.as_view(), name="editar-cidade"),
    path('editar/pessoa/<int:pk>/', PessoaUpdate.as_view(), name="editar-pessoa"),
]