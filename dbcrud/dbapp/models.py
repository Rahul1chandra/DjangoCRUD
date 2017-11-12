# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Employee(models.Model):
	emp_id = models.AutoField(primary_key=True)
	emp_name = models.CharField(max_length=100)
	emp_emailid = models.EmailField(max_length = 100)
	emp_phn = models.CharField(max_length=100)