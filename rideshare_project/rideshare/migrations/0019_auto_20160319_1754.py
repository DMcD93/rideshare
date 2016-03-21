# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0018_auto_20160319_1722'),
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
