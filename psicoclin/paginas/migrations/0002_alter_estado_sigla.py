# Generated by Django 4.0.3 on 2022-05-23 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estado',
            name='sigla',
            field=models.CharField(max_length=2, unique=True),
        ),
    ]
