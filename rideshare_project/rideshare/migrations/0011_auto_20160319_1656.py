# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0010_auto_20160319_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='reg_no',
            field=models.CharField(max_length=8),
        ),
    ]
