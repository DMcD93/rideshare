# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0025_auto_20160319_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='user',
            field=models.ManyToManyField(related_name=b'driver', to=b'rideshare.Vehicle'),
        ),
    ]
