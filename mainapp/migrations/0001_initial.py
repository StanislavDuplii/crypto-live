# Generated by Django 3.2.2 on 2021-05-17 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('login', models.CharField(max_length=50, unique=True, verbose_name='Login')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='Email adress')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]