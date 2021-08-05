from django.urls import path
from . import views
from users import views as users_views
from NGO import views as NGO_views
from users.views import profile

urlpatterns = [
    path('',views.ngo,name='ngo'),
    path('list/', NGO_views.RequestListView.as_view(), name='lists'),
    path('create/', NGO_views.RequestCreateView.as_view(), name='create-request'),
    #path('request/<int:pk>', views.RequestDetailView.as_view(), name='request-detail'),


    path('create-cat', NGO_views.CategoryCreateView.as_view(), name='create-cat'),
    path('detail/<int:pk>/', NGO_views.RequestDetailView.as_view(), name='detail'),
    path('profile/',users_views.profile,name='profile') 
    


]
