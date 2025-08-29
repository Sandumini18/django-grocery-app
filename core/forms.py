from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={'class':'w-full h-8 p-4'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'w-full h-8 p-4'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'w-full h-8 p-4'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'w-full h-8 p-4'}))

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'w-full h-8 p-4'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'w-full h-8 p-4'}))