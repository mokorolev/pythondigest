# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-09 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digest', '0049_auto_20160509_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='additionally',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Additional info'),
        ),
    ]
