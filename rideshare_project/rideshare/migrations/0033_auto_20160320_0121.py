# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0032_auto_20160320_0113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journey',
            name='make',
        ),
        migrations.RemoveField(
            model_name='journey',
            name='model',
        ),
    ]
