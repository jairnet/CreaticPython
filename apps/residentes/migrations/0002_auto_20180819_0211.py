# Generated by Django 2.1 on 2018-08-19 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('residentes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='residente',
            name='arrendador',
            field=models.BooleanField(choices=[(True, 'Si'), (False, 'No')], default=False),
        ),
    ]
