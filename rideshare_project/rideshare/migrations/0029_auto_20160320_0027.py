# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0028_auto_20160319_2225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='no_of_seats',
        ),
        migrations.AlterField(
            model_name='journey',
            name='seatsAvailable',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(1)]),
        ),
    ]
