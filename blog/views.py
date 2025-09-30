# blog/views.py
from django.shortcuts import render
from .models import Post

def home(request):
    # Get the single most recent post
    try:
        recent_post = Post.objects.latest('publication_date')
    except Post.DoesNotExist:
        recent_post = None
    
    context = {
        'recent_post': recent_post
    }
    return render(request, 'index.html', context)

def post_list(request):
    # Get all posts
    all_posts = Post.objects.all()
    context = {
        'all_posts': all_posts
    }
    return render(request, 'blog_list.html', context)