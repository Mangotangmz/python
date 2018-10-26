from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from home.forms import UserLoginForm


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        # 1.表单验证
        form = UserLoginForm(request.POST)
        # 使用is_valid()进行表单验证
        if form.is_valid():
            # form表单验证成功
            user = auth.authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password'),
            )
            # 2.auth模块验证
            # 3.auth.login登录
            if user:
                # 如果用户名密码正确获取到user对象，则进行登录
                # request.user默认是AnonyMouseUser
                auth.login(request, user)  # 实质上是给request.user赋值
                return HttpResponseRedirect(reverse('home:index'))
            else:
                # 获取用户名和密码错误
                return render(request, 'login.html', {'error': '密码错误'})


        else:
            # form验证失败，则将错误返回
            return render(request, 'login.html', {'error': form})


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        return HttpResponseRedirect(reverse('home:login'))


def goods_desc(request):
    if request.method == 'GET':
        return render(request, 'goods_desc.html')


def order_list(request):
    if request.method == 'GET':
        return render(request, 'order_list.html')


def user_list(request):
    if request.method == 'GET':
        return render(request, 'user_list.html')