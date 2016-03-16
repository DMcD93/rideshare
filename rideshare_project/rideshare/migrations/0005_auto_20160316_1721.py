# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0004_auto_20160316_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users_reg',
            name='users',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
