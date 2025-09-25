from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from .models import Blog
from .forms import BlogForm

# Create your views here.
class PostListView(ListView):
    model = Blog
    template_name = 'post_list.html'
    context_object_name = 'posts'
    
class PostDetailView(DetailView):
    model = Blog
    template_name = 'post_detail.html'
    context_object_name = 'post'
    
class PostCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'post_create.html'
    success_url = reverse_lazy('list')
    
class PostUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'post_update.html'
    
    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.object.pk})
    
class PostDeleteView(DeleteView):
    model = Blog
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('list')