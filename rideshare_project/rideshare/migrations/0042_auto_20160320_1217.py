# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0041_auto_20160320_1215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passanger',
            name='id',
        ),
        migrations.AlterField(
            model_name='passanger',
            name='journey',
            field=models.ForeignKey(primary_key=True, serialize=False, to='rideshare.Journey'),
        ),
    ]
