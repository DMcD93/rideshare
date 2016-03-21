# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0013_auto_20160319_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='cost',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2),
        ),
    ]
