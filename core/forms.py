from django import forms
from .models import *


class BiodataForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'type': "text",
        "class": "form-control",
        "placeholder": "First Name"
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'type': "text",
        "class": "form-control",
        "placeholder": "Last Name"
    }))
    
    email = forms.CharField(widget=forms.TextInput(attrs={
        'type': "email",
        "class": "form-control",
        "placeholder": "Email@example.com"
    }))

    class Meta:
        model = Biodata
        fields = [
        
            'first_name', 'last_name','email'
        ]
