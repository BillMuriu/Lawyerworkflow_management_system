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


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'start_date', 'end_date', 'priority', 'matter', 'assigned_to', 'private']
        widgets = {
            'start_date': forms.SelectDateWidget,
            'end_date': forms.SelectDateWidget,
            'assigned_to': forms.CheckboxSelectMultiple(),
        }


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('name', 'link', 'description', 'category', 'file')

    file = forms.FileField(required=False)


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['category', 'subject', 'description', 'private', 'matter']


class IndividualClientForm(forms.ModelForm):
    class Meta:
        model = IndividualClient
        fields = ['first_name', 'last_name', 'middle_name', 'email', 'primary_phone', 'secondary_phone', 'address', 'website', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }


class BusinessClientForm(forms.ModelForm):
    class Meta:
        model = BusinessClient
        fields = ['name', 'email', 'primary_phone', 'secondary_phone', 'address', 'website', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }

class FeeNoteForm(forms.ModelForm):
    class Meta:
        model = FeeNote
        fields = ('matter', 'individual_client', 'business_client', 'billed_by', 'due_date', 'date_billed', 'billable', 'description')


class FirmDetailsForm(forms.ModelForm):
    class Meta:
        model = FirmDetails
        fields = ['name', 'tagline', 'email', 'phone', 'website', 'address', 'currency_code', 'tax_pin',
                  'physical_address', 'bank', 'bank_account_name', 'bank_account_number', 'bank_branch']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
            'physical_address': forms.Textarea(attrs={'rows': 3})
        }