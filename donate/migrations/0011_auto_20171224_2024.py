# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-24 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0010_auto_20171216_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='Edition',
            field=models.CharField(choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third'), ('Forth', 'Forth'), ('Fifth', 'Fifth'), ('Sixth', 'Sixth'), ('Seventh', 'Seventh'), ('Eighth', 'Eighth'), ('Ninth', 'Ninth'), ('Tenth', 'Tenth')], max_length=10),
        ),
        migrations.AlterField(
            model_name='details',
            name='Status',
            field=models.CharField(choices=[('Open', 'Open'), ('Reserved', 'Reserved')], max_length=10),
        ),
    ]
