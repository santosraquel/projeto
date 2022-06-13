from re import template
from django.urls import path
from django.contrib.auth import views

urlpatterns = [

    path('entrar/', views.LoginView.as_view(
        template_name='usuarios/form.html'
    ), name='login'),

    path('sair/', views.LogoutView.as_view(), name='logout'),

]
