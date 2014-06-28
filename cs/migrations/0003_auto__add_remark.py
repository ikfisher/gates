# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'remark'
        db.create_table(u'cs_remark', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('words', self.gf('django.db.models.fields.CharField')(default='', max_length=128)),
        ))
        db.send_create_signal(u'cs', ['remark'])


    def backwards(self, orm):
        # Deleting model 'remark'
        db.delete_table(u'cs_remark')


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
            'words': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128'})
        }
    }

    complete_apps = ['cs']