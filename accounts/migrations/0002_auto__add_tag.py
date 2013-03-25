# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tag'
        db.create_table('accounts_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=25)),
        ))
        db.send_create_signal('accounts', ['Tag'])

        # Adding M2M table for field tags on 'Transaction'
        db.create_table('accounts_transaction_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('transaction', models.ForeignKey(orm['accounts.transaction'], null=False)),
            ('tag', models.ForeignKey(orm['accounts.tag'], null=False))
        ))
        db.create_unique('accounts_transaction_tags', ['transaction_id', 'tag_id'])


    def backwards(self, orm):
        # Deleting model 'Tag'
        db.delete_table('accounts_tag')

        # Removing M2M table for field tags on 'Transaction'
        db.delete_table('accounts_transaction_tags')


    models = {
        'accounts.account': {
            'Meta': {'ordering': "['name', 'owner']", 'object_name': 'Account'},
            'account_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'accounts'", 'to': "orm['accounts.AccountType']"}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'accounts'", 'to': "orm['accounts.Currency']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.Person']"})
        },
        'accounts.accounttype': {
            'Meta': {'object_name': 'AccountType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'liability': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'accounts.currency': {
            'Meta': {'object_name': 'Currency'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'accounts.person': {
            'Meta': {'object_name': 'Person'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'accounts.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'accounts.transaction': {
            'Meta': {'ordering': "['date', 'account']", 'object_name': 'Transaction'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.Account']"}),
            'amount': ('django.db.models.fields.FloatField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'transactions'", 'symmetrical': 'False', 'to': "orm['accounts.Tag']"})
        }
    }

    complete_apps = ['accounts']