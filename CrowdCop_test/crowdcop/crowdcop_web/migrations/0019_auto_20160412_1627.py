# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-12 20:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdcop_web', '0018_auto_20160412_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tip',
            name='suspect_identity',
            field=models.CharField(max_length=128, verbose_name='Who did you see? (If known, enter a name or a name known by)'),
        ),
    ]
