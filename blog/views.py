from django.shortcuts import render

def home(request):
    context = {
        'title': 'home',
        'posts':  [
            {
                'author': 'CoreyMS',
                'title': 'Blog Post 1',
                'content': 'First post content',
                'date_posted': 'August 27, 2018'
            },
            {
                'author': 'Jane Doe',
                'title': 'Blog Post 2',
                'content': 'Second post content',
                'date_posted': 'August 28, 2018'
            }
        ]

    }
    return render(request, 'blog/home.html', context)

def about(request):
    context = {
        'title': 'about'
    }
    return render(request, 'blog/about.html', context)