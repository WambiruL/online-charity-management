from django.db import models
from django.db.models.base import Model
from users.models import *
from django.contrib.auth.models import User
from django.utils import timezone
from users.models import Profile
# Create your models here.
# class Donor(models.Model):
#     roles = models.OneToOneField(User_Roles, on_delete=models.CASCADE)
#     name=models.CharField(max_length=200)
#     donation=models.IntegerField()



    

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name



# class DonationRequest(models.Model):
#     ngo_name = models.CharField(max_length=50, default=None)
#     project_name = models.CharField(max_length=50, default=None)
#     description = models.TextField(default=None)
#     amount = models.CharField(max_length=70,default=None,blank=False)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.ngo_name

#     @classmethod
#     def search_by_category(cls, category):
#         requests = cls.objects.filter(category__name__contains=category)
#         return requests

class Donation(models.Model):
    id = models.AutoField(primary_key=True)
    donor_name = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    donation_title = models.CharField(max_length=50, default=None)
    donation_amount = models.CharField(max_length=70, default=None)
    description = models.TextField(default=None)
    donation_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.donation_title
       
