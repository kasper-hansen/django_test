# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Profile.created'
        db.add_column('persons_profile', 'created',
                      self.gf('django.db.models.fields.DateField')(auto_now_add=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Profile.last_modified'
        db.add_column('persons_profile', 'last_modified',
                      self.gf('django.db.models.fields.DateField')(auto_now=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Staff.title'
        db.add_column('persons_staff', 'title',
                      self.gf('django.db.models.fields.CharField')(default='ansat', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Profile.created'
        db.delete_column('persons_profile', 'created')

        # Deleting field 'Profile.last_modified'
        db.delete_column('persons_profile', 'last_modified')

        # Deleting field 'Staff.title'
        db.delete_column('persons_staff', 'title')


    models = {
        'persons.parent': {
            'Meta': {'object_name': 'Parent'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['persons.Profile']"})
        },
        'persons.profile': {
            'Meta': {'object_name': 'Profile'},
            'created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '128', 'null': 'True'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'last_modified': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'mobile_number': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'})
        },
        'persons.resident': {
            'Meta': {'object_name': 'Resident'},
            'history': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['persons.Profile']"})
        },
        'persons.staff': {
            'Meta': {'object_name': 'Staff'},
            'about': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'employed_since': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['persons.Profile']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['persons']