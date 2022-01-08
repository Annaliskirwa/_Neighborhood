from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from django.forms.widgets import EmailInput, Textarea
from . models import NeighbourHood,Post,Business,Profile

# User registration form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields= ['Username','Email','Password1','Password2']
        
User._meta.get_field('email')._unique=True

# Hood registration form
class HoodForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        exclude = ('admin',)


# Update user form
class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address.')

    class Meta:
        model = User
        fields = ('Username', 'Email')

# Update user profile form
class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['Name', 'Neighbourhood','Profile_picture', 'Biography', 'Phone_number']
        
        widgets = {
            'bio': Textarea(attrs={'cols': 20, 'rows': 5}),
        }

# Business form
class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('Business owner', 'Neighbourhood')

# Post form
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['Title', 'Post']