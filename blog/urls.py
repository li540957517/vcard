from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', view=views.blog_list, name='blog_list'),
]
