# Generated by Django 3.2.5 on 2021-08-12 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0003_sensor_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensor',
            name='date',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='name',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='reading',
        ),
        migrations.AddField(
            model_name='sensor',
            name='humidity',
            field=models.IntegerField(default=1, verbose_name='humidity'),
        ),
        migrations.AddField(
            model_name='sensor',
            name='precipitation',
            field=models.IntegerField(default=1, verbose_name='precipitation'),
        ),
        migrations.AddField(
            model_name='sensor',
            name='soil_density',
            field=models.IntegerField(default=1, verbose_name='soil density'),
        ),
        migrations.AddField(
            model_name='sensor',
            name='solar_radiation',
            field=models.IntegerField(default=1, verbose_name='radiation'),
        ),
        migrations.AddField(
            model_name='sensor',
            name='surface_pressure',
            field=models.IntegerField(default=1, verbose_name='pressure'),
        ),
        migrations.AddField(
            model_name='sensor',
            name='temperature',
            field=models.IntegerField(default=1, verbose_name='temperature'),
        ),
    ]