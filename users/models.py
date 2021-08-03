from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.manager import Manager

# Create your models here.
# class User_Roles(AbstractUser):
#     roles = (
#         ('1','Admin'), ('2','NGO'),('3','Donor')
#     )
#     user_roles = models.CharField(choices=roles,max_length=25, default=1)

#     def __str__(self):
#         full_name = self.first_name + " " + self.last_name
#         return self.full_name

# class Admin(models.Model):
#     """ role based admin"""
#     roles = models.OneToOneField(User_Roles, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now_add=True)
#     objects = Manager()



    