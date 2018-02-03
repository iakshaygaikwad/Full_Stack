# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-28 03:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quora', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=124)),
                ('code', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='dept',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quora.Department'),
        ),
    ]