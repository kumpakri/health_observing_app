# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.CharField(max_length=4, choices=[('food', 'food'), ('med', 'medication'), ('ex', 'excerise'), ('con', 'conditions')])),
                ('value', models.TextField()),
            ],
        ),
    ]
