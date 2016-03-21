# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0019_auto_20160319_1754'),
    ]

    operations = [
        migrations.RenameField(
            model_name='journey',
            old_name='user',
            new_name='driver',
        ),
    ]
