from django.contrib.auth.hashers import make_password, check_password
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from users.forms import UserForm
from users.models import Users, UserTicket
from utils.functions import get_ticekt, is_login


def register(request):
    if request.method == 'GET':
        # 如果请求为get，返回注册页面
        return render(request, 'register.html')

    if request.method == 'POST':
        # 校验参数
        form = UserForm(request.POST,request.FILES)
        # 判断is_valid()是否为True
        if form.is_valid():
            # 注册,使用make_password进行密码加密，否则为明文
            password = make_password(form.cleaned_data['password'])
            Users.objects.create(username=form.cleaned_data['username'],
                                 password=password,
                                 icon = request.FILES.get('icon'))
            # 跳转到登录页面,使用namespace:nane
            return HttpResponseRedirect(reverse('users:login'))

        else:
            return render(request, 'register.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        # 校验登录页面传递的参数
        form = UserForm(request.POST)
        # 使用is_valid()判断是否校验成功
        if form.is_valid():
            # 登录的设置
            # 1. 通过用户名和密码获取当前的user对象  ===>> auth.authenticate
            user = Users.objects.filter(username=form.cleaned_data['username']).first()
            if user:
                # 可以通过username获取到对象
                # 将 user.password和form.cleaned_data[‘password’]进行校验
                if check_password(form.cleaned_data['password'], user.password):
                    # 校验用户名和密码都成功
                    # 1. 向cookie中设置随机参数ticket
                    res = HttpResponseRedirect(reverse('users:index'))
                    # set_cookie(key, value, max_age='', expires='')
                    ticket = get_ticekt()
                    res.set_cookie('ticket', ticket, max_age=1000)
                    # 2. 向表user_ticket中存这个ticket和user的对应关系
                    UserTicket.objects.create(user=user, ticket=ticket)
                    return res
                else:
                    return render(request, 'login.html')
            else:
                # 登录系统的用户名不存在
                return render(request, 'login.html')
            # 2. 设置cookie中的随机值   ====>> auth.login()
            # 3. 设置user_ticket中的随机值
            pass
        else:
            return render(request, 'login.html')

# 装饰index函数
# @is_login
def index(request):
    if request.method == 'GET':
        # 从cookies中拿ticket
        ticket = request.COOKIES.get('ticket')
        user_ticket =  UserTicket.objects.filter(ticket=ticket).first()
        if user_ticket :
            # 获取当前登录系统的用户
            user= user_ticket.user
            return render(request,'index.html',{'user':user})
        else:
            return HttpResponseRedirect(reverse('users:login'))


def logout(request):
    if request == "GET":
        # 注销
        ticket = request.COOKIES.get('ticket')
        user_ticket = UserTicket.objects.filter(ticket=ticket).first()
        res = HttpResponseRedirect(reverse('users:index'))
        res.set_cookie('ticket',ticket,max_age=0)
    return render(request, 'login.html')


def users(request):
    if request.method == "GET":
        # 使用切片功能实现分页功能
        #sql:offset limit ,select * from user offset 3 limit 3
        page_number =  int(request.GET.get('page',1))
        users = Users.objects.all()

        # 使用paginator实现按照3条 数据进行分页
        pagintor = Paginator(users,3)

        # 获取某一个的信息
        page = pagintor.page(page_number)
        return render(request,'users.html',{'page':page})

