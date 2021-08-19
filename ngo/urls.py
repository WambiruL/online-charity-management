from functools import total_ordering
from django.urls import path
from . import views
from ngo.views import ad_user, ngo, donor
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    ################### NGO ################################################
    path('lists/', ngo.get_ngo_post, name='lists'),
    path('single_request/<int:id>', ngo.specific_requests, name='single_request'),
    #path('categories/', ngo.get_objects_per_category, name='categories'),
    path('ngo/create/', ngo.RequestCreate, name='create-request'),
    path('ngo/create-cat', ngo.CategoryCreateView.as_view(), name='create-cat'),
    path('ngo/detail/<int:pk>/', ngo.RequestDetailView.as_view(), name='detail'),
    path('ngo/update/<int:pk>', ngo.UpdateRequest, name='request-update'),
    path('ngo/delete/<int:pk>', ngo.RequestDeleteView.as_view(), name='request-delete'),
    path('ngo/ngo-profile/', ngo.ngoProfile, name='ngo-profile'),
    path('ngo/search/',ngo.search_results,name='search'),
    path('ngo/total_donations/<int:pk>/',ngo.sum_of_donations,name='total_donations'),
    path('homepage/', ngo.homepage, name='homepage'),
    path('ngo/upload/',ngo.upload,name='upload'),
    path('ngo/contact/', ngo.contact, name='contact'),
    path('ngo/create-cat', ngo.CategoryCreateView.as_view(), name='create-cat'),
    
    

    ################### DONOR ################################################
    path('donor/home/',donor.viewNGORequest,name='home'),

    #path('donor_create', donor.DonorCreateView.as_view(), name='donor_create'),
    path('donor/donorlist/', donor.DonorListView.as_view(), name='donor_list'),

    path('donor/donor_profile/', donor.donorProfile, name='donor-profile'),
    path('donor/donate/<int:pk>/', donor.makeDonation, name='donate'),
    path('donor/donations/',donor.donations, name = 'donations'),
    path('donor/updatedonation/<int:pk>/', donor.UpdateDonation, name='donation-update'),
    #path('categories/', donor.get_objects_per_category, name='categories'),

    ################### ADMIN ################################################
    path('admin_profile/', ad_user.adminProfile, name='admin-profile'),
    path('queries/', ad_user.admin_view, name='queries'),
    path('adminupdate/<int:pk>', ad_user.UpdateRequest, name='adminrequest-update'),
    path('approved/', ad_user.adminApproved, name='approved'),
    path('notapproved/', ad_user.adminNotapproved, name='notapproved'),
    path('admindetail/<int:pk>/', ad_user.RequestDetailView.as_view(), name='admindetail'),
   

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
