# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('moocb', '0009_remove_timelog_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2015, 2, 14, 0, 0)),
            preserve_default=True,
        ),
    ]
