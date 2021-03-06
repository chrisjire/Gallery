# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-06 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0004_editor_phone_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='editor',
            options={'ordering': ['first_name'], 'verbose_name': 'Editor', 'verbose_name_plural': 'Editors'},
        ),
        migrations.AlterModelOptions(
            name='images',
            options={'verbose_name': 'Image', 'verbose_name_plural': 'Images'},
        ),
        migrations.AlterModelOptions(
            name='tags',
            options={'verbose_name': 'tag', 'verbose_name_plural': 'tags'},
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='images',
            name='image_name',
            field=models.CharField(max_length=50),
        ),
    ]
