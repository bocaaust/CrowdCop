# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-12 20:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdcop_web', '0012_tip_campaign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tip',
            name='suspect_race',
            field=models.CharField(choices=[('UNKNOWN', 'Unknown'), ('ASIAN', 'Asian'), ('BLACK', 'Black'), ('CAUCASIAN', 'Caucasian'), ('HISPANIC/LATINO', 'Hispanic/Latino'), ('NATIVE AMERICAN', 'Native American'), ('OTHER', 'Other')], max_length=30),
        ),
    ]