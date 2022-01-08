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


# Hoods view
@login_required(login_url='login')
def hoods(request):
    current_user=request.user
    hoods = NeighbourHood.objects.all()
    return render(request,"all-neighbour/hoods.html",{'hoods':hoods,'current_user':current_user})

# Profile view
@login_required(login_url='login')
def profile(request, username):
    current_user=request.user
           
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateUserProfileForm(instance=request.user.profile)

    return render(request, 'all-neighbour/profile.html', {'user_form':user_form,'profile_form':profile_form})

# New hood view
@login_required(login_url='login')
def new_hood(request):
    if request.method == 'POST':
        form = HoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user
            hood.save()
            return HttpResponseRedirect(reverse("hoods"))
    else:
        form = HoodForm()
    return render(request, 'all-neighbour/newhood.html', {'form': form})

# A user hood view
@login_required(login_url='login')
def user_hood(request,id):
    current_user = request.user
    hood = NeighbourHood.objects.get(id=id)
    members = Profile.objects.filter(neighbourhood=hood)
    businesses = Business.objects.filter(neighbourhood=hood)
    posts = Post.objects.filter(neighbourhood=hood)
    request.user.profile.neighbourhood = hood
    request.user.profile.save()
    
    return render(request, 'all-neighbour/user_hood.html', {'hood': hood,'businesses':businesses,'posts':posts,'current_user':current_user, 'members':members})


# Leave hood view
@login_required(login_url='login')
def leave_hood(request,id):
    hood = NeighbourHood.objects.get(id=id)
    request.user.profile.neighbourhood = None
    request.user.profile.save()
    return redirect('hoods')


# Add a business view
@login_required(login_url='login')
def new_business(request,id):
    hood = NeighbourHood.objects.get(id=id)
    title = 'Add here your business'
    if request.method=='POST':
        bus_form = BusinessForm(request.POST,request.FILES)
        if bus_form.is_valid():
            business = bus_form.save(commit=False)
            business.neighbourhood = hood
            business.owner = request.user.profile
            business.save()
            return redirect('my_hood', id)
    else:
        bus_form = BusinessForm()
    return render(request,'all-neighbour/business.html',{'bus_form':bus_form,'title':title})


# Add a post view
@login_required(login_url='login')
def new_post(request,id):
    hood = NeighbourHood.objects.get(id=id)
    title = 'Add here your post'
    if request.method=='POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.neighbourhood = hood
            post.owner = request.user
            post.save()
            return redirect('my_hood', id)
    else:
        post_form = PostForm()
    return render(request,'all-neighbour/post.html',{'post_form':post_form,'title':title})


# Update business view
@login_required(login_url='login')
def update_business(request,id,bus_id):
    instance= Business.objects.get(id=bus_id)
    title = 'Update here yoour business'
    if request.method=='POST':
        bus_form = BusinessForm(request.POST,request.FILES,instance=instance)
        if bus_form.is_valid():
            bus_form.save()
        return redirect('my_hood', id)
    else:
        bus_form = BusinessForm(instance=instance)
    return render(request,'all-neighbour/business.html',{'bus_form':bus_form,'title':title})

# Update post view
@login_required(login_url='login')
def update_post(request,id,post_id):
    title = 'Update here your post'
    instance= Post.objects.get(id=post_id)
    if request.method=='POST':
        post_form = PostForm(request.POST,instance=instance)
        if post_form.is_valid():
           post_form.save()
        return redirect('my_hood', id)
    else:
        post_form = PostForm(instance=instance)
    return render(request,'all-neighbour/post.html',{'post_form':post_form,'title':title})

# Update hood view
@login_required(login_url='login')
def update_hood(request,id):
    title = 'Update here your hood'
    instance= NeighbourHood.objects.get(id=id)
    if request.method=='POST':
        form = HoodForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
           form.save()
        messages.success(request, ('Your hood has been succesfully updated'))
        return redirect('hoods')
    else:
        form = HoodForm(instance=instance)
    return render(request,'all-neighbour/newhood.html',{'form':form,'title':title})
