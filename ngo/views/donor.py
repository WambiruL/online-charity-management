from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView
from ngo.models import *
from ngo.forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import ngo
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

# Create your views here.

class DonorSignUpView(CreateView):
    model =User
    form_class = DonorSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        is_donor=True
        kwargs['user_type'] = 'donor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('donor-profile')


class DonorCreateView(CreateView):
    model = Donor
    template_name = 'donor/donorcreate.html'
    fields = '__all__'
    success_url = '/'


class DonorListView(ListView):
    model = Donor
    template_name = 'donor/donorlist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



def donorProfile(request):
    DonorProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = DonorProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.donorprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('lists')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = DonorProfileUpdateForm(instance=request.user.donorprofile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'donor/donor-profile.html', context)

def viewNGORequest(request):
    requests = NGO.objects.filter(is_approved=True)
    context={'requests':requests}
    return render(request,'donor/donorhomepage.html',context)

def singleDonationRequest(request, pk):
    requests = NGO.objects.get(pk=pk)
    return render(request, 'donor/singleDonation.html',{'requests':requests})


def makeDonation(request):
    if request.method == 'POST':
        form = MakeDonationForm(request.POST)
        if form.is_valid():
            #form.user=onor
            #form.receipient=request.user        
            form.save()
            return redirect('donations')
    else:
        form = MakeDonationForm()

    return render(request,'donor/makedonation.html', {'form':form})

def donations(request):
    DonorProfile.objects.get_or_create(user=request.user)
    donations = Donor.objects.filter(user=request.user.donorprofile)
    context = {'donations':donations}
    return render(request,'donor/donations.html',context)


def search_results(request):
    if 'name' in request.GET and request.GET["name"]:
        search_term = request.GET.get("name")
        searched_categorys = NGO.search_by_name(search_term)
        message = f"{search_term}"
        return render (request, 'search.html',{"message":message,"categorys": searched_categorys})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

# def donationStatus(request,pk):
#     donation=Donation.objects.get(pk=pk)

def UpdateDonation(request, pk):
    # dictionary for initial data with
    # field names as keys
    context ={}
    # fetch the object related to passed id
    obj = get_object_or_404(Donor, pk = pk)
    # pass the object as instance in form
    form = DonationUpdateForm(request.POST or None, instance = obj)
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/donations/')
    # add form dictionary to context
    context["form"] = form
    return render(request, "donor/donation_update.html", context)

