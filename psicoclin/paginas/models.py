from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

status_CHOICES = [
    ('Ativo', 'Ativo'),
    ('Anativo', 'Inativo'),
]

status_consulta_CHOICES = [
    ('Pendente', 'Pendente'),
    ('Agendada', 'Agendada'),
    ('Realizada', 'Realizada'),
    ('Cancelada', 'Cancelada'),
]

class Estado(models.Model):
    sigla = models.CharField(max_length=2, unique=True)
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome + " / " + self.sigla

class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome + "/" + self.estado.sigla


class Paciente(models.Model):

    nome = models.CharField(
        max_length=50, verbose_name="Nome", help_text="Digite o nome completo do paciente")
    titular = models.CharField(
        max_length=50, verbose_name="Titular", help_text="Digite o nome completo do titular")
    nascimento = models.DateField()
    rg = models.CharField(max_length=15, verbose_name="RG",
                          help_text="99.999.999-9")
    cpf = models.CharField(max_length=15, verbose_name="CPF", help_text="999.999.999-90")
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    numero = models.CharField(max_length=5)
    telefone = models.CharField(max_length=20, help_text="(DD)99999-9999")
    status = models.CharField(
        max_length=20,
        choices=status_CHOICES,
        default='Ativo',
    )
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
        max_length=50, verbose_name="Nome", help_text="Digite o nome completo do médico")
    nascimento = models.DateField()
    rg = models.CharField(max_length=15, verbose_name="RG",
                          help_text="99.999.999-9")
    crm = models.CharField(
        max_length=15, verbose_name="CRM")
    cep = models.CharField(max_length=100)
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    numero = models.CharField(max_length=5)
    telefone = models.CharField(max_length=20, help_text="(DD)99999-9999")
    status = models.CharField(
        max_length=20,
        choices=status_CHOICES,
        default='Ativo',
    )
    cidade = models.CharField(max_length=100)
    # cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    funcao = models.ForeignKey(Funcao, on_delete=models.PROTECT)

    def __str__(self):
        return '{} (CRM: {} | Função{})'.format(self.nome, self.crm, self.funcao)

    
class Funcionario(models.Model):

    nome = models.CharField(
        max_length=50, verbose_name="Nome", help_text="Digite o nome completo do funcionario")
    nascimento = models.DateField()
    rg = models.CharField(max_length=15, verbose_name="RG",
                          help_text="99.999.999-9")
    cpf = models.CharField(max_length=15, verbose_name="CPF", help_text="999.999.999-90")
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    numero = models.CharField(max_length=5)
    telefone = models.CharField(max_length=20, help_text="(DD)99999-9999")
    status = models.CharField(
        max_length=20,
        choices=status_CHOICES,
        default='Ativo',
    )
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return '{} (CPF: {})'.format(self.nome, self.cpf)


class Consulta(models.Model):

    data = models.DateField()
    hora = models.CharField(max_length=5, verbose_name="Hora")
    status = models.CharField(
        max_length=20,
        choices=status_consulta_CHOICES,
        default='Pendente',
    )
    valor = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT)
    agendada_por = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return '{} ({})'.format(self.paciente, self.medico)
