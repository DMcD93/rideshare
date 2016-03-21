# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0030_passangers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passangers',
            name='user',
            field=models.ManyToManyField(related_name=b'backRight', null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
