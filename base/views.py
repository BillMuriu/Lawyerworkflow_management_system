from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.


def registerPage(request):
    context = {}
    return render(request, 'register.html')

def loginPage(request):
    context = {}
    return render(request, 'login.html')


def dashboard(request):
    return render(request, 'dashboard.html')

def matters(request):
    matter = Matter.objects.all()
    context = {'matter': matter}
    return render(request, 'matters.html', context)