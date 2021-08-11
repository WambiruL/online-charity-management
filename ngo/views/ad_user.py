from django.contrib.auth import login
from django.shortcuts import redirect,render
from django.views.generic import CreateView, ListView
from ngo.models import *
from ngo.forms import *
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView
from django.views import generic

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
        return redirect('queries')


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
   

def UpdateRequest(request, pk):
    # dictionary for initial data with
    # field names as keys
    context ={}
    # fetch the object related to passed id
    obj = get_object_or_404(NGO, pk = pk)
    # pass the object as instance in form
    form = AdminUpdateRequestForm(request.POST or None, instance = obj)
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/queries/')
    # add form dictionary to context
    context["form"] = form
    return render(request, "admin/adminupdate.html", context)
    # def user_update(self):
    #     if user.is_ngo():
            
    #         amount_donated_field=HiddenInput(), 
    #         funded_field=HiddenInput()

    #     return 
         

def adminApproved(request):
   # Only fetch the requests that are approved
   queryset = NGO.objects.filter(is_approved=True)
   return render(request, 'admin/approved.html', {'queryset' : queryset})


def adminNotapproved(request):
   # Only fetch the requests that are approved
   queryset = NGO.objects.filter(is_approved=False)
   return render(request, 'admin/notapproved.html', {'queryset' : queryset})


class RequestDetailView(generic.DetailView):
	model = NGO
	template_name = 'admin/admindetails.html'
	fields = '__all__'

	success_url = 'admindetail'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

