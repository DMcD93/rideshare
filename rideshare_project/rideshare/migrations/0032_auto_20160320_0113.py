# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0031_auto_20160320_0032'),
    ]

    operations = [
        migrations.AddField(
            model_name='journey',
            name='make',
            field=models.ForeignKey(related_name=b'carMake', to='rideshare.Vehicle', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='journey',
            name='model',
            field=models.ForeignKey(related_name=b'carModel', to='rideshare.Vehicle', null=True),
            preserve_default=True,
        ),
    ]
