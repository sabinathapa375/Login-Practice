from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserLogin
 

class RegistrationForm(UserCreationForm):
 
    class Meta:
        model = UserLogin
        fields = ["username", "email", "password1", "password2", "phone"]
