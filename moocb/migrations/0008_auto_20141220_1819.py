# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moocb', '0007_auto_20141220_1711'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='timelog',
            options={'ordering': ['date']},
        ),
        migrations.AlterField(
            model_name='timelog',
            name='goal',
            field=models.ForeignKey(to='moocb.Goal'),
            preserve_default=True,
        ),
    ]
