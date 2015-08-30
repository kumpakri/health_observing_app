# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20150827_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='category',
            field=models.CharField(max_length=4, choices=[('food', 'food'), ('med', 'medication'), ('ex', 'exercise'), ('con', 'conditions')]),
        ),
    ]
