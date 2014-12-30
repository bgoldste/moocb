# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moocb', '0005_timelog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timelog',
            name='time_to_add',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
