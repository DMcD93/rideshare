# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0046_auto_20160320_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='cost',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(50), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='journey',
            name='seatsAvailable',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(0)]),
        ),
    ]
