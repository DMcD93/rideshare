# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rideshare', '0037_passanger'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passanger',
            old_name='user',
            new_name='backRight',
        ),
        migrations.AddField(
            model_name='passanger',
            name='backLeft',
            field=models.ManyToManyField(related_name=b'backLeft', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='passanger',
            name='front',
            field=models.ManyToManyField(related_name=b'front', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]