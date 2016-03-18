# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import ckeditor.fields
import datetime
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('kblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(verbose_name='Nombre', max_length=128, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='short_description',
            field=models.TextField(verbose_name='Descripcion corta', blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='body_draft',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(verbose_name='Categoria', to='kblog.Category', default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 2, 15, 7, 44, 767662, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='published_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 2, 15, 7, 58, 467177, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(verbose_name='Tags', help_text='A comma-separated list of tags.', to='taggit.Tag', through='taggit.TaggedItem'),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(verbose_name='Titulo', max_length=255, default=''),
            preserve_default=False,
        ),
    ]
