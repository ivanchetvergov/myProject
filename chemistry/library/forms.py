from django.forms import ModelForm, TextInput, Textarea
from django import forms
from .models import *
from django_summernote.widgets import SummernoteWidget

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['shorts', 'full', 'answer', 'decision', 'key']
        widgets = {
            'shorts': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите номер задачи"
            }),
            'full': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
            'answer': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите номер задачи"
            }),
            'decision': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите решение'
            }),
            'key': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ключ задания'
            }),
        }

class Meta:
    model = Articles
    fields = ['shorts', 'full', 'answer', 'key', 'decision']
    widgets = {
        'decision': SummernoteWidget(),
        'full': SummernoteWidget(),
    }





class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body']
        widgets = {
            'shorts': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите номер задачи"
            }),
            'full': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
        }

class Meta:
    model = Blog
    fields = ['body']
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
