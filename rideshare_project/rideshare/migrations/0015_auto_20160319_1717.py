# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0014_auto_20160319_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journey',
            name='id',
        ),
        migrations.AddField(
            model_name='journey',
            name='journey',
            field=models.AutoField(default=100, serialize=False, primary_key=True),
            preserve_default=False,
        ),
    ]
