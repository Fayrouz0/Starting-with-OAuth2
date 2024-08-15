from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # type: ignore
from django.contrib.auth.models import User # type: ignore
from django import forms
from django.forms.widgets import PasswordInput,EmailInput

class CreateUserForm(UserCreationForm):

    class Meta:
        
        model = User
        fields = ['username','email','password1','password2']
        
class LoginForm(AuthenticationForm):
    email=forms.CharField(widget=EmailInput())
    password=forms.CharField(widget=PasswordInput())