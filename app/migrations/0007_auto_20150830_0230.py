# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_entry_enterdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='enterdate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
