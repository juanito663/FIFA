# Generated by Django 4.1.3 on 2022-12-03 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seleccion', '0003_asociacion_rename_n_ciudad_equipo_ciudad_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asociacion',
            old_name='clubes',
            new_name='nombre_del_director',
        ),
    ]
