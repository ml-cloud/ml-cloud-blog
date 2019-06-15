from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django import forms
from .models import Post
from .forms import  CommentForm
from django.core.paginator import Paginator

def contact(request):
    return render(request,"contact.html")


def about(request):
    return render(request,"about.html")


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    paginate_by = 5
    template_name = 'index_new.html'

class PostList_ML(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on').filter(tag="ML")
    template_name = 'index_filtered.html'

class PostList_Cloud(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on').filter(tag="Cloud")
    template_name = 'index_filtered.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post.html'

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', post.slug)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form': form})
            
        