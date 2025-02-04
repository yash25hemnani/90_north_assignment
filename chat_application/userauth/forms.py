from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauth.models import User

class UserRegisterForm(UserCreationForm):
    usable_password = None # To hide the unecessary field
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Enter Email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Enter Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Enter Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Enter Password'}))

    class Meta:
        model = User
        fields = ['email', 'username']
        # fields = '__all__'
    