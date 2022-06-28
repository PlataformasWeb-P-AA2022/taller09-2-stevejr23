# Generated by Django 4.0.5 on 2022-06-15 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('futbolec', '0003_alter_equipo_siglas_alter_equipo_twitter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campeonatosequipo',
            name='anio',
            field=models.IntegerField(verbose_name='Año'),
        ),
        migrations.AlterField(
            model_name='campeonatosequipo',
            name='campeonato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loscampeonatos', to='futbolec.campeonato'),
        ),
        migrations.AlterField(
            model_name='campeonatosequipo',
            name='equipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='losequipos', to='futbolec.equipo'),
        ),
    ]