from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import *

from django.forms import ModelForm, fields      
from .models import Photo

class PhotoForm(ModelForm):
  class Meta:
      model = Photo
      fields='__all__'

################## NGO ################################################
class NGOSignUpForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_ngo = True
        user.save()
        return user


class NGOProfileUpdateForm(forms.ModelForm):
    class Meta:
        model= NGOProfile
        fields=['bio']

class NGORequestUpdateForm(forms.ModelForm):
    class Meta:
        model=NGO
        fields='__all__'
        exclude=['funded','is_approved','summary','user']

class NGORequestCreateForm(forms.ModelForm):
    class Meta:
        model=NGO
        fields='__all__'
        exclude=['funded','is_approved','summary','user']


################## ADMIN################################################
class AdminProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=AdminProfile
        fields=['bio']

class AdminSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_admin = True
        if commit:
            user.save()
        return user


class AdminUpdateRequestForm(forms.ModelForm):
    class Meta:
        model=NGO
        fields='__all__'
        exclude=['user','funded','summary','Organisation','categories','pitch','amount_needed','country','funded','date','images']



################## DONOR ################################################
class DonorSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_donor = True
        if commit:
            user.save()
        return user

class DonorProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=DonorProfile
        fields=['bio']

class MakeDonationForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = '__all__'
        exclude=['user','receipient']
       
        

class DonationUpdateForm(forms.ModelForm):
    class Meta:
        model=Donor
        fields='__all__'
        exclude=['user','receipient']


################## FOR ALL ################################################

class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email']

class ContactForm(forms.ModelForm):
    class Meta:
        model=ContactUs
        fields = '__all__'