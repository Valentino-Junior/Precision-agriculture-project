# Generated by Django 3.2.5 on 2021-08-12 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0004_auto_20210812_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='humidity',
            field=models.FloatField(default=1, verbose_name='humidity'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='precipitation',
            field=models.FloatField(default=1, verbose_name='precipitation'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='soil_density',
            field=models.FloatField(default=1, verbose_name='soil density'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='solar_radiation',
            field=models.FloatField(default=1, verbose_name='radiation'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='surface_pressure',
            field=models.FloatField(default=1, verbose_name='pressure'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='temperature',
            field=models.FloatField(default=1, verbose_name='temperature'),
        ),
    ]
