# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2022-11-08 08:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0003_delete_loginuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loginuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
