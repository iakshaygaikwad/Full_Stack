# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-28 04:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quora', '0005_remove_user_dept'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile_number',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]
