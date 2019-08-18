from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from django.shortcuts import redirect
from .forms import PostForm
# Create your views here.

def blogHome(request):
    return render(request, 'blog/blog_home.html', {})

def blogList(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date').reverse()
    return render(request, 'blog/blog_list.html', {'posts':posts})

def blogDetail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/blog_detail.html', {'post': post})

def blogDelete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blogList')

def blogNew(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blogDetail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/blog_new.html', {'form': form})

def blogEdit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blogDetail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/blog_new.html', {'form': form})