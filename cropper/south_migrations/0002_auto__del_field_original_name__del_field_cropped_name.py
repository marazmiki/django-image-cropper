# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Original.name'
        db.delete_column('cropper_original', 'name')

        # Deleting field 'Cropped.name'
        db.delete_column('cropper_cropped', 'name')


    def backwards(self, orm):
        
        # Adding field 'Original.name'
        db.add_column('cropper_original', 'name', self.gf('django.db.models.fields.CharField')(default='', max_length=255), keep_default=False)

        # Adding field 'Cropped.name'
        db.add_column('cropper_cropped', 'name', self.gf('django.db.models.fields.CharField')(default='', max_length=255), keep_default=False)


    models = {
        'cropper.cropped': {
            'Meta': {'object_name': 'Cropped'},
            'h': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'h_display': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
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
            'image_width': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['cropper']
