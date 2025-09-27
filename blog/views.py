from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Blog
from .forms import BlogForm, LoginForm, SignUpForm

# Create your views here.
class OnlyAdminMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_staff
    
    def handle_no_permission(self):
        return redirect('login')

class PostListView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = 'post_list.html'
    context_object_name = 'posts'
    
class PostDetailView(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = 'post_detail.html'
    context_object_name = 'post'
    
class PostCreateView(OnlyAdminMixin, CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'post_create.html'
    success_url = reverse_lazy('list')
    
class PostUpdateView(OnlyAdminMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'post_update.html'
    
    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.object.pk})
    
class PostDeleteView(OnlyAdminMixin, DeleteView):
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

@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return render(request, 'logout_confirm.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
        
    return render(request, 'signup.html', {'form':form})