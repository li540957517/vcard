from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Comment, Post, Category


# Create your views here.
def blog_list(request):
    """博客列表页"""
    # posts = Post.objects.filter(status='published')
    # posts = Post.published.all()
    # return render(request, 'blog-list.html', {'posts': posts})
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog-list.html', {'page': page, 'posts': posts, 'paginator': paginator})


def blog_detail(request, year, month, day, slug):
    """博客日志详情页"""
    post = get_object_or_404(Post,
                             slug=slug,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day,
                             status='published')
    # categories = Category.objects.all()
    # return render(request, 'blog-detail.html', {'post': post, 'categories': categories})
    return render(request, 'blog-detail.html', {'post': post})
