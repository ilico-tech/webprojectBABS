from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django.contrib.auth.forms import (PasswordResetForm, SetPasswordForm)

from django import forms
from django.contrib.auth.forms import PasswordResetForm


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2',]




