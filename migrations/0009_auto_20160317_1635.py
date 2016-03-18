# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kblog', '0008_auto_20160317_1626'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitem',
            old_name='target',
            new_name='link',
        ),
    ]
