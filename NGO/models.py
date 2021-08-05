from django.db import models

from users.models import CustomUser

from django.urls import reverse
from cloudinary.models import CloudinaryField






#Create your models here.
class Category(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name


class NGO(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
	pitch = models.TextField(max_length=5000)
	email = models.EmailField()
	amount_needed = models.IntegerField()
	country = models.CharField(max_length=100)
	past_projects = models.TextField()
	funded = models.BooleanField(default=False, null=True)
	# project_images = models.ImageField(upload_to='images', null=True)
	# project_images = CloudinaryField('image', null=True)


	def __str__(self):
		return self.name

		
	def get_absolute_url(self):
		return reverse('detail', kwargs={'pk': self.pk})
