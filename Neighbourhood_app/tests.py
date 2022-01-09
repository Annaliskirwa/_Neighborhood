from django.test import TestCase
from django.test import TestCase
from .models import Post, NeighbourHood,Profile,Business
from django.contrib.auth.models import User
import datetime as dt

# Create your tests here.
class neighbourhoodTestClass(TestCase):
    def setUp(self):
        self.Pioneer = NeighbourHood(neighbourhood='Pioneer')

    def test_instance(self):
        self.assertTrue(isinstance(self.Kahawa,NeighbourHood))

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