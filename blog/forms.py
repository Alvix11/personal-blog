from django import forms
from .models import Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BlogForm(forms.ModelForm):
    title = forms.CharField(
        max_length=100,
        label='Title',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the blog title...'
        }),
        )
    
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 10,
            'col': 80,
            'class': 'form-control',
            'placeholder': 'Write the blog content...'
        }),
        label='Content'
    )
    
    class Meta:
        model = Blog
        fields = ['title', 'content']

class LoginForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Write your username'
        })
    )
    
    password = forms.CharField(
        widget = forms.PasswordInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Write your password'
            })
    )

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label = 'Username',
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Create your username'
        })
    )
    
    password1 = forms.CharField(
        label = 'Password',
        widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Create your password'
        })
    )
    
    password2 = forms.CharField(
        label = 'Confirm password',
        widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Repeat your password'
        })
    )
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')