from django.contrib import admin
from .models import Category, Post, Comment
from tinymce.widgets import TinyMCE


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    """日志分类管理"""
    list_display = ('name', 'slug', 'description')


class PostAdmin(admin.ModelAdmin):
    """日志管理"""
    list_display = ('title', 'slug', 'category', 'status', 'publish')
    list_editable = ('status',)
    search_fields = ('title', 'body')
    date_hierarchy = 'publish'
    list_filter = ('category', 'status', 'publish')
    list_per_page = 20

    # class Media:
    #     js = (
    #         'https://cloud.tinymce.com/stable/tinymce.min.js',
    #         '/static/js/tinymce/textareas.js'
    #     )


class CommentAdmin(admin.ModelAdmin):
    """日志评论管理"""
    list_display = ('name', 'post', 'email', 'active', 'created')
    list_per_page = 20


# 注册博客模块模型管理
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
