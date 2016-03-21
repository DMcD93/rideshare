# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rideshare', '0020_auto_20160319_2109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journey',
            name='driver',
        ),
        migrations.AddField(
            model_name='journey',
            name='user',
            field=models.ManyToManyField(related_name=b'driver', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
