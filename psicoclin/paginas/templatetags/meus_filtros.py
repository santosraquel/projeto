from operator import truediv
from django import template
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
