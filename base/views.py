from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


from .models import *

# Create your views here.


# @login_required
# def dashboard(request):
#     user = request.user
#     tasks = Task.objects.filter(assigned_to=user)
#     is_admin = user.is_staff
#     return render(request, 'dashboard.html', {'tasks': tasks, 'is_admin': is_admin})




def home(request):
    return render(request, 'home.html')

def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)

def loginPage(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {'form': form}
    return render(request, 'login.html', context)


def dashboard(request):
    return render(request, 'dashboard.html')

def matters(request):
    matter = Matter.objects.all()
    context = {'matter': matter}
    return render(request, 'matters.html', context)