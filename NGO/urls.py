from django.urls import path
from . import views
from users import views as users_views
from NGO import views as NGO_views
from users.views import profile

urlpatterns = [
    #path('',views.get_ngo_post,name='ngo'),
    path('', NGO_views.get_ngo_post, name='lists'),
    path('create/', NGO_views.RequestCreateView.as_view(), name='create-request'),
    #path('request/<int:pk>', views.RequestDetailView.as_view(), name='request-detail'),

    path('create-cat', NGO_views.CategoryCreateView.as_view(), name='create-cat'),
    path('detail/<int:pk>/', NGO_views.RequestDetailView.as_view(), name='detail'),
    path('profile/',users_views.profile,name='profile'),
    path('update/<int:pk>', NGO_views.RequestUpdateView.as_view(), name='request-update'),
    path('delete/<int:pk>', NGO_views.RequestDeleteView.as_view(), name='request-delete'),
    path('filter/',NGO_views.NGO_list,name='filter'),

    


]
