from django.contrib import admin
from django.urls import path, include
from blog.views import login_view, logout_view, signup_view, home

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('blog.urls')),
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup')
]
