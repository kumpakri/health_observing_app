# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20150830_0202'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='enterdate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
