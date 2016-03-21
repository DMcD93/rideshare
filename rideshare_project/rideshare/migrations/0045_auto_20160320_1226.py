# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0044_auto_20160320_1222'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='passanger',
            unique_together=None,
        ),
    ]
