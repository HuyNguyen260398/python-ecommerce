# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-08-11 14:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0002_marketingpreference_mailchimp_subscribed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marketingpreference',
            old_name='update',
            new_name='updated',
        ),
    ]