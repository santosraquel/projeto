from django.contrib import admin

from .models import Estado, Cidade, Paciente

admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Paciente)
