from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django.contrib.auth.forms import (PasswordResetForm, SetPasswordForm)

from django import forms
from django.contrib.auth.forms import PasswordResetForm


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2',]

    widgets = {
        'username': forms.TextInput(attrs={'class':'form-control'

                                        }),
        'password1': forms.TextInput(attrs={'class':'form-control'

                                         }),

        'password2': forms.TextInput(attrs={'class':'form-control'

                                         })
    }




