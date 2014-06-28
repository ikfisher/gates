# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'remark.words'
        db.delete_column(u'cs_remark', 'words')

        # Adding field 'remark.message'
        db.add_column(u'cs_remark', 'message',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=128),
                      keep_default=False)

        # Adding field 'remark.who'
        db.add_column(u'cs_remark', 'who',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cs.author'], null=True),
                      keep_default=False)

        # Adding field 'remark.source'
        db.add_column(u'cs_remark', 'source',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cs.paper'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'remark.words'
        db.add_column(u'cs_remark', 'words',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=128),
                      keep_default=False)

        # Deleting field 'remark.message'
        db.delete_column(u'cs_remark', 'message')

        # Deleting field 'remark.who'
        db.delete_column(u'cs_remark', 'who_id')

        # Deleting field 'remark.source'
        db.delete_column(u'cs_remark', 'source_id')


    models = {
        u'cs.author': {
            'Meta': {'object_name': 'author'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'cs.paper': {
            'Meta': {'object_name': 'paper'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['cs.author']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'topic': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128'})
        },
        u'cs.remark': {
            'Meta': {'object_name': 'remark'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cs.paper']", 'null': 'True'}),
            'who': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cs.author']", 'null': 'True'})
        }
    }

    complete_apps = ['cs']