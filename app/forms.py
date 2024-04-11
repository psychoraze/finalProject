from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Team_Form(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'city', 'rating']

class Racer_Form(forms.ModelForm):
    class Meta:
        model = Racer
        fields = ['first_name', 'last_name', 'age', 'reaction', 'strategic_thinking', 'mental_toughness', 'g_force_withstanding', 'car_understanding', 'team']

class Admin_Form(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ['name', 'team']

class Bolide_Form(forms.ModelForm):
    class Meta:
        model = Bolide
        fields = ['name', 'racer', 'team']

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }