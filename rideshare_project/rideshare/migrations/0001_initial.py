# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Journey',
            fields=[
                ('journey', models.AutoField(serialize=False, primary_key=True)),
                ('departure', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('travelling_date', models.DateField(null=True)),
                ('travelling_time', models.TimeField(null=True)),
                ('seatsAvailable', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(0)])),
                ('cost', models.IntegerField(validators=[django.core.validators.MaxValueValidator(50), django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'db_table': 'journey',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Passanger',
            fields=[
                ('journey', models.ForeignKey(primary_key=True, serialize=False, to='rideshare.Journey')),
            ],
            options={
                'db_table': 'passanger',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(max_length=150, null=True)),
                ('posted_at', models.DateTimeField()),
                ('posted_by', models.TextField(max_length=30, null=True)),
            ],
            options={
                'db_table': 'review',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Users_Reg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.BigIntegerField(validators=[django.core.validators.MaxValueValidator(99999999999L)])),
                ('age', models.IntegerField(default=18, null=True, validators=[django.core.validators.MaxValueValidator(80), django.core.validators.MinValueValidator(16)])),
                ('identity_number', models.CharField(max_length=8)),
            ],
            options={
                'db_table': 'users',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('reg_no', models.CharField(max_length=8)),
                ('make', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=30)),
                ('user', models.ForeignKey(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'vehicle',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='users_reg',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='passanger',
            name='backLeft',
            field=models.ForeignKey(related_name=b'backLeft', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='passanger',
            name='backRight',
            field=models.ForeignKey(related_name=b'backRight', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='passanger',
            name='front',
            field=models.ForeignKey(related_name=b'front', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='journey',
            name='user',
            field=models.ForeignKey(related_name=b'driver', to='rideshare.Vehicle', null=True),
            preserve_default=True,
        ),
    ]
