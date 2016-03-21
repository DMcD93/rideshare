# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0016_auto_20160319_1719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journey',
            name='id',
        ),
        migrations.AddField(
            model_name='journey',
            name='journey',
            field=models.AutoField(default=1, unique=True, serialize=False, primary_key=True),
            preserve_default=False,
        ),
    ]
