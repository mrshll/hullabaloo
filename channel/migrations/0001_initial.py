# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Channel'
        db.create_table('channel_channel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('channel', ['Channel'])

        # Adding model 'View'
        db.create_table('channel_view', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('channel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['channel.Channel'])),
            ('stamp', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('channel', ['View'])

        # Adding model 'Post'
        db.create_table('channel_post', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=180, null=True, blank=True)),
            ('body', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('channel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['channel.Channel'])),
        ))
        db.send_create_signal('channel', ['Post'])


    def backwards(self, orm):
        
        # Deleting model 'Channel'
        db.delete_table('channel_channel')

        # Deleting model 'View'
        db.delete_table('channel_view')

        # Deleting model 'Post'
        db.delete_table('channel_post')


    models = {
        'channel.channel': {
            'Meta': {'object_name': 'Channel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'channel.post': {
            'Meta': {'object_name': 'Post'},
            'body': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'channel': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['channel.Channel']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '180', 'null': 'True', 'blank': 'True'})
        },
        'channel.view': {
            'Meta': {'object_name': 'View'},
            'channel': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['channel.Channel']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stamp': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['channel']
