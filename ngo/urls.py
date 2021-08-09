from django.urls import path
from . import views
from ngo.views import ad_user, ngo, donor


urlpatterns = [

    ################### NGO ################################################
    path('', ngo.get_ngo_post, name='lists'),
    path('create/', ngo.RequestCreateView.as_view(), name='create-request'),
    path('create-cat', ngo.CategoryCreateView.as_view(), name='create-cat'),
    path('detail/<int:pk>/', ngo.RequestDetailView.as_view(), name='detail'),
    path('update/<int:pk>', ngo.RequestUpdateView.as_view(), name='request-update'),
    path('delete/<int:pk>', ngo.RequestDeleteView.as_view(), name='request-delete'),
    path('ngo-profile/', ngo.ngoProfile, name='ngo-profile'),
    path('search/',ngo.search_results,name='search'),
    
    

    ################### DONOR ################################################
    path('home/',donor.viewNGORequest,name='home'),
    path('donor_create', donor.DonorCreateView.as_view(), name='donor_create'),
    path('donorlist', donor.DonorListView.as_view(), name='donor_list'),
    path('donor_profile/', donor.donorProfile, name='donor-profile'),
    path('donate/', donor.makeDonation, name='donate'),
    path('donations/',donor.donations, name = 'donations'),


    path('admin_profile/', ad_user.adminProfile, name='admin-profile'),
   
    


     

    


]
