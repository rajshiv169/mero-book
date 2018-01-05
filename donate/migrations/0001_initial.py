# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-05 08:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='t', max_length=200)),
                ('Class', models.PositiveSmallIntegerField(default='5')),
                ('Publisher', models.CharField(default='t', max_length=200)),
                ('Edition', models.CharField(default='t', max_length=100)),
                ('Your_District', models.CharField(default='t', max_length=100)),
                ('Phone_number', models.CharField(default='5', max_length=100)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
