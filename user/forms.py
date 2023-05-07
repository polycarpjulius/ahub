from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'type': "text",
        "class": "form-control",
        "placeholder": "First name"
    }),max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'type': "text",
        "class": "form-control",
        "placeholder": "Last Name"
    }),max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(
        widget=forms.TextInput(attrs={
        'type': "email",
        "class": "form-control",
        "placeholder": "Email@example.com"
    }),max_length=254, help_text='Required. Inform a valid email address.')
    

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

