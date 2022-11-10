""" from django.shortcuts import render,redirect
from .forms import FormName
from django.http import HttpResponseRedirect
from .models import ModelName
# Create your views here.

def index(request):
    return render(request,'index.html')

def form_name_view(request):
   
        form = FormName(request.POST or None)

        if form.is_valid():
            form.save()
            return redirect('/')
        
        return render(request,'form_sample.html',{'form':form}) 


 """
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from FormApp.models import ModelName
from FormApp.forms import NewUser

def index(request):
    return render(request,'index.html') 

def users(request):
   
        form = NewUser()
        if request.method == 'POST':
            form =NewUser(request.POST)
            if form.is_valid():
                form.save(commit=True)
                return index(request)
            else:
                print("Error form invalid..")

        return render(request,'signup.html',{'form':form})