from django.shortcuts import render,redirect
from .forms import *
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .decorators import unauthenticated_user,allowed_users,admin_only
from django.contrib.auth.models import Group
# Create your views here.





class RegisterView(CreateView):
    form_class = CustomCreateUserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
