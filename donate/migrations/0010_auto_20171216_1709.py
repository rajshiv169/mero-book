# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-16 11:24
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0009_auto_20171216_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='Class',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(13), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='details',
            name='Ward_number',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(36), django.core.validators.MinValueValidator(1)]),
        ),
    ]
