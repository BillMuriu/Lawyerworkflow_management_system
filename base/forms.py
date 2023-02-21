from django.forms import ModelForm
from django import forms
from .models import *



class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['created_by', 'created_at', 'updated_at']
        widgets = {
            'assigned_to': forms.CheckboxSelectMultiple(),
        }

    # def __init__(self, *args, **kwargs):
    #     self.request = kwargs.pop('request', None)
    #     super(TaskForm, self).__init__(*args, **kwargs)
    #     self.fields['assigned_to'].queryset = User.objects.exclude(pk=self.request.user.pk)


class MatterForm(forms.ModelForm):
    class Meta:
        model = Matter
        fields = ['type', 'title', 'description', 'category', 'ref_code', 'open_date', 'close_date', 'original_lawyer', 'current_lawyer', 'participants', 'private', 'individual_client', 'business_client']
        widgets = {
            'open_date': forms.SelectDateWidget,
            'close_date': forms.SelectDateWidget,
            'participants': forms.CheckboxSelectMultiple(),
        }
