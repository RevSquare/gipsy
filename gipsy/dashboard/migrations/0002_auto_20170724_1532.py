# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gipsydashboardmenu',
            name='content_type',
            field=models.ForeignKey(blank=True, to='contenttypes.ContentType', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gipsydashboardmenu',
            name='icon',
            field=models.CharField(help_text='Font awesome class                                         http://fortawesome.github.io/Font-Awesome/icons/                                         ie: fa-circle', max_length=20, verbose_name='icon'),
            preserve_default=True,
        ),
    ]
