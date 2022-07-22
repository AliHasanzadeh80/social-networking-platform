from multiprocessing.spawn import import_main_path
from turtle import pos
from django.shortcuts import render
from .models import Post


def home(request):
    posts = Post.objects.all()
    context = {
        'title': 'home',
        'posts':  posts
    }

    return render(request, 'blog/home.html', context)


def about(request):
    context = {
        'title': 'about'
    }
    
    return render(request, 'blog/about.html', context)