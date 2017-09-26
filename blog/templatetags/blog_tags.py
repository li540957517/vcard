from django import template
from blog.models import Post, Category
from taggit.models import Tag

register = template.Library()


@register.simple_tag
def total_posts():
    """自定义简单标签"""
    return Post.published.count()


@register.inclusion_tag('latest_posts.html')
def show_latest_posts(count=5):
    """自定义包含标签"""
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


@register.assignment_tag
def get_all_categories():
    """自定义赋值标签"""
    return Category.objects.all()


@register.assignment_tag()
def get_all_tags():
    """所有标签项"""
    return Tag.objects.all()
