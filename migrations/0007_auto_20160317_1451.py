# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kblog', '0006_post_preview_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='nombre del menu', default='Menu', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='nombre del item', default='Item', max_length=20)),
                ('position', models.PositiveIntegerField(default=1)),
                ('submenu', models.ForeignKey(blank=True, null=True, to='kblog.Menu')),
                ('target', models.ForeignKey(to='kblog.Post')),
            ],
            options={
                'ordering': ('position',),
            },
        ),
        migrations.AddField(
            model_name='menu',
            name='items',
            field=models.ManyToManyField(to='kblog.MenuItem'),
        ),
    ]
