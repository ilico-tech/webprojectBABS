
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path
from django.contrib.auth import views
from . import views
from django.contrib.auth.views import (
    LogoutView,
    PasswordResetView, PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView



)

urlpatterns = [
    path('inscription',views.Inscription,name='inscription'),
    path('seconnecter', views.Seconnecter, name='seconnecter'),
    path('sedeconnecter', views.Sedeconnecter, name='sedeconnecter'),
    path('profile', views.user_profile, name='profile'),

    path('reset_password',PasswordResetView.as_view(template_name='voitures/password_reset.html'),name='password_reset'),
    path('reset_password_send',PasswordResetDoneView.as_view(template_name='voitures/password_reset_sent.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='voitures/password_reset_form.html'),name='password_reset_confirm'),
    path('reset_password_complete/',PasswordResetCompleteView.as_view(template_name='voitures/password_reset_done.html'),name='password_reset_complete'),





]








