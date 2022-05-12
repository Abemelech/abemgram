from dataclasses import field
from enum import unique
from hashlib import blake2b
from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    phone = forms.CharField(max_length=10)

    class Meta: 
        model = User
        fields = ["username", "phone", "password1", "password2"]