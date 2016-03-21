# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0038_auto_20160320_1201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passanger',
            name='backLeft',
        ),
        migrations.RemoveField(
            model_name='passanger',
            name='backRight',
        ),
        migrations.RemoveField(
            model_name='passanger',
            name='front',
        ),
        migrations.RemoveField(
            model_name='passanger',
            name='journey',
        ),
        migrations.DeleteModel(
            name='Passanger',
        ),
    ]
