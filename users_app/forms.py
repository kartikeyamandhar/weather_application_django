from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#this form is overriding the custom form from 'UserCreationForm' class provided by django to include email input
#and hence forming our own form class CustomForm as the former does not have email input.

class CustomForm(UserCreationForm):
    email = forms.EmailField(required=False)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
