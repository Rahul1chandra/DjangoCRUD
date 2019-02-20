# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class AccountRisk(models.Model):
    accountId = models.AutoField(primary_key=True)
    acctRisk = models.CharField(max_length=200)
    customer_name = models.CharField(max_length=200)
    account_name = models.CharField(max_length=200)


class Account(models.Model):
    STAGE_CHOICES = (
        ("WON", 'WON'),
        ("LOST", 'LOST'), 
    )
    accChildId = models.AutoField(primary_key=True)
    accountRisk = models.ForeignKey(AccountRisk, on_delete=models.CASCADE)
    Potential = models.CharField(max_length=200)
    pipline = models.CharField(max_length=200)
    stage = models.CharField(max_length=4, choices=STAGE_CHOICES)