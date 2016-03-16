# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0003_auto_20160316_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users_reg',
            name='users',
            field=models.OneToOneField(to='rideshare.Vehicle'),
        ),
    ]
