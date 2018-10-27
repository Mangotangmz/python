from django.contrib.auth.hashers import check_password
from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from django.urls import reverse

from untils.functons import is_login
from users.models import Users


def login(request):
    if request.method == 'GET':
        return render(request,'login.html')

    if request.method == "POST":
        # 使用cookies+session形式实现登录
        username = request.POST.get('username')
        password = request.POST.get('password')
        # all()校验参数，如果列表中元素为空，则返回False
        if not all([username,password]):
            msg ='请填写完整参数'
            return  render(request,'login.html', {'msg':msg})
        # 校验是否能通过username和password找到user对象
        user = Users.objects.filter(username=username).first()
        if user:
            # 校验密码
            if not check_password(password,user.password):
                msg = '密码错误'
                return  render(request,'login.html',{'msg':msg})
            else:
                # 向cookie中设置，向user_ticket表中设置
                # user_id作为键，user.id 为键值
                request.session['user_id'] = user.id
                #
                from datetime import datetime, timedelta
                # 设置明天这个时候过期
                # out_time = datetime.now() + timedelta(days=1)
                request.session.set_expiry(timedelta(days=4))
                return  HttpResponseRedirect(reverse('users:index'))

        else:
            msg = '用户名错误'
            return render(request,'login.html',{'msg':msg})
@is_login
def index(request):
    if request.method == "GET":
        return  render(request,'index.html')
@is_login
def logout(request):
    if request.method == "GET":
        # 注销，删除session和cookies中的值
        request.session.flush()
        # 获取session的值并注销
        # session_key = request.session.session_key
        # request.session.delete(session_key)
        # 设置seesion过期时间


        return HttpResponseRedirect(reverse('users:login'))

