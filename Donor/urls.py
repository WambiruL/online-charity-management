from Donor.models import Donation
from django.conf.urls import url
from . import views
from users import views as users_views
from NGO import views as NGO_views


urlpatterns=[
    url(r'home/',NGO_views.get_ngo_post,name='home'),
   # url(r'requestslist/',views.viewDonationRequest,name='donation-request'),
    #url(r'request/(?P<pk>\d+)/$', views.singleDonationRequest, name='request'),
    url(r'donate/', views.makeDonation, name='donate'),
    url(r'donations/',views.donations, name = 'donations'),
    #url(r'profile/',users_views.profile,name='profile'),
]