from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment, Post, Category


# Create your views here.
def blog_list(request):
    """博客列表页"""
    posts = Post.objects.all()
    return render(request, 'blog-list.html', {'posts': posts})


def blog_detail(request):
    """博客日志详情页"""
    pass
