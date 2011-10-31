# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Original'
        db.create_table('cropper_original', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('image_width', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('image_height', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal('cropper', ['Original'])

        # Adding model 'Cropped'
        db.create_table('cropper_cropped', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('original', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cropped', to=orm['cropper.Original'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('x', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('y', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('w', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('h', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('w_display', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('h_display', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('cropper', ['Cropped'])


    def backwards(self, orm):
        
        # Deleting model 'Original'
        db.delete_table('cropper_original')

        # Deleting model 'Cropped'
        db.delete_table('cropper_cropped')


    models = {
        'cropper.cropped': {
            'Meta': {'object_name': 'Cropped'},
            'h': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'h_display': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'original': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cropped'", 'to': "orm['cropper.Original']"}),
            'w': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'w_display': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'x': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'y': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'cropper.original': {
            'Meta': {'object_name': 'Original'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'image_height': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'image_width': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['cropper']
