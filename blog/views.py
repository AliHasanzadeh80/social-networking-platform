from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.contrib.auth.models import User

from django.core.paginator import Paginator


# def home(request):
#     posts = Post.objects.all()
#     context = {
#         'title': 'home',
#         'posts':  posts
#     }

#     return render(request, 'blog/home.html', context)


class PostList(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_added']
    paginate_by = 5


class UserPostList(ListView):
    model = Post
    template_name = 'blog/user-posts.html'
    context_object_name = 'posts'
    ordering = ['-date_added']
    paginate_by = 5

    def get_queryset(self):
        user = User.objects.get(username=self.kwargs['username'])
        return Post.objects.filter(author=user)
    

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post-detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        print(post)
        if post.author == self.request.user:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        print(post)
        if post.author == self.request.user:
            return True
        else:
            return False

    
def about(request):
    context = {
        'title': 'about'
    }
    
    return render(request, 'blog/about.html', context)