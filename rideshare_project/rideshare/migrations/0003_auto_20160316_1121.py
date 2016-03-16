# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0002_remove_journey_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='travelling_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='journey',
            name='travelling_time',
            field=models.TimeField(null=True),
        ),
    ]
