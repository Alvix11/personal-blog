from django.contrib import admin
from django.urls import path, include
from blog.views import login_view

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('blog.urls')),
    path('login/', login_view, name='login')
]
