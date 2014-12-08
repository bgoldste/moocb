# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moocb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='time_goal',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
