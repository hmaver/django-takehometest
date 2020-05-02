from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .forms import PostForm
from django.shortcuts import redirect
from django.utils import timezone


from .models import Post, Author

# Get blog posts and display posts
def index(request):
    latest_posts = Post.objects.order_by('-created_date')[:5]
    context = {'latest_posts': latest_posts}

    return render(request, 'homepage/index.html', context)

# Display detailed view of each post
def detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'post_detail.html', {'post':post})

# Create new post
def post_new(request):
    user = request.user
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('homepage:detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})
