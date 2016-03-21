# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0042_auto_20160320_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passanger',
            name='backLeft',
            field=models.ForeignKey(related_name=b'backLeft', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='passanger',
            name='backRight',
            field=models.ForeignKey(related_name=b'backRight', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='passanger',
            name='front',
            field=models.ForeignKey(related_name=b'front', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='passanger',
            unique_together=set([('front', 'backLeft', 'backRight')]),
        ),
    ]
