# Generated by Django 4.1.3 on 2022-12-02 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seleccion', '0002_equipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asociacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_de_la_asociacion', models.CharField(max_length=20)),
                ('pais', models.CharField(max_length=20)),
                ('clubes', models.CharField(max_length=20)),
                ('campeonato_nacional', models.CharField(max_length=20)),
                ('campeonato_internacional', models.CharField(max_length=20)),
                ('division', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameField(
            model_name='equipo',
            old_name='n_ciudad',
            new_name='ciudad',
        ),
        migrations.RenameField(
            model_name='equipo',
            old_name='n_entrenador',
            new_name='nombre_del_entrenador',
        ),
        migrations.RenameField(
            model_name='equipo',
            old_name='n_equipo',
            new_name='nombre_del_equipo',
        ),
        migrations.RenameField(
            model_name='equipo',
            old_name='n_estadio',
            new_name='nombre_del_estadio',
        ),
        migrations.RenameField(
            model_name='equipo',
            old_name='p_origen',
            new_name='pais_de_origen',
        ),
    ]
