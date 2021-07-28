from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



# Create your views here.
def signupform(request):


    return render(request, 'signup.html', )


def registerform(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            myuser = form.save()
            p = UserProfile(user=myuser)
            p.first_name = myuser.first_name
            p.last_name = myuser.last_name
            p.save()
            # login(request,myuser)
            return redirect('signupform')
            messages.success(request, 'Your Account Has Been Created!')
        else:
            messages.warning(request,form.errors)
            return redirect('signupform')


    return render(request, 'signup.html')


def loginform(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid username/password')
        


    return render(request,'signup.html')


def logoutfunc(request):
    logout(request)
    return redirect('index')


# @login_required(login_url='/login')
def userprofile(request):
    profile = UserProfile.objects.get(user__username = request.user.username)

    context = {
        'profile': profile,
    }

    return render(request, 'userprofile.html', context)


@login_required(login_url='/login')
def profileupdate(request):
    if request.method == 'POST':
        profileform = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if profileform.is_valid:
            profileform.save()
            messages.success(request, 'Your Account has been updated')
            return redirect('userprofile')
    else:
        profileform = ProfileUpdateForm(instance=request.user.userprofile)
        profile = UserProfile.objects.filter(user_id=request.user.id).first()


        context = {
            'profileform': profileform,
        }
    
    return render(request, 'profileupdate.html', context)