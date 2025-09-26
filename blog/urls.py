from django.urls import path
from .views import PostListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('post/list/', PostListView.as_view(), name='list'),
    path('post/create/', PostCreateView.as_view(), name='create'),
    path('post/<int:pk>/detail/', PostDetailView.as_view(), name='detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete')
]
