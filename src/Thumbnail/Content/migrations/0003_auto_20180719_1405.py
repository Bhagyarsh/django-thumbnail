# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-19 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Content', '0002_auto_20180718_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='file',
            field=models.FileField(upload_to='Thumbnail/'),
        ),
    ]