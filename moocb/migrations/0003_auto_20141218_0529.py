# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moocb', '0002_goal_time_goal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='url',
            field=models.URLField(max_length=300),
            preserve_default=True,
        ),
    ]
