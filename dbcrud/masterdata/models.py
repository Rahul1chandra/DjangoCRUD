# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class EmployeeUser(models.Model):
    user = models.OneToOneField(User)
    temp_address = models.CharField(max_length=30, default="IN")
    
