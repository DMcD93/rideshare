# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0035_auto_20160320_1142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passanger',
            name='journey',
        ),
        migrations.RemoveField(
            model_name='passanger',
            name='user',
        ),
        migrations.DeleteModel(
            name='Passanger',
        ),
    ]
