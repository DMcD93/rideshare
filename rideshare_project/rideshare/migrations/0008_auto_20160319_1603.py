# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0007_auto_20160318_1043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='registration_number',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='reg_no',
            field=models.CharField(max_length=8, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='make',
            field=models.CharField(max_length=50),
        ),
    ]
