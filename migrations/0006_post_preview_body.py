# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('kblog', '0005_category_category_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='preview_body',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
