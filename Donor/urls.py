from Donor.models import Donation
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'home/',views.home,name='home'),
    url(r'requestslist/',views.viewDonationRequest,name='donation-request'),
    url(r'request/(?P<pk>\d+)/$', views.singleDonationRequest, name='request'),
    url(r'donate/', views.makeDonation, name='donate'),
    url(r'donations/',views.donations, name = 'donations'),
]