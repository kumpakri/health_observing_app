# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150826_1414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='date',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='time',
        ),
        migrations.AddField(
            model_name='entry',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
