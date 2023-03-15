from django.shortcuts import render
from django.utils import timezone
from .models import Post, Comment
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, CommentForm     
from django.shortcuts import redirect

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        pform = PostForm(request.POST)
        if pform.is_valid():
            post = pform.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        pform = PostForm()
    return render(request, 'blog/post_edit.html', {'form': pform})    

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        pform = PostForm(request.POST, instance=post)
        if pform.is_valid():
            post = pform.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        pform = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': pform})

def comment_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    if request.method == "POST":
        cform = CommentForm(request.POST)
        if cform.is_valid():
            comment = cform.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.published_date = timezone.now()
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        cform = CommentForm()
    return render(request, 'blog/post_detail.html', {'comments' : comments, 'post': post, 'xform': cform}) 
    