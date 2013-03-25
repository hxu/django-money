from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    code = models.CharField(max_length=3)


class AccountType(models.Model):
    name = models.CharField(max_length=50)
    liability = models.BooleanField(default=False)


class Person(models.Model):
    name = models.CharField(max_length=50)


class Account(models.Model):
    name = models.CharField(max_length=100)
    currency = models.ForeignKey(Currency)
    account_type = models.ForeignKey(AccountType)
    owner = models.ForeignKey(Person)

    class Meta:
        ordering = ['name', 'owner']


class Transaction(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=100)
    account = models.ForeignKey(Account)
    amount = models.FloatField()

    class Meta:
        ordering = ['date', 'account']
        get_latest_by = 'date'
