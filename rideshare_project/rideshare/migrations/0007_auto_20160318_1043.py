# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0006_auto_20160317_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='departure',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='journey',
            name='destination',
            field=models.CharField(max_length=100),
        ),
    ]
