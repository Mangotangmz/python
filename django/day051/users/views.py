from django.contrib.auth.models import User
from django.shortcuts import render
from users.forms import UserForm
from users.forms import UserLoginForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import auth


# Create your views here.
def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    if request.method == "POST":
        # 校验页面中传递的参数是否填写完成

        form = UserForm(request.post)
        # is_valid():判断表单是否验证通过
        if form.is_vaild():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            password2 = form.cleaned_data.get('password2')
            User.objects.create_user(username=username, password=password)
            return HttpResponseRedirect(reverse('user:login'))

        else:
            return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')

    if request.method == 'POST':
        #         表单验证，用户名和密码是否填写，校验用户名是否注册
        form = UserLoginForm(request.POST)
        if form.is_valid():

            # 校验用户名和密码与数据库中对应的是否匹配
            user = auth.authenticate(username=form.cleaned_data['username'],
                                     password=form.cleaned_data['password'])

            if user:
                #             用户名和密码是正确的
                auth.login(request, user)
                return HttpResponseRedirect(reverse('user:index'))

            else:
                #             密码不正确
                return render(request, 'login.html', {'error': '密码错误'})
        else:
            return render(request, 'login.html', {'form': form})


def index(request):
    if request.method == "GET":
        return render(request, 'index.html')


def logout(request):
    if request.method == "GET":
        # 注销
        auth.logout(request)
        return HttpResponseRedirect(reverse('user:login'))
