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
        fields= ['username','email','password1','password2']
        
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
        fields = ('username', 'email')

# Update user profile form
class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'neighbourhood','profile_pic', 'bio', 'phone_number']
        
        widgets = {
            'bio': Textarea(attrs={'cols': 20, 'rows': 5}),
        }

# Business form
class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('owner', 'neighbourhood')