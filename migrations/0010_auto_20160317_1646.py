# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kblog', '0009_auto_20160317_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='link',
            field=models.ForeignKey(blank=True, null=True, to='kblog.Link'),
        ),
    ]
