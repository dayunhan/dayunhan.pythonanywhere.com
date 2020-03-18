from .models import Post
from .forms import PostForm

from django.shortcuts import render
from django.utils import timezone


def index(request):
    return render(request, 'blog/index.html', {})


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
