from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Consulta(models.Model):
    dataConsulta = models.DateField(verbose_name="Data")
    horaConsulta = models.TimeField(verbose_name="Hora")
    valorConsulta = models.DecimalField(decimal_places=2, max_digits=9, default=0, verbose_name="Valor")
    statusConsulta = models.BooleanField(verbose_name="Status")

    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    # medico = models.ForeignKey(Pessoa, on_delete=models.PROTECT)
    # paciente = models.ForeignKey(Pessoa, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.dataConsulta}"

    # documento = models.CharField(
    #     max_length=20, verbose_name="CPF ou CNPJ", unique=True)

