from django.shortcuts import render,redirect

from .forms import UserProfileInfoForm,UserForm,Login

from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponse

#newly added
from django.http import HttpResponseRedirect,HttpResponse

from django.contrib.auth.decorators import login_required

#from django.views.generic import ListView,DetailView
from .models import Post,UserProfileInfo
# Create your views here.
def index(request):
    return render(request,'basic_apps/index.html')

def register(request):

    registered= False
    
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)


        if user_form.is_valid() and profile_form.is_valid():

            user=user_form.save()
            user.set_password(user.password) 
            user.save()

            profile=profile_form.save(commit=False)

            profile.user =user

            if 'profile_pic' in request.FILES:
                print("Found it")
                profile.profile_pic=request.FILES['profile_pic']
            
            profile.save()

            registered =True 
        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'basic_apps/registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})

#newly added
def user_login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('index')
            else:
                return HttpResponse("Account not active")
        else:
            print("Someone tried to login and failed")
            print("Username:{} and password {}".format(username,password))
            return HttpResponse("Invalid login details")

    else:

        return render(request,'basic_apps/login.html',{})
@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

@login_required
def userprofile(request):
    return render(request,'basic_apps/profile.html')
    
""" def loginview(request):
    if request.method == 'POST':
        login_form = Login(request.POST)
        if login_form.is_valid():
            username=login_form.cleaned_data['username']
            password=login_form.cleaned_data['password']
            user= authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                messages.success(request,("you are logged in successfully!!"))
                return redirect('index')
            else:
                messages.success(request,("Found error while logging in. Try Again..."))
                #return redirect('login')
    else:
        login_form = Login()
    return render(request,'basic_apps/login.html',{'login_form':login_form})


def logoutview(request):
    logout(request)
    messages.success(request,("You are logged out!!"))
    return redirect('index')
 """


def blog(request):
    blogs= Post.objects.all()
    my_dic={'blogs':blogs}
    return render(request,'basic_apps/home.html',context=my_dic)

def blogpost(request, slug):
    blog = Post.objects.filter(slug=slug).first()
    return render(request, 'basic_apps/blogpost.html', {'blog': blog})

""" class HomeView(ListView):
    model=Post
    template_name='home.html' """