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
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
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
            messages.success(request, f'Your account has been updated!')
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
class RequestCreateView(generic.CreateView):
    model = NGO
    template_name = 'ngo/ngocreate.html'
    fields = '__all__'
    exclude=['user']
    
    def get_success_url(self):
        return reverse('lists')



class CategoryCreateView(generic.CreateView):
	model = Category
	template_name = 'ngo/category_create.html'
	fields = '__all__'
	success_url = 'list'


class RequestDetailView(generic.DetailView):
	model = NGO
	template_name = 'ngo/detail_view.html'
	fields = '__all__'

	success_url = 'detail'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context


def get_ngo_post(request):
   # Only fetch the requests that are approved
   queryset = NGO.objects.filter(is_approved=True)
   return render(request, 'ngo/request_list.html', {'queryset' : queryset})


class RequestUpdateView(generic.UpdateView):
	model = NGO
	template_name = 'ngo/request_update.html'
	fields = '__all__'

	def get_success_url(self):
		return reverse('detail', kwargs={'pk': self.kwargs['pk']})
        
    # def user_update(self):
    #     if user.is_ngo():
            
    #         amount_donated_field=HiddenInput(), 
    #         funded_field=HiddenInput()

    #     return 
         




class RequestDeleteView(generic.DeleteView):
	model = NGO
	template_name='ngo/ngo_confirm_delete.html'
	success_url='/'

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




	    
	






