# Generated by Django 2.1.4 on 2018-12-19 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='komentarz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick', models.CharField(max_length=10, unique=True)),
                ('email', models.CharField(max_length=20)),
                ('tytul', models.CharField(max_length=50)),
                ('tresc', models.CharField(max_length=200)),
                ('create_data', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
