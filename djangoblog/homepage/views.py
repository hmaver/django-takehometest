from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Post, Author


# Get blog posts and display posts
def index(request):
    latest_posts = Post.objects.order_by('-created_date')[:5]
    context = {'latest_posts': latest_posts}

    return render(request, 'homepage/index.html', context)

# Display detailed view of each post
def detail(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'post_detail.html', {'post':post})

# Create new post

# Edit Post
