from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.


def home(request):
    return render(request, 'home.html')

def room(request):
    return render(request, 'room.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def matters(request):
    matter = Matter.objects.all()
    context = {'matter': matter}
    return render(request, 'matters.html', context)