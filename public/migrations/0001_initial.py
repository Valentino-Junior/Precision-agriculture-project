# Generated by Django 3.2.5 on 2021-07-30 23:06

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(max_length=200, null=True, verbose_name='first name')),
                ('last_name', models.CharField(max_length=200, null=True, verbose_name='last name')),
                ('username', models.CharField(max_length=200, unique=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True, verbose_name='email')),
                ('phone', models.CharField(max_length=200, null=True, verbose_name='phone number')),
                ('profile_pic', models.ImageField(null=True, upload_to='', verbose_name='profile_pic')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]