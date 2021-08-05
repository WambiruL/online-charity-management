from django.db import models
from django.db.models.base import Model
from users.models import *
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
# class Donor(models.Model):
#     roles = models.OneToOneField(User_Roles, on_delete=models.CASCADE)
#     name=models.CharField(max_length=200)
#     donation=models.IntegerField()



    

class Category(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name



class DonationRequest(models.Model):
    ngo_name = models.CharField(max_length=50, default=None)
    project_name = models.CharField(max_length=50, default=None)
    description = models.TextField(default=None)
    amount = models.CharField(max_length=70,default=None,blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.ngo_name

    @classmethod
    def search_by_category(cls, category):
        requests = cls.objects.filter(category__name__contains=category)
        return requests

class Donation(models.Model):
    donor_name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    donation_title = models.CharField(max_length=50, default=None)
    donation_amount = models.CharField(max_length=70, default=None)
    description = models.TextField(default=None)
    donation_time = models.DateTimeField(default=timezone.now())
    def __str__(self):
        return self.donation_title
       
