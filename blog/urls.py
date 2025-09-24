from django.urls import path
from .views import PostListView, PostCreateView, PostDetailView, PostUpdateView

urlpatterns = [
    path('list/', PostListView.as_view(), name='list'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', PostUpdateView.as_view(), name='update')
]
