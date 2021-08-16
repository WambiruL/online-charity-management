from functools import total_ordering
from django.urls import path
from . import views
from ngo.views import ad_user, ngo, donor
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    ################### NGO ################################################
    path('', ngo.get_ngo_post, name='lists'),
    path('single_request/<int:id>', ngo.specific_requests, name='single_request'),
    #path('categories/', ngo.get_objects_per_category, name='categories'),
    path('create/', ngo.RequestCreate, name='create-request'),
    path('create-cat', ngo.CategoryCreateView.as_view(), name='create-cat'),
    path('detail/<int:pk>/', ngo.RequestDetailView.as_view(), name='detail'),
    path('update/<int:pk>', ngo.RequestDetailView.as_view(), name='request-update'),
    path('delete/<int:pk>', ngo.RequestDeleteView.as_view(), name='request-delete'),
    path('ngo-profile/', ngo.ngoProfile, name='ngo-profile'),
    path('search/',ngo.search_results,name='search'),
    path('total_donations/<int:pk>/',ngo.sum_of_donations,name='total_donations'),
    path('homepage/', ngo.homepage, name='homepage'),
    path('upload/',ngo.upload,name='upload'),
    path('contact/', ngo.contact, name='contact'),
    
    

    ################### DONOR ################################################
    path('home/',donor.viewNGORequest,name='home'),

    #path('donor_create', donor.DonorCreateView.as_view(), name='donor_create'),
    path('donorlist/', donor.DonorListView.as_view(), name='donor_list'),

    path('donor_profile/', donor.donorProfile, name='donor-profile'),
    path('donate/<int:pk>/', donor.makeDonation, name='donate'),
    path('donations/',donor.donations, name = 'donations'),
    path('updatedonation/<int:pk>/', donor.UpdateDonation, name='donation-update'),
    #path('categories/', donor.get_objects_per_category, name='categories'),

    ################### ADMIN ################################################
    path('admin_profile/', ad_user.adminProfile, name='admin-profile'),
    path('queries/', ad_user.admin_view, name='queries'),
    path('adminupdate/<int:pk>', ad_user.UpdateRequest, name='adminrequest-update'),
    path('approved/', ad_user.adminApproved, name='approved'),
    path('notapproved/', ad_user.adminNotapproved, name='notapproved'),
    path('admindetail/<int:pk>/', ad_user.RequestDetailView.as_view(), name='admindetail'),
    path('create-cat', ngo.CategoryCreateView.as_view(), name='create-cat'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
