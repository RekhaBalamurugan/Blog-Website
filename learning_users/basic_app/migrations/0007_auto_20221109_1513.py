# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2022-11-09 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0006_auto_20221108_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, default='Logo_1.png', upload_to='profile_pics'),
        ),
    ]
