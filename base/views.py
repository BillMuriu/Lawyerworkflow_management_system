from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


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
    context = {'form': form}
    return render(request, 'register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'login.html')


def dashboard(request):
    return render(request, 'dashboard.html')

def matters(request):
    matter = Matter.objects.all()
    context = {'matter': matter}
    return render(request, 'matters.html', context)