from django.contrib.auth import login
from django.shortcuts import redirect,render
from django.views.generic import CreateView, ListView
from ngo.models import *
from ngo.forms import DonorSignUpForm, UserUpdateForm, DonorProfileUpdateForm,AdminSignUpForm, AdminProfileUpdateForm
from django.contrib import messages

class AdminSignUpView(CreateView):
    model = User
    form_class = AdminSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        is_admin=True
        kwargs['user_type'] = 'admin'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('admin-profile')


def adminProfile(request):
    AdminProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = AdminProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.adminprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('queries')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = AdminProfileUpdateForm(instance=request.user.adminprofile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'admin/admin-profile.html', context)

class AdminCreateView(CreateView):
    model = Admin
    template_name = 'admincreate.html'
    fields = '__all__'
    success_url = '/'

def admin_view(request):
   # Only fetch the requests that are approved
   queryset = NGO.objects.all()
   return render(request, 'admin/queries.html', {'queryset' :queryset})