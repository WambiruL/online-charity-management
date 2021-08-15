from django.test import TestCase
from .models import Category, Donor,User,Photo,Admin,NGO,NGOProfile,DonorProfile
import datetime as dt

# Create your tests here

# Test for Category class
class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.category = Category(id=1,name = 'test-category')
        self.category.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))

# Test for User class
class UserTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.user = User(id=1,is_donor='False',is_ngo='True',is_admin='False')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user,User))

# Test for Photo class
class PhotoTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.photo = Photo(image='test/image.jpg')
        self.photo.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.photo,Photo))
# Test for NGOProfile class
class NGOProfileTestClass(TestCase):
    def setUp(self):
        self.user = User(username='test_user')
        self.user.save()
        self.ngoprofile = NGOProfile(user=self.user,username='test_username',bio='test_bio',email='test_email')
        self.ngoprofile.save_profile()

    def tearDown(self):
        User.objects.all().delete()
        Category.objects.all().delete()
        Photo.objects.all().delete()
        NGOProfile.objects.all().delete()
        Donor.objects.all().delete()
        NGO.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.user,User))
        self.assertTrue(isinstance(self.ngoprofile, NGOProfile))

    def test_save_method(self):
        self.ngoprofile.save_profile()
        ngoprofile = NGOProfile.objects.all()
        self.assertTrue(len(ngoprofile) > 0)

# Test for DonorProfile class
class DonorProfileTestClass(TestCase):
    def setUp(self):
        self.user = User(username='test_user')
        self.user.save()
        self.donorprofile = DonorProfile(user=self.user,username='test_username',bio='test_bio',email='test_email')
        self.donorprofile.save_profile()

    def tearDown(self):
        User.objects.all().delete()
        Category.objects.all().delete()
        Photo.objects.all().delete()
        NGOProfile.objects.all().delete()
        Donor.objects.all().delete()
        NGO.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.user,User))
        self.assertTrue(isinstance(self.donorprofile, DonorProfile))

    def test_save_method(self):
        self.donorprofile.save_profile()
        donorprofile = DonorProfile.objects.all()
        self.assertTrue(len(donorprofile) > 0)



class AdminTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.admin = Admin(name='test_name')
        self.admin.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.admin,Admin))


class NGOTestClass(TestCase):
    def setUp(self):
        self.user = User(username='test_user')
        self.user.save()

        self.category = Category(id=1,name = 'test-category')
        self.category.save()

        self.ngo = NGO(NGOProfile(user=self.user),Organisation='test_organisation',categories=self.category,pitch='test_pitch',amount_needed='1000',country='kenya',funded='False',is_approved='False',images='test_image.jpg')
        self.ngo.save_ngo()

    def tearDown(self):
        User.objects.all().delete()
        Category.objects.all().delete()
        Photo.objects.all().delete()
        NGOProfile.objects.all().delete()
        Donor.objects.all().delete()
        NGO.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.user,User))
        self.assertTrue(isinstance(self.ngo, NGO))


class DonorTestClass(TestCase):
    def setUp(self):
        self.user = User(username='test_user')
        self.user.save()

        self.category = Category(id=1,name = 'test-category')
        self.category.save()

        self.donor = Donor(DonorProfile(user=self.user),receipient=NGO(NGOProfile(user=self.user)),donation_amount='1000',description='test_description')
        self.donor.save_donor()

    def tearDown(self):
        User.objects.all().delete()
        Category.objects.all().delete()
        Photo.objects.all().delete()
        NGOProfile.objects.all().delete()
        Donor.objects.all().delete()
        NGO.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.user,User))
        self.assertTrue(isinstance(self.donor, Donor))



       