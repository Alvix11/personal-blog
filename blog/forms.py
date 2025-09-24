from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    title = forms.CharField(max_length=100, label='Title', required=True)
    
    publish_date = forms.DateTimeField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Publish Date'
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
        fields = ['title', 'publish_date', 'content']