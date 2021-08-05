from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.manager import Manager
from django.dispatch import receiver 
from django.db.models.signals import post_save

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

class Profile(models.Model):
	user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
	username=models.CharField(max_length=200,null=True)
	profile_image=models.ImageField(default='default.jpeg', upload_to='Profilepics/')
	bio=models.CharField(max_length=1000,null=True, default="My Bio")
	email=models.EmailField(max_length=200,null=True)

	def __str__(self):
		return self.user.username

	@receiver(post_save, sender=CustomUser) #add this
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.get_or_create(user=instance)

	@receiver(post_save, sender=CustomUser) #add this
	def save_user_profile(sender, instance, **kwargs):
		instance.profile.save()
    



    
