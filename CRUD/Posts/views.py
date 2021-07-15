from django.shortcuts import render
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    ctx = {'posts': posts}

    return render(request, template_name='list.html', context=ctx)

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    ctx = {'post': post}

    return render(request, template_name='detail.html', context=ctx)