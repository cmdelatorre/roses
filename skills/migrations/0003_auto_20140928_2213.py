# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0002_role_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seniority',
            name='rank',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
