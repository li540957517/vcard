from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import reverse
from tinymce.models import HTMLField
from taggit.managers import TaggableManager


# Create your models here.
class Category(models.Model):
    """日志分类"""
    name = models.CharField('分类名称', max_length=20)
    slug = models.SlugField('URL缩写', max_length=100)
    description = models.CharField('备注说明', max_length=200, null=True)

    def __str__(self):
        return self.name


class PostPublishedManager(models.Manager):
    """
    博客日志管理器
    过滤状态为 published 日志信息
    """

    def get_queryset(self):
        return super(PostPublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    """日志文章"""
    STATUS_CHOICE = (
        ('draft', '草稿'),
        ('published', '发布'),
    )
    title = models.CharField('标题', max_length=100)
    slug = models.SlugField('URL缩写', max_length=100, unique_for_date='publish')
    category = models.ForeignKey(Category, related_name='blog_posts')
    author = models.ForeignKey(User, related_name='blog_posts')
    image = models.ImageField('图片', null=True, blank=True, upload_to='uploads')
    # body = models.TextField('正文')
    body = HTMLField('正文')
    publish = models.DateTimeField('发布时间', default=timezone.now)
    created = models.DateTimeField('创建时间', auto_now_add=True)
    update = models.DateTimeField('更新时间', auto_now=True)
    status = models.CharField('发布状态', max_length=50, choices=STATUS_CHOICE, default='draft')

    objects = models.Manager()
    published = PostPublishedManager()

    tags = TaggableManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publish', ]

    def get_absolute_url(self):
        """获取反向解析当前实例的URL"""
        return reverse('blog:blog_detail', args=[
            self.publish.year,
            self.publish.month,
            self.publish.day,
            self.slug,
        ])


class Comment(models.Model):
    """日志评论"""
    post = models.ForeignKey(Post, related_name='comments')
    name = models.CharField('用户名', max_length=20)
    email = models.EmailField('邮箱', max_length=200)
    content = models.TextField('评论')
    active = models.BooleanField('有效状态', default=True)
    created = models.DateTimeField('提交时间', auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.name}评论至{self.post}'
