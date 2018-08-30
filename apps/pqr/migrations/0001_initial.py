# Generated by Django 2.1 on 2018-08-30 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('residentes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(blank=True, max_length=1000)),
                ('fecha', models.DateField()),
                ('emisor', models.CharField(choices=[('', ''), (1, 'Residente'), (2, 'Administrador')], max_length=15)),
                ('estado', models.CharField(blank=True, choices=[('', ''), (1, 'Solucionado'), (2, 'Sin Resolver'), (3, 'En Proceso')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Pqr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.CharField(choices=[('', ''), (1, 'Queja'), (2, 'Peteicion'), (3, 'Reclamo'), (4, 'Sugerencia'), (5, 'Felicitacion')], max_length=15)),
                ('estado', models.CharField(blank=True, choices=[('', ''), (1, 'Solucionado'), (2, 'Sin Resolver'), (3, 'En Proceso')], max_length=15)),
                ('residente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='residentes', to='residentes.Residente')),
            ],
            options={
                'ordering': ['motivo'],
            },
        ),
        migrations.AddField(
            model_name='comentarios',
            name='pqr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pqrs', to='pqr.Pqr'),
        ),
    ]