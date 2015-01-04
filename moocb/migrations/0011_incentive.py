# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('moocb', '0010_auto_20141231_0845'),
    ]

    operations = [
        migrations.CreateModel(
            name='Incentive',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total_pledge', models.FloatField(default=50.0, validators=django.core.validators.MinValueValidator(0.0))),
                ('amount_refunded', models.FloatField(default=0.0, validators=django.core.validators.MinValueValidator(0.0))),
                ('refund_increment', models.FloatField(default=0.25, validators=django.core.validators.MinValueValidator(0.0))),
                ('goal', models.OneToOneField(to='moocb.Goal')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
