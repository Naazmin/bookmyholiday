from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class packageForm(ModelForm):
	class Meta:
		model=package
		fields='__all__'
		
class vehicleForm(ModelForm):
	class Meta:
		model=vehicle
		fields="__all__"
class hotelForm(ModelForm):
	class Meta:
		model=hotels
		fields="__all__"	
class bookingsForm(ModelForm):
	class Meta:
		model=mybookings
		fields="__all__"			
class CreateUserForm(UserCreationForm):
	class Meta:
		model=User
		fields=['username','email','password1','password2']


	
	
		