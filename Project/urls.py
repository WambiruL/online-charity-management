"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django_registration.backends.one_step.views import RegistrationView
from ngo.views import choice, ngo, donor, ad_user
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ngo.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', choice.SignUpView.as_view(), name='signup'),
    path('accounts/signup/ngo/', ngo.NGOSignUpView.as_view(), name='ngo_signup'),
    path('accounts/signup/donor/', donor.DonorSignUpView.as_view(), name='donor_signup'),
    path('accounts/signup/admin/', ad_user.AdminSignUpView.as_view(), name='admin_signup'),
    path('logout/',auth_views.LogoutView.as_view(),{"next_page": '/lists'}, name='logout'), 
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
