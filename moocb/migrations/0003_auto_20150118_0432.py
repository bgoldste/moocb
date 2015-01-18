# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import moocb.models


class Migration(migrations.Migration):

    dependencies = [
        ('moocb', '0002_incentive_is_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='end_date',
            field=models.DateField(default=moocb.models.get_end),
            preserve_default=True,
        ),
    ]
