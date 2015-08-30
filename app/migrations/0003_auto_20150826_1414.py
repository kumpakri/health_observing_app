# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150826_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='value',
            field=models.CharField(max_length=80),
        ),
    ]
