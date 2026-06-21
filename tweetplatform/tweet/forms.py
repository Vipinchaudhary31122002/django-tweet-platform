from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm, User

class TweetForm(forms.ModelForm):
    
    class Meta:
        model = Tweet
        fields = ['text', 'photo']

class UserRegistrationForm(UserCreationForm):
    emai = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')