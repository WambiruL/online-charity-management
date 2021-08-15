from django.test import TestCase
from .models import Category,User,Photo,Admin,NGO,NGOProfile
import datetime as dt

# Create your tests here
class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.category = Category(id=1,name = 'test-category')
        self.category.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))


class UserTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.user = User(id=1,is_donor='False',is_ngo='True',is_admin='False')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user,User))

    # def tearDown(self):
    #     User.objects.all().delete()



class PhotoTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.photo = Photo(image='test/image.jpg')
        self.photo.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.photo,Photo))

class NGOProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.user = User(id=1,is_donor='False',is_ngo='True',is_admin='False')
        self.user.save()
        self.ngoprofile = NGOProfile(user=self.user,username='test_username',bio='test_bio',email='test_email')
        self.ngoprofile.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.ngoprofile,NGOProfile))


class AdminTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.admin = Admin(name='test_name')
        self.admin.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.admin,Admin))