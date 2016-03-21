# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rideshare', '0036_auto_20160320_1157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passanger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('journey', models.ForeignKey(to='rideshare.Journey')),
                ('user', models.ManyToManyField(related_name=b'backRight', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'passanger',
            },
            bases=(models.Model,),
        ),
    ]
