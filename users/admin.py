from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomCreateUserForm, CustomUserChangeForm
from .models import CustomUser
# Register your models here.
class CustomUserAdmin(UserAdmin):
	add_form = CustomCreateUserForm
	form = CustomUserChangeForm
	model = CustomUser
	list_display = ['email','username']

admin.site.register(CustomUser, CustomUserAdmin)
