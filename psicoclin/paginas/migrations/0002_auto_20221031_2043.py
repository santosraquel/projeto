# Generated by Django 3.2.12 on 2022-10-31 23:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consulta',
            old_name='usuario',
            new_name='agendada_por',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='usuario',
        ),
    ]
