from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.models import User
from django.http  import HttpResponseRedirect,Http404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.forms.models import model_to_dict
from django.contrib import messages
from . forms import UpdateUserForm, UpdateUserProfileForm, UserRegisterForm,HoodForm,BusinessForm,PostForm
from .models import NeighbourHood,Business,Post,Profile


# Create your views here.

def index(request):
    return render(request,'all-neighbour/home.html')