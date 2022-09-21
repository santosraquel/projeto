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
        max_length=50, verbose_name="Nome", help_text="Digite seu nome completo do paciente")
    titular = models.CharField(
        max_length=50, verbose_name="Titular", help_text="Digite seu nome completo do titular")
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')
    rg = models.CharField(max_length=15, verbose_name="RG",
                          help_text="99.999.999-9")
    cpf = models.CharField(max_length=15, verbose_name="CPF", help_text="999.999.999-90")
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    numero = models.IntegerField(max_length=5)
    telefone = models.CharField(max_length=20, help_text="(DD)99999-9999")
    status = models.CharField()
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return '{} (CPF: {})'.format(self.nome, self.cpf)


class Funcao(models.Model):

    funcao = models.CharField(
        max_length=50, verbose_name="Função")
    descricao = models.TextField(verbose_name='Descrição')

    def __str__(self):
        return '{}'.format(self.funcao)


class Medico(models.Model):

    nome = models.CharField(
        max_length=50, verbose_name="Nome", help_text="Digite seu nome completo do médico")
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')
    rg = models.CharField(max_length=15, verbose_name="RG",
                          help_text="99.999.999-9")
    crm = models.CharField(
        max_length=15, verbose_name="CRM")
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    numero = models.IntegerField(max_length=5)
    telefone = models.CharField(max_length=20, help_text="(DD)99999-9999")
    status = models.CharField()
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return '{} (CRM: {})'.format(self.nome, self.crm)

    
class Funcionario(models.Model):

    nome = models.CharField(
        max_length=50, verbose_name="Nome", help_text="Digite seu nome completo do funcionário")
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')
    rg = models.CharField(max_length=15, verbose_name="RG",
                          help_text="99.999.999-9")
    cpf = models.CharField(
        max_length=15, verbose_name="CPF", help_text="999.999.999-90")
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    numero = models.IntegerField(max_length=5)
    telefone = models.CharField(max_length=20, help_text="(DD)99999-9999")
    status = models.CharField()
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return '{} (CPF: {})'.format(self.nome, self.cpf)


class Consulta(models.Model):

    data_consulta = models.DateField(verbose_name='Data da Consulta')
    hora_consulta = models.TimeField(verbose_name="Hora")
    status_consulta = models.BooleanField(verbose_name="Status")

    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT)

    def __str__(self):
        return '{} ({})'.format(self.paciente, self.medico)
