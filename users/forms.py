from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import *
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

from .forms import *
from django import forms
from django.forms import ModelForm
from .models import *
from users.models import CustomUser

class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()

    class Meta:
        model=CustomUser
        fields=['username','email','user_roles']

class ProfleUpdateForm(forms.ModelForm):

    class Meta:
        model=Profile
        fields=['profile_image','bio']
        

