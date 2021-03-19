# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-08-22 00:29
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_productfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productfile',
            name='file',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='D:\\Documents\\workspace\\python-ecommerce\\static_cdn\\protected_media'), upload_to=products.models.upload_product_file_loc),
        ),
    ]