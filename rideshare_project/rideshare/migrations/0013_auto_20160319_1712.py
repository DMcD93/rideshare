# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0012_auto_20160319_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='journey',
            name='make',
            field=models.ForeignKey(related_name=b'vehicleMake', to='rideshare.Vehicle', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='journey',
            name='model',
            field=models.ForeignKey(related_name=b'vehicleModel', to='rideshare.Vehicle', null=True),
            preserve_default=True,
        ),
    ]
