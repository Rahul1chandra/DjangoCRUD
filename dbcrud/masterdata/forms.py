from django import forms
from django.contrib.auth.models import User
from masterdata.models import EmployeeUser


class EmployeeForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ['username', 'password', 'email', 'first_name', 'last_name']