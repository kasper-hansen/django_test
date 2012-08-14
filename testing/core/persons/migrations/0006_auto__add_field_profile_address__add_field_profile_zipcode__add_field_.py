# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Profile.address'
        db.add_column('persons_profile', 'address',
                      self.gf('django.db.models.fields.CharField')(default='her', max_length=100, null=True),
                      keep_default=False)

        # Adding field 'Profile.zipcode'
        db.add_column('persons_profile', 'zipcode',
                      self.gf('django.db.models.fields.IntegerField')(default=0, null=True),
                      keep_default=False)

        # Adding field 'Profile.city'
        db.add_column('persons_profile', 'city',
                      self.gf('django.db.models.fields.CharField')(default='Herrestrup', max_length=100, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Profile.address'
        db.delete_column('persons_profile', 'address')

        # Deleting field 'Profile.zipcode'
        db.delete_column('persons_profile', 'zipcode')

        # Deleting field 'Profile.city'
        db.delete_column('persons_profile', 'city')


    models = {
        'persons.parent': {
            'Meta': {'object_name': 'Parent'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['persons.Profile']"})
        },
        'persons.profile': {
            'Meta': {'object_name': 'Profile'},
            'address': ('django.db.models.fields.CharField', [], {'default': "'her'", 'max_length': '100', 'null': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'default': "'Herrestrup'", 'max_length': '100', 'null': 'True'}),
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
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'zipcode': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'})
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