from django.contrib import admin
from ngo.models import *
from django.contrib.auth.admin import UserAdmin


# Register your models here.
admin.site.register(Category)
admin.site.register(User, UserAdmin)
admin.site.register(NGO)
admin.site.register(Donor)
admin.site.register(NGOProfile)
admin.site.register(AdminProfile)
admin.site.register(Admin)
admin.site.register(DonorProfile)

