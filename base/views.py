from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import migrations
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


from .models import *
from .decorators import unauthenticated_user
from .forms import TaskForm, MatterForm

# Create your views here.

# Generate a create_task view that will allow a user to create and assign a task to another user. Only the task creator and the assigned user should be able to see the task in their task list. The task creator should be able to edit the task and the assigned user should be able to mark the task as completed. The task creator should be able to delete the task. 

@login_required(login_url='login')
def matters(request):
    user = request.user
    try:
        lawyer = Lawyer.objects.get(user=user)
    except Lawyer.DoesNotExist:
        lawyer = None

    try:
        business_client = BusinessClient.objects.get(user=user)
    except BusinessClient.DoesNotExist:
        business_client = None

    try:
        individual_client = IndividualClient.objects.get(user=user)
    except IndividualClient.DoesNotExist:
        individual_client = None

    matters_filter = Q(original_lawyer=lawyer) | Q(current_lawyer=lawyer)

    if business_client:
        matters_filter |= Q(business_client=business_client)

    if individual_client:
        matters_filter |= Q(individual_client=individual_client)

    matters = Matter.objects.filter(matters_filter)

    is_admin = user.is_staff
    context = {'matters': matters, 'is_admin': is_admin}
    return render(request, 'matters.html', context)
    

@login_required(login_url='login')
def create_matter(request):
    if request.method == 'POST':
        form = MatterForm(request.POST)
        if form.is_valid():
            matter = form.save(commit=False)
            matter.original_lawyer = request.user.lawyer
            matter.save()
            form.save_m2m()
            return redirect('matters')
    else:
        form = MatterForm()
    return render(request, 'create_matter.html', {'form': form})





@login_required(login_url='login')
def matter_detail(request, pk):
    matter = get_object_or_404(Matter, pk=int(pk))
    user = request.user
    is_admin = user.is_staff
    context = {'matter': matter, 'is_admin': is_admin}
    return render(request, 'matter_detail.html', context)

@login_required(login_url='login')
def matter_tasks(request, pk):
    matter = get_object_or_404(Matter, pk=pk)
    user = request.user
    tasks = Task.objects.filter(Q(assigned_to=user) | Q(created_by=user), matter=matter)
    is_admin = user.is_staff
    context = {'tasks': tasks, 'is_admin': is_admin, 'matter': matter}
    return render(request, 'tasks.html', context)

@login_required(login_url='login')
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            assigned_users = form.cleaned_data['assigned_to']
            task.assigned_to.set(assigned_users)
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







