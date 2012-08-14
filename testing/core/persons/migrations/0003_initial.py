# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Profile'
        db.create_table('persons_profile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=254, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=128, null=True)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=64, null=True)),
            ('mobile_number', self.gf('django.db.models.fields.CharField')(max_length=64, null=True)),
            ('facebook', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
        ))
        db.send_create_signal('persons', ['Profile'])

        # Adding model 'Resident'
        db.create_table('persons_resident', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['persons.Profile'])),
            ('history', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('persons', ['Resident'])

        # Adding model 'Staff'
        db.create_table('persons_staff', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['persons.Profile'])),
            ('about', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('employed_since', self.gf('django.db.models.fields.IntegerField')(max_length=4, null=True)),
        ))
        db.send_create_signal('persons', ['Staff'])

        # Adding model 'Parent'
        db.create_table('persons_parent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['persons.Profile'])),
        ))
        db.send_create_signal('persons', ['Parent'])


    def backwards(self, orm):
        # Deleting model 'Profile'
        db.delete_table('persons_profile')

        # Deleting model 'Resident'
        db.delete_table('persons_resident')

        # Deleting model 'Staff'
        db.delete_table('persons_staff')

        # Deleting model 'Parent'
        db.delete_table('persons_parent')


    models = {
        'persons.parent': {
            'Meta': {'object_name': 'Parent'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['persons.Profile']"})
        },
        'persons.profile': {
            'Meta': {'object_name': 'Profile'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '128', 'null': 'True'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
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
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['persons.Profile']"})
        }
    }

    complete_apps = ['persons']