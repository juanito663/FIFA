# Generated by Django 4.1.3 on 2022-11-29 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seleccion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_equipo', models.CharField(max_length=20)),
                ('n_entrenador', models.CharField(max_length=20)),
                ('n_estadio', models.CharField(max_length=20)),
                ('titulos', models.CharField(max_length=20)),
                ('n_ciudad', models.CharField(max_length=20)),
                ('p_origen', models.CharField(max_length=20)),
            ],
        ),
    ]