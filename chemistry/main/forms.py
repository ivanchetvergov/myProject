from django.forms import ModelForm, TextInput, Textarea
from django import forms
from .models import *
from django_summernote.widgets import SummernoteWidget

class MassiveForm(ModelForm):
    class Meta:
        model = Massive
        fields = ['name', 'mean', 'source']
        widgets = {
            'shorts': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите номер задачи"
            }),
            'full': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
            'source': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите номер задачи"
            }),
        }

class Meta:
    model = Massive
    fields = ['mean']
    widgets = {
        'full': SummernoteWidget(attrs={
            'summernote': {
                'airMode': True,
                'width': '270%',
                'height': '300',
                },
            }
        ),
    }
