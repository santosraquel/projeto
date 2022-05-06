from django.db import models

class Estado(models.Model):
    sigla = models.CharField(max_length=2)
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.sigla


class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome + "/" + self.estado


class Pessoa(models.Model):

    nome = models.CharField(
        max_length=50, verbose_name="Nome", help_text="Digite seu nome completo")
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')
    email = models.CharField(max_length=100)

    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return '{} ({})'.format(self.nome, self.data_nascimento)
