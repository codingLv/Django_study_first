# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 06:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170725_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
    ]
