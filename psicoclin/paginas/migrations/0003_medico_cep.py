# Generated by Django 3.2.12 on 2022-11-21 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0002_auto_20221031_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='medico',
            name='cep',
            field=models.CharField(default=87712401, max_length=100),
            preserve_default=False,
        ),
    ]
