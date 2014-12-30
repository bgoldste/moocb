# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moocb', '0006_auto_20141220_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='time_goal',
            field=models.PositiveIntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='goal',
            name='time_worked',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='timelog',
            name='time_to_add',
            field=models.PositiveIntegerField(),
            preserve_default=True,
        ),
    ]
