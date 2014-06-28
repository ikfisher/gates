# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'author'
        db.create_table(u'cs_author', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal(u'cs', ['author'])

        # Adding model 'paper'
        db.create_table(u'cs_paper', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'cs', ['paper'])

        # Adding M2M table for field authors on 'paper'
        m2m_table_name = db.shorten_name(u'cs_paper_authors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('paper', models.ForeignKey(orm[u'cs.paper'], null=False)),
            ('author', models.ForeignKey(orm[u'cs.author'], null=False))
        ))
        db.create_unique(m2m_table_name, ['paper_id', 'author_id'])


    def backwards(self, orm):
        # Deleting model 'author'
        db.delete_table(u'cs_author')

        # Deleting model 'paper'
        db.delete_table(u'cs_paper')

        # Removing M2M table for field authors on 'paper'
        db.delete_table(db.shorten_name(u'cs_paper_authors'))


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
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['cs']