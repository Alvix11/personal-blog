from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import Blog
from .forms import BlogForm, LoginForm

# Create your views here.
class PostListView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = 'post_list.html'
    context_object_name = 'posts'
    
class PostDetailView(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = 'post_detail.html'
    context_object_name = 'post'
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'post_create.html'
    success_url = reverse_lazy('list')
    
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'post_update.html'
    
    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.object.pk})
    
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('list')
    
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('list')
            else:
                form.add_error(None, 'Username or password incorrect')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return render(request, 'logout_confirm.html')