from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


from .models import *
from .decorators import unauthenticated_user
from .forms import TaskForm

# Create your views here.

# create a task
@login_required(login_url='login')
def create_task(request):
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            return redirect('tasks')
    else:
        form = TaskForm()
    
    context = {'form': form}
    return render(request, 'create_task.html', context)







@login_required(login_url='login')
def tasks(request):
    user = request.user
    tasks = Task.objects.filter(Q(assigned_to=user) | Q(created_by=user))
    is_admin = user.is_staff
    context = {'tasks': tasks, 'is_admin': is_admin}
    return render(request, 'tasks.html', context)

# @login_required
# def matters(request):
#     user = request.user
#     matters = Matter.objects.filter(assigned_to=user)
#     is_admin = user.is_staff
#     context = {'matters': matters, 'is_admin': is_admin}
#     return render(request, 'matters.html', context)



@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')




@unauthenticated_user
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



@unauthenticated_user
def loginPage(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Username OR password is incorrect')

    context = {'form': form}
    return render(request, 'login.html', context)



@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')



@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html')


def userPage(request):
    context = {}
    return render(request, 'user.html')



@login_required(login_url='login')
def matters(request):
    matter = Matter.objects.all()
    context = {'matter': matter}
    return render(request, 'matters.html', context)