from django.forms import ModelForm
from .models import Order
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class meta:
        model= User
        feilds= ['username','Email address','password1','password2']

