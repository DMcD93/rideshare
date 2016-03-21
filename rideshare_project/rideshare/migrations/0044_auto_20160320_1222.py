# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0043_auto_20160320_1220'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='passanger',
            unique_together=set([('front', 'backLeft'), ('front', 'backLeft', 'backRight'), ('front', 'backRight'), ('backLeft', 'backRight')]),
        ),
    ]
