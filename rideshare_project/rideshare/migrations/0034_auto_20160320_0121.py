# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0033_auto_20160320_0121'),
    ]

    operations = [
        migrations.AddField(
            model_name='journey',
            name='make',
            field=models.ManyToManyField(related_name=b'carMake', null=True, to='rideshare.Vehicle'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='journey',
            name='model',
            field=models.ManyToManyField(related_name=b'carModel', null=True, to='rideshare.Vehicle'),
            preserve_default=True,
        ),
    ]
