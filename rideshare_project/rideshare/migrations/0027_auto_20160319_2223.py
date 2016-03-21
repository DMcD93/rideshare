# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0026_auto_20160319_2220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journey',
            name='is_return',
        ),
        migrations.AddField(
            model_name='journey',
            name='seatsAvailable',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
