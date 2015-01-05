# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('url', models.URLField(max_length=300)),
                ('time_goal', models.PositiveIntegerField(null=True)),
                ('start_date', models.DateField(default=datetime.datetime.now)),
                ('end_date', models.DateField(default=datetime.datetime(2015, 2, 14, 0, 0))),
                ('time_worked', models.PositiveIntegerField(default=0)),
                ('last_worked', models.DateField(null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Incentive',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total_pledge', models.PositiveIntegerField(default=3000)),
                ('amount_refunded', models.PositiveIntegerField(default=0)),
                ('refund_increment', models.FloatField(default=0.25, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('goal', models.OneToOneField(to='moocb.Goal')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email_address', models.EmailField(unique=True, max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TimeLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('time_to_add', models.PositiveIntegerField()),
                ('goal', models.ForeignKey(to='moocb.Goal')),
            ],
            options={
                'ordering': ['date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('goal', models.CharField(max_length=300)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
