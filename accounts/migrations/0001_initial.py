# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Currency'
        db.create_table('accounts_currency', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal('accounts', ['Currency'])

        # Adding model 'AccountType'
        db.create_table('accounts_accounttype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('liability', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('accounts', ['AccountType'])

        # Adding model 'Person'
        db.create_table('accounts_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('accounts', ['Person'])

        # Adding model 'Account'
        db.create_table('accounts_account', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('currency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.Currency'])),
            ('account_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.AccountType'])),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.Person'])),
        ))
        db.send_create_signal('accounts', ['Account'])

        # Adding model 'Transaction'
        db.create_table('accounts_transaction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.Account'])),
            ('amount', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('accounts', ['Transaction'])


    def backwards(self, orm):
        # Deleting model 'Currency'
        db.delete_table('accounts_currency')

        # Deleting model 'AccountType'
        db.delete_table('accounts_accounttype')

        # Deleting model 'Person'
        db.delete_table('accounts_person')

        # Deleting model 'Account'
        db.delete_table('accounts_account')

        # Deleting model 'Transaction'
        db.delete_table('accounts_transaction')


    models = {
        'accounts.account': {
            'Meta': {'ordering': "['name', 'owner']", 'object_name': 'Account'},
            'account_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.AccountType']"}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.Currency']"}),
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
        'accounts.transaction': {
            'Meta': {'ordering': "['date', 'account']", 'object_name': 'Transaction'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.Account']"}),
            'amount': ('django.db.models.fields.FloatField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['accounts']