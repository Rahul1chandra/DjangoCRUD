from __future__ import unicode_literals
from dbapp.models import Employee
from django.shortcuts import render
from django.http import HttpResponseRedirect
from dbapp.forms import EmployeeForm
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
def login(request):
    data = {
        "name": "Rahul",
        "email": "rahul1chandra@gmail.com"
    }
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['psw']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            result = auth.login(request, user)
            return render(request, "success.html", {"user": user.username})
        else:
            data["status"] = "Login Failed"
            return render(request, "index.html", data)

    if request.method  == 'GET':
        if request.user.is_authenticated.value:
            
            return render(request, "success.html", {"user": request.user.username})
        else:
            return render(request, "index.html", data)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")


def updateEmployee(request):
    form = EmployeeForm(request.POST)
    empobj = Employee.objects.all()
    resp_dict = {
        'details': empobj,
        'form': form,
        'user': request.user.username,
    }
    if request.method == 'GET':
        return render(request, 'detail.html', resp_dict)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/updateEmployee/')


def deleterecord(request, id = None):
    if id == "all":
        Employee.objects.all().delete()
    else:
        delobj = Employee.objects.get(emp_id=id).delete()
    return redirect('/updateEmployee/')

def updaterecord(request, id = None):
    obj = Employee.objects.get(emp_id=id)
    form = EmployeeForm(request.POST)
    resp_dict = {'details': obj, 'form': form, }

    if request.method == 'GET':
        return render(request, 'update.html', resp_dict)

    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data['emp_name']
            email_id = form.cleaned_data['emp_emailid']
            emp_ph = form.cleaned_data['emp_phn']
            obj.emp_name = name
            obj.emp_emailid = email_id
            obj.emp_phn = emp_ph
            obj.save()
            return HttpResponseRedirect('/updateEmployee/')

    return redirect('/updateEmployee/')



    