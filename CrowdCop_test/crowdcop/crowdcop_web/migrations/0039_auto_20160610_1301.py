# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-06-10 17:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdcop_web', '0038_crowdcopuser_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crowdcopuser',
            name='profile_picture',
            field=models.ImageField(default='default_image.png', upload_to=b''),
        ),
    ]
