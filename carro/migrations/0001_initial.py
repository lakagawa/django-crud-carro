# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 00:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=200)),
                ('marca', models.CharField(max_length=200)),
                ('ano', models.CharField(max_length=4)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]