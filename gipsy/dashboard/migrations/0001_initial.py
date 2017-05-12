# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GipsyDashboardMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('url', models.CharField(blank=True, max_length=255, null=True, verbose_name='Url')),
                ('order', models.PositiveSmallIntegerField(verbose_name='Order')),
                ('icon', models.CharField(help_text='Font awesome class \
                                                     http://fortawesome.github.io/Font-Awesome/icons/ ie: fa-circle',
                 max_length=20,           verbose_name='icon')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                             to='dashboard.GipsyDashboardMenu')),
            ],
            options={
                'abstract': False,
                'ordering': ['order'],
            },
        ),
    ]
