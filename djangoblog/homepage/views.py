from django.shortcuts import render

from .models import Post, Author

def index(request):
    return render(request, 'homepage/index.html')