# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0017_auto_20160319_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='journey',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
