# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rideshare', '0039_auto_20160320_1205'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passanger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('backLeft', models.ForeignKey(related_name=b'backLeft', to=settings.AUTH_USER_MODEL)),
                ('backRight', models.ForeignKey(related_name=b'backRight', to=settings.AUTH_USER_MODEL)),
                ('front', models.ForeignKey(related_name=b'front', to=settings.AUTH_USER_MODEL)),
                ('journey', models.ForeignKey(to='rideshare.Journey')),
            ],
            options={
                'db_table': 'passanger',
            },
            bases=(models.Model,),
        ),
    ]
