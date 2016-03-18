# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kblog', '0003_auto_20160312_0111'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='heading_iamge',
            new_name='heading_image',
        ),
    ]
