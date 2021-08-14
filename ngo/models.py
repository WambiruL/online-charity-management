import cloudinary
from django.db import models
from django.urls import reverse
from django.dispatch import receiver 
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField

#Create your models here.
from django.db import models
from cloudinary.models import CloudinaryField
class Photo(models.Model):
  image = CloudinaryField('image')
################### FOR ALL ################################################
class User(AbstractUser):
    is_donor = models.BooleanField(default=False)
    is_ngo = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return self.name


################### NGO ################################################
class NGOProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    username=models.CharField(max_length=200,null=True)
    #profile_image=models.ImageField(upload_to='Profilepics/')
    bio=models.CharField(max_length=1000,null=True, default="My Bio")
    email=models.EmailField(max_length=200,null=True)

    def __str__(self):
        return self.user.username
	
	
    @receiver(post_save, sender=User) #add this
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            NGOProfile.objects.get_or_create(user=instance)

    @receiver(post_save, sender=User) #add this
    def save_user_profile(sender, instance, **kwargs):
        instance.ngoprofile.save()

class NGO(models.Model):
    user = models.ForeignKey(NGOProfile, on_delete=models.CASCADE, null=True)
    Organisation = models.CharField(max_length=200)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    pitch = models.TextField(max_length=5000)
    amount_needed = models.IntegerField()
    country = models.CharField(max_length=100)
    funded = models.BooleanField(default=False, null=True)
    is_approved = models.BooleanField(default=False, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    images = cloudinary.models.CloudinaryField('image',null=True, blank=True)

    class Meta:
        ordering = ['-date',]

    def __str__(self):
        return self.Organisation

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    @classmethod
    def search_by_name(cls,search_term):
	    categorys = cls.objects.filter(categorys__name__icontains=search_term).all()
	    return categorys


    


	

########################### Donor ####################################################    

class DonorProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    username=models.CharField(max_length=200,null=True)
    #profile_image=models.ImageField( upload_to='Profilepics/')
    bio=models.CharField(max_length=1000,null=True, default="My Bio")
    email=models.EmailField(max_length=200,null=True)
    
    def __str__(self):
        return self.user.username

    

    @receiver(post_save, sender=User) #add this
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            DonorProfile.objects.get_or_create(user=instance)

    @receiver(post_save, sender=User) #add this
    def save_user_profile(sender, instance, **kwargs):
        instance.donorprofile.save()

# class Donor(models.Model):
# 	name = models.CharField(max_length=100, null=True)
# 	amount = models.IntegerField()


class Donor(models.Model):
    user = models.ForeignKey(DonorProfile, on_delete=models.CASCADE,null=True)
    receipient=models.ForeignKey(NGO, related_name='Donor', on_delete=models.CASCADE,null=True)
    donation_amount = models.IntegerField(max_length=70, default=0)
    description = models.TextField(default=None)
    donation_time = models.DateTimeField(auto_now_add=True)
	
	
    def __str__(self):
	    return str(self.user)

    class Meta:
        ordering = ['-donation_time',]

# class Donation(models.Model):
#     donor = models.ForeignKey(DonorProfile, on_delete=models.CASCADE)
#     amount_donated = models.IntegerField()
#     ngo = models.ForeignKey(NGO, on_delete=models.CASCADE)
    
    # def amount_remaining(self):
    #     balance = NGO.amount_needed - Donation.amount_donated
    #     return balance

    # def amount_remaining(self, *args, **kwargs):
    #     amount_needed = self.ngo.amount_needed
    #     donation= Donation.objects.filter(ngo=self.ngo)
    #     balance =amount_needed-donation
    #     super(Donation, self).save(*args, **kwargs)
            


######################################### Admin #############################################


class AdminProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    username=models.CharField(max_length=200,null=True)
    #profile_image=models.ImageField(upload_to='Profilepics/')
    bio=models.CharField(max_length=1000,null=True, default="My Bio")
    email=models.EmailField(max_length=200,null=True)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User) #add this
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            AdminProfile.objects.get_or_create(user=instance)

    @receiver(post_save, sender=User) #add this
    def save_user_profile(sender, instance, **kwargs):
        instance.adminprofile.save()


class Admin(models.Model):
    name = models.CharField(max_length=100, null=True)


	

	


	