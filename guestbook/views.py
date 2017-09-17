from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Message


# Create your views here.
def post_message(request):
    """首页留言提交处理"""
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        content = request.POST.get('message', '')
        if name and content:
            msg = Message(name=name, email=email, message=content)
            msg.save()
            return redirect(reverse('home'))
        else:
            return HttpResponse('用户名和留言必须填写！')
    return redirect(reverse('home'))
