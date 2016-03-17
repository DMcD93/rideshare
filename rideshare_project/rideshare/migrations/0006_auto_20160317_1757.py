# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0005_auto_20160316_1721'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users_reg',
            old_name='users',
            new_name='user',
        ),
    ]
