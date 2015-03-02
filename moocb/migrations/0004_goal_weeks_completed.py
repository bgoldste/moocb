# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moocb', '0003_auto_20150118_0432'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='weeks_completed',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
