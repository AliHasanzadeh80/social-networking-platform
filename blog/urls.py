from django.urls import path
from blog import views as blog_views
from .views import PostList, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostList

urlpatterns = [
    path('', PostList.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('user/<str:username>', UserPostList.as_view(), name='user-posts'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', blog_views.about, name='blog-about'),
]