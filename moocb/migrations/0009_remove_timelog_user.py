# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moocb', '0008_auto_20141220_1819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timelog',
            name='user',
        ),
    ]
