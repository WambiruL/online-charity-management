from django.shortcuts import render,redirect
from .forms import *
from .decorators import unauthenticated_user,allowed_users,admin_only
from django.contrib.auth.models import Group
# Create your views here.
@unauthenticated_user
def registerPage(request):
    form=CustomCreateUserForm()

    if request.method=='POST':
        form=CustomCreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')

            group=Group.objects.get(name='Donor')
            user.groups.add(group)
            return redirect('login')

    context={'form':form}
    return render(request,'registration/register.html',context)

# @allowed_users(allowed_roles=['admin'])
# @admin_only
def index(request):
    return render(request,'index.html')