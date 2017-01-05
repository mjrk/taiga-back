# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0007_auto_20160614_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='due_date',
            field=models.DateField(blank=True, null=True, verbose_name='due date')
        ),
    ]
