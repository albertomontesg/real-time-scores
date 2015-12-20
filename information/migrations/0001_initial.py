# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-20 12:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Masculí'), ('F', 'Femení')], default='M', max_length=10)),
                ('url', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]