# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-06 16:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0005_auto_20191006_1522'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='location',
            new_name='name',
        ),
    ]