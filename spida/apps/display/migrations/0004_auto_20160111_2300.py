# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-11 23:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0003_auto_20160111_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]