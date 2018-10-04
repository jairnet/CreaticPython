# Generated by Django 2.1 on 2018-09-10 09:45

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
            name='Copropiedad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=50)),
                ('nit', models.CharField(max_length=20)),
                ('descripcion', models.TextField(max_length=200)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='coporpiedades/imagen')),
                ('property_of', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='copropiedades', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
    ]
