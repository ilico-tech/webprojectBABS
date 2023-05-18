
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout,update_session_auth_hash
from django.shortcuts import render, redirect,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm,SetPasswordForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.urls import reverse



from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

User = get_user_model()


def Inscription(request):

        form=UserCreationForm()
        if request.method == "POST":
           form=UserCreationForm(request.POST)
           if form.is_valid():
               messages.success(request, 'compte cree avec succes')
               form.save()
               user=form.cleaned_data.get('username')

           return redirect('seconnecter')
        context={'form':form}
        return render(request,'voitures/inscrire.html',context)

def Seconnecter(request):
         if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:

                login(request, user)
                messages.info(request, 'connexion validee')
                return redirect('voiture')
            else:
                messages.info(request,'l identifiant ou le mot de passe n est pas valide')
         return render(request,'voitures/seconnecter.html')

#profile

def user_profile(request):


 if request.user.is_authenticated:

   return render(request,'voitures/monprofil.html',{'name':request.user})
 else:
   return redirect('seconnecter')



def Sedeconnecter(request):
    logout(request)
    return redirect('seconnecter')




