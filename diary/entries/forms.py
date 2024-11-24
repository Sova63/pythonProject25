from datetime import datetime

from django import forms
from .models import Entry
from django.forms import ModelForm,TextInput,Textarea,DateInput

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['name', 'date', 'text']
        labels = {
            'name': 'Название задачи',
            'date': 'Дата',
            'text': 'Текст сообщения'
        }
        widgets = {
            'name': TextInput(attrs={'class': "form-control", 'placeholder': "Название задачи"}),
            'date': DateInput(attrs={'class': "form-control",'type':"date", 'placeholder': "Дата"}),
            'text': Textarea(attrs={'class': "form-control", 'placeholder': "Текст сообщения"})
        }