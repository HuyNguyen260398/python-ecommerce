# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-08-11 14:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0004_auto_20190811_2126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marketingpreference',
            old_name='update',
            new_name='updated',
        ),
    ]
