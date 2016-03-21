# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0015_auto_20160319_1717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journey',
            name='journey',
        ),
        migrations.AddField(
            model_name='journey',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
