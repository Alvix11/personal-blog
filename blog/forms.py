from django import forms
from .models import Blog

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