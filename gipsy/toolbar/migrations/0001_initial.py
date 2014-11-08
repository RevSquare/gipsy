# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GipsyToolbarMenu'
        db.create_table(u'gipsy_toolbar_gipsytoolbarmenu', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gipsy_toolbar.GipsyToolbarMenu'], null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('order', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'gipsy_toolbar', ['GipsyToolbarMenu'])


    def backwards(self, orm):
        # Deleting model 'GipsyToolbarMenu'
        db.delete_table(u'gipsy_toolbar_gipsytoolbarmenu')


    models = {
        u'gipsy_toolbar.gipsytoolbarmenu': {
            'Meta': {'ordering': "['order']", 'object_name': 'GipsyToolbarMenu'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gipsy_toolbar.GipsyToolbarMenu']", 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['gipsy_toolbar']