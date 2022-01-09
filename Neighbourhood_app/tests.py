from django.test import TestCase
from django.test import TestCase
from .models import Post, NeighbourHood,Profile,Business
from django.contrib.auth.models import User
import datetime as dt

# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.Annalis = User(user = "Annalis", email = "annaliskirwa@gmail.com",password = "Ann")
        self.profile = Profile(user= self.Annalis,bio='bio',name='Annalis',profile_pic='mepng', neighbourhood='Pioneer', phone_number='07xxxxxxxx')
        self.profile.save_profile()

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.Annalis, User))
        self.assertTrue(isinstance(self.profile, Profile))

    def test_edit_bio(self):
        self.profile.edit_bio('I am a business owner in the hood')
        self.assertEqual(self.profile.bio, 'I am a business owner in the hood at the far left')

class NeighbourHoodTestClass(TestCase):
    def setUp(self):
        self.Pioneer = NeighbourHood(neighbourhood='Pioneer')

    def test_instance(self):
        self.assertTrue(isinstance(self.Pioneer,NeighbourHood))

    def tearDown(self):
        NeighbourHood.objects.all().delete()

    def test_save_method(self):
        self.Pioneer.save_neighbourhood()
        hood = NeighbourHood.objects.all()
        self.assertTrue(len(hood)>0)

    def test_delete_method(self):
        self.Pioneer.delete_neighbourhood('Pioneer')
        hood = NeighbourHood.objects.all()
        self.assertTrue(len(hood)==0)

class PostTestClass(TestCase):
    def setUp(self):
        self.Vaccinate = Post(vaccinate='Vaccinate')

    def test_instance(self):
        self.assertTrue(isinstance(self.Vaccinate))

    def tearDown(self):
        Post.objects.all().delete()

    def test_save_method(self):
        self.Vaccinate.save_vaccinate()
        rest = Post.objects.all()
        self.assertTrue(len(rest)>0)

    def test_delete_method(self):
        self.Vaccinate.delete_vaccinate('Vaccinate')
        rest = Post.objects.all()
        self.assertTrue(len(rest)==0)

class BusinessTestClass(TestCase):
    def setUp(self):
        self.Pizza = Business(pizza='Pizza')

    def test_instance(self):
        self.assertTrue(isinstance(self.Pizza))

    def tearDown(self):
        Post.objects.all().delete()

    def test_save_method(self):
        self.Pizza.save_pizza()
        rest = Business.objects.all()
        self.assertTrue(len(rest)>0)

    def test_delete_method(self):
        self.Pizza.delete_pizza('Pizza')
        rest = Business.objects.all()
        self.assertTrue(len(rest)==0)

    def test_search_method(self):
        self.Pizza.search_pizza('Pizza')
        rest = Business.objects.all()
        self.assertEqual(name__icontains=Business).all()