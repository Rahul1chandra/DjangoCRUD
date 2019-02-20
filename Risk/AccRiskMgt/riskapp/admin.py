# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from riskapp.models import AccountRisk, Account

admin.site.register(AccountRisk)

admin.site.register(Account)
