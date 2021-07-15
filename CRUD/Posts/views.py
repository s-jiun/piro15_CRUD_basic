from .forms import PostForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    ctx = {'posts': posts}

    return render(request, template_name='list.html', context=ctx)

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    ctx = {'post': post}

    return render(request, template_name='detail.html', context=ctx)

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post=form.save()
            return redirect('Posts:list')
    else:
        form = PostForm()
        ctx = {'form': form}

        return render(request, template_name='post_form.html', context=ctx)

def post_update(request, pk):
    post = get_object_or_404(Post, id=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('Posts:detail', pk)
    else:
        form = PostForm(instance=post)
        ctx = {'form': form}

    return render(request, template_name='post_form.html', context=ctx)

def post_delete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('Posts:list')