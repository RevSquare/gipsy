# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'GipsyToolbarMenu.url'
        db.alter_column(u'gipsy_toolbar_gipsytoolbarmenu', 'url', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'GipsyToolbarMenu.url'
        raise RuntimeError("Cannot reverse this migration. 'GipsyToolbarMenu.url' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'GipsyToolbarMenu.url'
        db.alter_column(u'gipsy_toolbar_gipsytoolbarmenu', 'url', self.gf('django.db.models.fields.CharField')(max_length=255))

    models = {
        u'gipsy_toolbar.gipsytoolbarmenu': {
            'Meta': {'ordering': "['order']", 'object_name': 'GipsyToolbarMenu'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gipsy_toolbar.GipsyToolbarMenu']", 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['gipsy_toolbar']