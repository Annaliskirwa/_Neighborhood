from django.test import TestCase
from django.test import TestCase
from .models import Post, NeighbourHood,Profile,Business
from django.contrib.auth.models import User
import datetime as dt

# Create your tests here.
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