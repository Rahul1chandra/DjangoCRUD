# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

from riskapp.models import AccountRisk, Account


def dashboard(request):
    template = 'main_page.html'
    accountDetails = Account.objects.filter()
    acc_risk = AccountRisk.objects.values()
    response_dict = {
        "account":Account.objects.values(),
        "acc_risk":acc_risk,
        
        "child_account":accountDetails.count(),
        "account_won":accountDetails.filter(stage= "WON").count(),
        "High_Potential_Account":accountDetails.filter(Potential= "HP").count(),
        "High_PipeLine_Account":accountDetails.filter(pipline= "HP").count(),
        "last_Value" : Account.objects.last()
    }
    
    #import ipdb; ipdb.set_trace()

    return render(request, template, response_dict)


