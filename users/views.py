from Donor.models import Donation
from django.shortcuts import render,redirect
from .forms import *
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .decorators import unauthenticated_user,allowed_users,admin_only
from django.contrib.auth.models import Group
from django.core.exceptions import ObjectDoesNotExist 
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

class RegisterView(CreateView):
    form_class = CustomCreateUserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

def index(request):
    return render(request,'index.html')

def ngo(request):
	current_user=request.user
	if not request.user.is_authenticated:
			return redirect('/accounts/login/')
	try:
		profile =Profile.objects.get(username=current_user)

	except ObjectDoesNotExist:
		return redirect('create-profile')

	return render(request,'ngo/request_list.html')
@login_required
def profile_form(request):
    Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfleUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('/profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfleUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'profile_form.html', context)

def profile(request):
   profile = Profile.objects.get_or_create(user=request.user)
   donations = Donation.objects.filter(donor_name=request.user.id).all()
   context = {'donations':donations,'profile':profile}
   return render(request,'profile.html', context)


	

