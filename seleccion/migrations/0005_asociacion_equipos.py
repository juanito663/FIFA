# Generated by Django 4.1.3 on 2022-12-03 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seleccion', '0004_rename_clubes_asociacion_nombre_del_director'),
    ]

    operations = [
        migrations.AddField(
            model_name='asociacion',
            name='equipos',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='seleccion.equipo'),
        ),
    ]