# Generated by Django 3.2.12 on 2022-09-19 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0003_cidade_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('funcao', models.CharField(max_length=50, verbose_name='Função')),
                ('descricao', models.TextField(verbose_name='Descrição')),
            ],
        ),
    ]
