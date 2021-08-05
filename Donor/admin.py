from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(DonationRequest)
admin.site.register(Category)
admin.site.register(Donation)