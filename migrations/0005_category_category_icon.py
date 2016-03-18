# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kblog', '0004_auto_20160312_0112'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_icon',
            field=models.CharField(default='file-text-o', choices=[('picture-o', 'Picture'), ('file-text-o', 'Document'), ('video-camera', 'Video'), ('music', 'Music')], verbose_name='Icono de categoria', max_length=20),
        ),
    ]
