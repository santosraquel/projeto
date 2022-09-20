from django.urls import path

from .views import ConsultaCreate
from .views import ConsultaUpdate
from .views import ConsultaDelete
from .views import ConsultaList

urlpatterns = [
    path('cadastrar/consulta/', ConsultaCreate.as_view(),
         name='cadastrar-consulta'),
 
    path('editar/consulta/<int:pk>/',
         ConsultaUpdate.as_view(), name='editar-consulta'),
    
    path('excluir/consulta/<int:pk>/',
         ConsultaDelete.as_view(), name='excluir-consulta'),
   
    path('listar/consulta/', ConsultaList.as_view(),
         name='listar-consulta'),
    
]
