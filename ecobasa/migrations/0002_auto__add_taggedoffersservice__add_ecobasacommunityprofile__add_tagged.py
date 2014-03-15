# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TaggedOffersService'
        db.create_table(u'ecobasa_taggedoffersservice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'ecobasa_taggedoffersservice_items', to=orm['taggit.Tag'])),
            ('content_object', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ecobasa.EcobasaCommunityProfile'])),
        ))
        db.send_create_signal(u'ecobasa', ['TaggedOffersService'])

        # Adding model 'EcobasaCommunityProfile'
        db.create_table(u'ecobasa_ecobasacommunityprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group', self.gf('django.db.models.fields.related.OneToOneField')(related_name=u'profile', unique=True, to=orm['cosinnus.CosinnusGroup'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('contact_telephone', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('contact_street', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('contact_city', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('contact_zipcode', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('contact_country', self.gf('django.db.models.fields.CharField')(default=u'ZZ', max_length=2)),
            ('contact_show', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('visitors_num', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True)),
            ('visitors_accommodation', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('wishlist_materials', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('wishlist_tools', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('wishlist_seeds_kind', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('wishlist_seeds_num', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True)),
            ('wishlist_special_needs', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('offers_workshop_spaces', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('offers_learning_seminars', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('basic_inhabitants', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, null=True, blank=True)),
            ('basic_inhabitants_underage', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, null=True, blank=True)),
            ('basic_brings_together', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('basic_membership_status', self.gf('django.db.models.fields.CharField')(default=u'o', max_length=2)),
        ))
        db.send_create_signal(u'ecobasa', ['EcobasaCommunityProfile'])

        # Adding model 'TaggedOffersCreation'
        db.create_table(u'ecobasa_taggedofferscreation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'ecobasa_taggedofferscreation_items', to=orm['taggit.Tag'])),
            ('content_object', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ecobasa.EcobasaCommunityProfile'])),
        ))
        db.send_create_signal(u'ecobasa', ['TaggedOffersCreation'])

        # Adding model 'TaggedOffersSkill'
        db.create_table(u'ecobasa_taggedoffersskill', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'ecobasa_taggedoffersskill_items', to=orm['taggit.Tag'])),
            ('content_object', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ecobasa.EcobasaCommunityProfile'])),
        ))
        db.send_create_signal(u'ecobasa', ['TaggedOffersSkill'])


    def backwards(self, orm):
        # Deleting model 'TaggedOffersService'
        db.delete_table(u'ecobasa_taggedoffersservice')

        # Deleting model 'EcobasaCommunityProfile'
        db.delete_table(u'ecobasa_ecobasacommunityprofile')

        # Deleting model 'TaggedOffersCreation'
        db.delete_table(u'ecobasa_taggedofferscreation')

        # Deleting model 'TaggedOffersSkill'
        db.delete_table(u'ecobasa_taggedoffersskill')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'cosinnus.cosinnusgroup': {
            'Meta': {'ordering': "(u'name',)", 'object_name': 'CosinnusGroup'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'blank': 'True'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'cosinnus_groups'", 'blank': 'True', 'through': u"orm['cosinnus.CosinnusGroupMembership']", 'to': u"orm['auth.User']"})
        },
        u'cosinnus.cosinnusgroupmembership': {
            'Meta': {'unique_together': "((u'user', u'group'),)", 'object_name': 'CosinnusGroupMembership'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'memberships'", 'to': u"orm['cosinnus.CosinnusGroup']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'cosinnus_memberships'", 'to': u"orm['auth.User']"})
        },
        u'ecobasa.ecobasacommunityprofile': {
            'Meta': {'object_name': 'EcobasaCommunityProfile'},
            'basic_brings_together': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'basic_inhabitants': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'basic_inhabitants_underage': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'basic_membership_status': ('django.db.models.fields.CharField', [], {'default': "u'o'", 'max_length': '2'}),
            'contact_city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'contact_country': ('django.db.models.fields.CharField', [], {'default': "u'ZZ'", 'max_length': '2'}),
            'contact_show': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'contact_street': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'contact_telephone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'contact_zipcode': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "u'profile'", 'unique': 'True', 'to': u"orm['cosinnus.CosinnusGroup']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'offers_learning_seminars': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'offers_workshop_spaces': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'visitors_accommodation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'visitors_num': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'wishlist_materials': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'wishlist_seeds_kind': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'wishlist_seeds_num': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'wishlist_special_needs': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'wishlist_tools': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'ecobasa.ecobasauserprofile': {
            'Meta': {'object_name': 'EcobasaUserProfile'},
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'birth_date': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'bus_consumption': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'bus_has_driving_license': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'bus_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'bus_num_passengers': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'bus_others_can_drive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'default': "u'ZZ'", 'max_length': '2'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "u'o'", 'max_length': '2'}),
            'has_bus': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "u'cosinnus_profile'", 'unique': 'True', 'to': u"orm['auth.User']"}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'ecobasa.taggedinterest': {
            'Meta': {'object_name': 'TaggedInterest'},
            'content_object': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ecobasa.EcobasaUserProfile']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'ecobasa_taggedinterest_items'", 'to': u"orm['taggit.Tag']"})
        },
        u'ecobasa.taggedofferscreation': {
            'Meta': {'object_name': 'TaggedOffersCreation'},
            'content_object': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ecobasa.EcobasaCommunityProfile']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'ecobasa_taggedofferscreation_items'", 'to': u"orm['taggit.Tag']"})
        },
        u'ecobasa.taggedoffersservice': {
            'Meta': {'object_name': 'TaggedOffersService'},
            'content_object': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ecobasa.EcobasaCommunityProfile']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'ecobasa_taggedoffersservice_items'", 'to': u"orm['taggit.Tag']"})
        },
        u'ecobasa.taggedoffersskill': {
            'Meta': {'object_name': 'TaggedOffersSkill'},
            'content_object': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ecobasa.EcobasaCommunityProfile']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'ecobasa_taggedoffersskill_items'", 'to': u"orm['taggit.Tag']"})
        },
        u'ecobasa.taggedproduct': {
            'Meta': {'object_name': 'TaggedProduct'},
            'content_object': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ecobasa.EcobasaUserProfile']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'ecobasa_taggedproduct_items'", 'to': u"orm['taggit.Tag']"})
        },
        u'ecobasa.taggedskill': {
            'Meta': {'object_name': 'TaggedSkill'},
            'content_object': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ecobasa.EcobasaUserProfile']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'ecobasa_taggedskill_items'", 'to': u"orm['taggit.Tag']"})
        },
        u'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['ecobasa']