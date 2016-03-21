# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0021_auto_20160319_2112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='id',
        ),
        migrations.AlterField(
            model_name='journey',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='user',
            field=models.ForeignKey(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
