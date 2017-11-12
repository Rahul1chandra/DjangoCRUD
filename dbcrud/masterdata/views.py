from __future__ import unicode_literals
from django.shortcuts import render, redirect
from masterdata.forms import EmployeeForm
from django.http import HttpResponse

def signup(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            return render(request, 'signup.html', {'form': form,'success': "successfullyRegister"})
        else:

            return render(request, 'signup.html', {'form': form,'error': "try again"})

    else:
        return render(request, 'signup.html', {'form': form})


