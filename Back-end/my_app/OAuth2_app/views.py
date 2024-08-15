
from django.shortcuts import render,redirect

from . forms import CreateUserForm, LoginForm

from .middlewares import author,guest
# Authentication models and functions

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login,logout


def home(request):
    return render(request,'OAuth2_app/index.html')

@guest
def register(request):

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save
            return redirect("login")

    context = {'registerForm':form}

    return render(request,'OAuth2_app/register.html', context=context)

@guest
def login(request):
    
    form = LoginForm()
    if request.method == "POST":
        form=LoginForm(request,data=request.POST)
        if form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            
            if user is not None:
                auth.login(request,user)
                return redirect ("dashboard")
            else:
                error= "Invalid Username or password"
    
    context = {'loginForm':form}
    
    return render(request,'OAuth2_app/login.html',context=context)


@author
def dashboard(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    return render(request,'OAuth2_app/dashboard.html')
