
from django.shortcuts import render,redirect
from .forms import NewUserForm
from django.views.generic import CreateView
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.

class RegisterView(SuccessMessageMixin,CreateView):
  template_name = "registration/register.html"
  form_class = NewUserForm
  success_url = reverse_lazy("register")
  success_message ="Registro exitoso, por favor inicie sesion!"
