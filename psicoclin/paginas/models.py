from django.db import models
from django.contrib.auth.models import User

class Estado(models.Model):
    sigla = models.CharField(max_length=2, unique=True)
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome + " / " + self.sigla

class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome + "/" + self.estado.sigla


class Paciente(models.Model):

    nome = models.CharField(
        max_length=50, verbose_name="Nome", help_text="Digite seu nome completo")
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')
    email = models.CharField(max_length=100)

    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return '{} ({})'.format(self.nome, self.data_nascimento)


class Funcao(models.Model):

    funcao = models.CharField(
        max_length=50, verbose_name="Função")
    descricao = models.TextField(verbose_name='Descrição')

    def __str__(self):
        return '{}'.format(self.funcao)


class Medico(models.Model):

    nome = models.CharField(
        max_length=50, verbose_name="Nome", help_text="Digite seu nome completo")
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')
    email = models.CharField(max_length=100)

    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return '{} ({})'.format(self.nome, self.data_nascimento)

    
class Funcionario(models.Model):

    nome = models.CharField(
        max_length=50, verbose_name="Nome", help_text="Digite seu nome completo")
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')
    email = models.CharField(max_length=100)

    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return '{} ({})'.format(self.nome, self.data_nascimento)


class Consulta(models.Model):

    data_consulta = models.DateField(verbose_name='Data da Consulta')
    hora_consulta = models.TimeField(verbose_name="Hora")
    status_consulta = models.BooleanField(verbose_name="Status")

    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT)

    def __str__(self):
        return '{} ({})'.format(self.nome, self.data_nascimento)
