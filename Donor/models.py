from django.db import models
from django.db.models.base import Model
from users.models import *

# Create your models here.
# class Donor(models.Model):
#     roles = models.OneToOneField(User_Roles, on_delete=models.CASCADE)
#     name=models.CharField(max_length=200)
#     donation=models.IntegerField()
class DonationRequest(models.Model):
    ngo_name = models.CharField(max_length=50, default=None)
    project_name = models.CharField(max_length=50, default=None)
    description = models.TextField(default=None)
    amount = models.CharField(max_length=70,default=None,blank=False)

    def __str__(self):
        return self.ngo_name