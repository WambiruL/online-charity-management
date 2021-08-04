from django.shortcuts import render
from django.views import generic
from .models import NGO, Category
# Create your views here.


class RequestListView(generic.ListView):
    model = NGO
    template_name = 'ngo/request_list.html'

    def get_context_data(self, **kwargs):
    	context = super().get_context_data(**kwargs)
    	return context


class RequestCreateView(generic.CreateView):
	model = NGO
	template_name = 'ngo/request_create.html'
	fields = '__all__'
	success_url = 'list'



class CategoryCreateView(generic.CreateView):
	model = Category
	template_name = 'ngo/category_create.html'
	fields = '__all__'
	success_url = 'list'

class RequestDetailView(generic.DetailView):
	model = NGO
	template_name = 'ngo/detail_view.html'
	fields = '__all__'
	success_url = 'list'