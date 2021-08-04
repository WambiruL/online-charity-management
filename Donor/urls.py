from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'home/',views.home,name='home'),


    url(r'requestslist/',views.viewDonationRequest,name='donation-request'),
    url(r'requestslistform/',views.createDonationRequest,name='donation-requestform'),
]