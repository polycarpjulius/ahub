from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from . models import *
from . forms import SignUpForm

# Create your views here.

def signup(request):
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)
        # check for password mismatch
        if form.is_valid():
            form.save()
            messages.info(request, 'succesful')
            return redirect('signup')
        else:
            messages.info(request, 'password mismatch')
            return redirect('signup')

    return render(request, 'user/signup.html',{"form":form})


def signOut(request):
    logout(request)
    return redirect('signin')


def signIn(request):
    """
    Log a user in.
    """
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)       
            return redirect('/')
        else:
            messages.info(request, 'invalid details')
            return redirect('signin')
    return render(request, 'user/signin.html')