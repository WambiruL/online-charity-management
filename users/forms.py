from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()
class CustomCreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email']

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'email']
        

