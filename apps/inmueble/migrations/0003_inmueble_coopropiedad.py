# Generated by Django 2.1 on 2018-08-18 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coopropiedad', '0002_remove_coopropiedad_inmuebles'),
        ('inmueble', '0002_auto_20180818_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='inmueble',
            name='coopropiedad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='inmuebles', to='coopropiedad.Coopropiedad'),
        ),
    ]