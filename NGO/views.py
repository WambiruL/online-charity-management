
from django.http import request
from django.shortcuts import render,redirect
from django.views import generic
from .models import NGO, Category
from django.core.exceptions import ObjectDoesNotExist 
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.models import *
from .filters import *

from django.shortcuts import get_object_or_404


from django.views.generic.detail import DetailView

# Create your views here.


# class RequestListView(generic.ListView):
#     model = NGO
#     template_name = 'ngo/request_list.html'

#     def get_context_data(self, **kwargs):
#     	context = super().get_context_data(**kwargs)
#     	return context


class RequestCreateView(generic.CreateView):
	model = NGO
	template_name = 'ngo/request_create.html'
	fields = '__all__'

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

	

# def ngo(request):
# 	return render(request,'ngo/request_list.html')

# def profile(request):
#     current_user=request.user
#     profile =Profile.objects.get(username=current_user)

#     return render(request,'profile.html', {'profile':profile})

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

class RequestDeleteView(generic.DeleteView):
	model = NGO
	template_name='ngo/ngo_confirm_delete.html'
	success_url='/'

	# def get_success_url(self):
	# 	return reverse('detail', kwargs={'pk': self.kwargs['pk']})

def NGO_list(request):
    f = NGOFilter(request.GET, queryset=NGO.objects.all())
    return render(request, 'ngo/filter.html', {'filter': f})

	    
	

