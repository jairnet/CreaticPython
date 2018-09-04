# Generated by Django 2.1 on 2018-09-04 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Copropiedad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_copropiedad', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=50)),
                ('nit', models.CharField(max_length=20)),
                ('descripcion', models.TextField(max_length=200)),
                ('foto', models.ImageField(upload_to='coporpiedades/imagen')),
            ],
            options={
                'ordering': ['nombre_copropiedad'],
            },
        ),
    ]
