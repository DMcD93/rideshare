# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0009_auto_20160319_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='model',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='make',
            field=models.CharField(max_length=30),
        ),
    ]
