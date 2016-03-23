# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-20 11:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rideshare', '0034_auto_20160320_0121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passanger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'passanger',
            },
        ),
        migrations.RemoveField(
            model_name='passangers',
            name='journey',
        ),
        migrations.RemoveField(
            model_name='passangers',
            name='user',
        ),
        migrations.RemoveField(
            model_name='journey',
            name='make',
        ),
        migrations.RemoveField(
            model_name='journey',
            name='model',
        ),
        migrations.DeleteModel(
            name='Passangers',
        ),
        migrations.AddField(
            model_name='passanger',
            name='journey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rideshare.Journey'),
        ),
        migrations.AddField(
            model_name='passanger',
            name='user',
            field=models.ManyToManyField(related_name='backRight', to=settings.AUTH_USER_MODEL),
        ),
    ]