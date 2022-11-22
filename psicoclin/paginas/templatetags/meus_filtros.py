from operator import truediv
from django import template

from ..models import Consulta
register = template.Library()

@register.filter(name="remover")
def remover (texto, r):
    return texto.replace(r, "")


@register.filter(name="substituir")
def substituir(string, encontrar, subs):
    return string.replace(encontrar, subs)


@register.filter(name="verificardddpr")
def verificardddpr(telefone):
    ddd = telefone[0:4]
    if(ddd == "44"):
        return True
    else:
        return False


@register.filter(name="esta_no_grupo")
def esta_no_grupo (usuario, nome_do_grupo):
    if(usuario.groups.filter(name=nome_do_grupo)):
        return True
    else:
        return False


@register.filter(name="verificarStatus")
def verificarStatus(status):
    if(status == 'Pendente'):
        return 'bg-pendente'
    elif(status == 'Realizada'):
        return 'bg-realizada'
    elif(status == 'Cancelada'):
        return 'bg-cancelada'
    elif(status == 'Agendada'):
        return 'bg-agendada'
    else:
        return 'bg-light'


# @register.filter(name="textStatus")
# def textStatus(status):
#     if(status == 'Pendente' or status == 'Realizada' or status == 'Cancelada' or status == 'Agendada'):
#         return 'text-white'
#     else:
#         return 'text-dark'

@register.simple_tag(name="total_consultas")
def total_consultas():   
      return Consulta.objects.count()
    