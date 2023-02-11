from django.forms import ModelForm
from django import forms
from .models import *



class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['created_by', 'status', 'created_at', 'updated_at']
        widgets = {
            'assigned_to': forms.CheckboxSelectMultiple(),
        }