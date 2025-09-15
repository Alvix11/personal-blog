from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from .models import Blog

# Create your views here.
class PostListView(ListView):
    model = Blog
    template_name = 'post_list.html'
    context_object_name = 'posts'