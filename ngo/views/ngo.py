from django.forms.widgets import HiddenInput
from django.shortcuts import render,redirect
from django.contrib.auth import login
from ngo.decorators import unauthenticated_user
from django.contrib import messages
from django.http import request
from django.views import generic
from django.core.exceptions import ObjectDoesNotExist 
from ngo.models import *
from ngo.forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView,ListView
from django.http import HttpResponseRedirect
from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.http import HttpResponse

from cloudinary.forms import cl_init_js_callbacks 
# Create your views here.


class NGOSignUpView(CreateView):
    model = User
    form_class = NGOSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        is_ngo = True
        kwargs['user_type'] = 'ngo'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('ngo-profile')


# class NGOListView(ListView):
#     model = NGO
#     template_name = 'ngolist.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
  
#         return context


# class NGOCreateView(CreateView):
#     model = NGO
#     template_name = 'ngocreate.html'
#     fields = '__all__'
#     success_url = '/'

@login_required(login_url='accounts/login')
def ngoProfile(request):
    NGOProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = NGOProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.ngoprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your NGO account has been updated!')
            return redirect('lists')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = NGOProfileUpdateForm(instance=request.user.ngoprofile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'ngo/ngo-profile.html', context)


# Create your views here.
# class RequestCreateView(generic.CreateView):
#     model = NGO
#     template_name = 'ngo/ngocreate.html'
#     form_class=NGORequestCreateForm
    
#     def get_success_url(self):
#         return reverse('lists')

@login_required(login_url='accounts/login')
def RequestCreate(request):
    user=request.user
    ngo=NGOProfile.objects.get(user=user)
    print(ngo)
    if request.method == 'POST':
        form = NGORequestCreateForm(request.POST,request.FILES)
        if form.is_valid():
            requests=form.save(commit=False)
            requests.user=ngo
            form.save()
            messages.success(request, f'Your request has been received. Waiting for the Admin to approve!')
            return redirect('lists')
    else:
        form = NGORequestCreateForm()

    return render(request,'ngo/ngocreate.html', {'form':form,'messages':messages})

class CategoryCreateView(generic.CreateView):
	model = Category
	template_name = 'ngo/category_create.html'
	fields = '__all__'
	success_url = 'create'


class RequestDetailView(LoginRequiredMixin,generic.DetailView):
	model = NGO
	template_name = 'ngo/detail_view.html'
	fields = '__all__'

	success_url = 'detail'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context



# def get_ngo_post(request):
#    # Only fetch the requests that are approved
#    queryset = NGO.objects.filter(is_approved=True)
#    return render(request, 'ngo/request_list.html', {'queryset' : queryset})



@login_required(login_url='accounts/login')
def get_ngo_post(request):
   user=request.user
   ngo=NGOProfile.objects.get(user=user)
   print(ngo)
   # Only fetch the requests that are approved
   queryset = NGO.objects.filter(is_approved=True,user=ngo.user.ngoprofile)
   print(queryset)
   return render(request, 'ngo/request_list.html', {'queryset' : queryset})


def sum_of_donations(request,pk):  
    """
    find sum of donations
    """
    donations=Donor.objects.filter(receipient=pk) 
    ngo = NGO.objects.get(pk=pk)
    print(ngo.pk)
    obj = Donor.objects.filter(receipient=ngo).aggregate(Sum('donation_amount'))
    #print('obj',obj)
    print(obj)
    #sum_total = Donation.objects.aggregate(Sum('donated_amount'))
    #sum_total = Donation.objects.filter().aggregate(Sum('donated_amount'))
    #print(sum_total)
    balances = ngo.amount_needed - obj['donation_amount__sum']
    print(balances)
    ctx={
        'donations':donations,
        'obj':obj,
        'balances':balances,
        'ngo':ngo,
        
    }
    return render(request,'ngo/total_donations.html',ctx)


def get_objects_per_category(request, **kwargs):
    categories = Category.objects.all()
    return render(request,'ngo/allcategories.html',{'categories':categories})

def specific_requests(request,id):
    category=Category.objects.get(id=id)
    requests=NGO.objects.filter(is_approved=True,categories=category)
    return render(request,'ngo/single_request.html',{'requests':requests,'category':category})

def UpdateRequest(request, pk):
    # dictionary for initial data with
    # field names as keys
    context ={}
    # fetch the object related to passed id
    obj = get_object_or_404(NGO, pk = pk)
    # pass the object as instance in form
    form = NGORequestUpdateForm(request.POST or None, instance = obj)
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        messages.success(request, f'You have updated your request')
        return HttpResponseRedirect('/lists')
    # add form dictionary to context
    context["form"] = form
    return render(request, "ngo/request_update.html", context)
    # def user_update(self):
    #     if user.is_ngo():
            
    #         amount_donated_field=HiddenInput(), 
    #         funded_field=HiddenInput()

    #     return 
         




class RequestDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = NGO
    template_name='ngo/ngo_confirm_delete.html'
    success_url='/lists'

       

	# def get_success_url(self):
	# 	return reverse('detail', kwargs={'pk': self.kwargs['pk']})


def search_results(request):
    if 'name' in request.GET and request.GET["name"]:
        search_term = request.GET.get("name")
        searched_categorys = NGO.search_by_name(search_term)
        message = f"{search_term}"
        return render (request, 'search.html',{"message":message,"categorys": searched_categorys})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


def deleteView(request,pk):
    ctx={}
    object=get_object_or_404(NGO,pk=pk)
    if request.method=='POST':
        object.delete()

        return HttpResponseRedirect('/lists/') 

    return render(request,'ngo/ngo_confirm_delete.html',ctx)

def donationsMade(request,pk):
    donations= Donor.objects.get(pk=pk)
    context = {
    'donations':donations
    }
    return render(request, 'ngo/total_donations.html', context)

def homepage(request):
    queryset = NGO.objects.filter(is_approved=True).order_by('-date')[0:3]
    donations = Donor.objects.all().order_by('-donation_time')[0:5]
    context = {'queryset' : queryset, 'donations': donations}
    return render(request, 'homepage.html', context)
	

     


def upload(request):
  context = dict( backend_form = PhotoForm())

  if request.method == 'POST':
    form = PhotoForm(request.POST, request.FILES)
    context['posted'] = form.instance
    if form.is_valid():
        form.save()

  return render(request, 'ngo/upload.html', context)
	






