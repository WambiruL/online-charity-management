from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.manager import Manager

# Create your models here.
class CustomUser(AbstractUser):
	is_ngo = models.BooleanField(default=True)
	is_donor = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)

	roles = (
        ('1','Admin'), ('2','NGO'),('3','Donor')
    )
	user_roles = models.CharField(choices=roles,max_length=25, default=1)

	def __str__(self):
		return self.user_roles

# class Admin(models.Model):
#     """ role based admin"""
#     roles = models.OneToOneField(User_Roles, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now_add=True)
#     objects = Manager()



    