from . import views
from django.conf.urls import url 
from django.contrib.auth import views as auth_views
from users.views import *

urlpatterns=[
    url(r'register/',views.RegisterView.as_view(),name='register'),
    url(r'login/',auth_views.LoginView.as_view(template_name='registration/login.html'),name='login'),
    url(r'^logout/',auth_views.LogoutView.as_view(),{"next_page": '/lists'}, name='logout'), 
    url(r'^$',views.index,name='index'),
    url(r'create-profile/',views.profile_form,name='create-profile'),
    url(r'profile/',views.profile,name='profile'),
    
]