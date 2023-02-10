from django.forms import ModelForm
from .models import *



class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['created_by', 'status', 'created_at', 'updated_at']