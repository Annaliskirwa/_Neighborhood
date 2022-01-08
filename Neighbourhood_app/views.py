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

# The index view
def index(request):
    return render(request,'all-neighbour/home.html')

# The user registration view
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
            
    else:
        form = UserRegisterForm()
    return render(request,"registration/register.html",{'form':form})