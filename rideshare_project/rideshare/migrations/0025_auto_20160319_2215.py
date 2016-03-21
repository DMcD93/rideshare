# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0024_auto_20160319_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='user',
            field=models.ManyToManyField(to=b'rideshare.Vehicle'),
        ),
    ]
