from django.shortcuts import render
from django.http import HttpResponse
from EmployeeApp.models import Users

# Create your views here.

def index(request):
    userDetails=Users.objects.all

    return render(request,"index.html",{'EmpDetails':userDetails})

