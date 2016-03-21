# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0045_auto_20160320_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passanger',
            name='backLeft',
            field=models.ForeignKey(related_name=b'backLeft', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='passanger',
            name='backRight',
            field=models.ForeignKey(related_name=b'backRight', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='passanger',
            name='front',
            field=models.ForeignKey(related_name=b'front', to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
