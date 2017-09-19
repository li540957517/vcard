from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', view=views.blog_list, name='blog_list'),
    url(r'^(?P<slug>[-\w]+)/$', view=views.blog_detail, name='blog_detail'),
]
