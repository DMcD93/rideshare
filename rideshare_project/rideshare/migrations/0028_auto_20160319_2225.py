# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0027_auto_20160319_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='seatsAvailable',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(1)]),
        ),
    ]
