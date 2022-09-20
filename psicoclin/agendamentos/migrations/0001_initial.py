# Generated by Django 3.2.12 on 2022-09-19 23:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataConsulta', models.DateField(verbose_name='Data')),
                ('horaConsulta', models.TimeField(verbose_name='Hora')),
                ('valorConsulta', models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Valor')),
                ('statusConsulta', models.BooleanField(verbose_name='Status')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
