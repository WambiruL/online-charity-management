from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import NGO, Category,NGOProfile
from django.contrib.auth.models import User

# Create your tests here.


class CategoryTest(TestCase):

    def setUp(self):
        self.name = Category(name='food')

    def test_instance(self):
        self.assertTrue(isinstance(self.name,Category))

    def test_save(self):
        self.name.save()
        categorys = Category.objects.all()
        self.assertTrue(len(categorys) > 0)

    def test_delete_category(self):
        self.name.save()
        self.name.delete()
        categorys = Category.objects.all()
        self.assertTrue(len(categorys) == 0)

class NGOTest(TestCase):

    def setUp(self):
        self.Organisation = NGO(Organisation='Health')

    def test_instance(self):
        self.assertTrue(isinstance(self.Organisation,NGO))


class NGOProfileTestClass(TestCase):
    def setUp(self):
        self.user = NGOProfile(user= 'James', username = 'Muriuki', email='james@moringaschool.com',bio="true")
    
    #testing instance

    def test_instance(self):
        self.assertTrue(isinstance(self.user,NGOProfile))
    
    #Testing save method
    def test_save_method(self):
        self.james.save_ngo()
        ngos = NGOProfile.objects.all()
        self.assertTrue(len(ngos) > 0)

    def test_delete(self):
        self.james.save_editor()
        self.james.delete_editor()
        editors =NGOProfile.objects.all()
        self.assertTrue(len(editors) == 0)
