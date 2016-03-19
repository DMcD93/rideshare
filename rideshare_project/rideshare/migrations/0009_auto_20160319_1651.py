# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0008_auto_20160319_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='no_of_seats',
            field=models.SmallIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(1)]),
        ),
    ]
