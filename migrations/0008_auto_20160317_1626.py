# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kblog', '0007_auto_20160317_1451'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('target', models.ForeignKey(to='kblog.Post')),
            ],
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='target',
            field=models.ForeignKey(to='kblog.Link'),
        ),
    ]
