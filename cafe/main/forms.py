from django import forms
from django.forms import TextInput, Textarea

from .models import Form

person = ['1', '2', '3', '4', '5', '6', '7', '8']
time = ['Завтрак', 'Обед', 'Ужин']


class FormPage(forms.ModelForm):
    class Meta:
        model = Form
        fields = ['name', 'email', 'phone', 'person', 'message']
        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Ваше имя',
                'id': 'name',
                'name': 'name',
                'class': 'contact-form input'
            }),
            'email': TextInput(attrs={
                'placeholder': 'Email',
            }),
            'phone': TextInput(attrs={
                'placeholder': 'Телефон',
            }),
            'person': TextInput(attrs={
                'placeholder': 'Количество гостей',
            }),
            'message': Textarea(attrs={
                'rows': '5',
                'placeholder': 'Сообщение',
            })
        }
