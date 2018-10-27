import logging

from django.contrib.auth.models import Permission,Group
from django.shortcuts import render
from django.http import  HttpResponse
from django.contrib.auth.decorators import  permission_required
# Create your views here.
from users.models import MyUser

logger =logging.getLogger(__name__)

def add_user_permission(request):
    if request.method =="GET":
        # 给姓名为admin的用户添加修改用户的权限
        user= MyUser.objects.filter(username = 'admin').first()
        per = Permission.objects.filter(codename='change_myuser_username').first()
#         添加权限
        user.user_permissions.add(per)

        #删除权限
        user.user_permission.remove()

        # 情空权限
        user.user_permissions.clear()

        return HttpResponse('添加用户权限成功')

def create_user(request):
    if request.method =="GET":
        MyUser.objects.create_user(username='admin',password='123123')

        return  HttpResponse('创建用户成功')




def add_group_permission(request):
    if request.method == "GET":
#         创建审核组，并分配查看和编辑
        group =Group.objects.filter(name='审核组').first()
        if group:
            per_list =['change_myuser','delete_myuser',
                       'change_myuser_username',
                       'change_myuser_password']
            # 获取编辑的四个权限
            perms = Permission.objects.filter(codename__in = per_list)
            for per in perms:
                # 添加组合权限之间的关系
                group.permissions.add(per)
            #     删除组和权限之间的关系
            #     group.permission.remove(per)
            return HttpResponse('添加组和权限的关系')

        else:

            Group.objects.create(name='审核组')
            return HttpResponse('审核组没有创建，请先创建')

def add_user_group(request):
    if request.method == "GET":
        # 给admin用户分配审核组
        user = MyUser.objects.filter(username='admin').first()
        group = Group.objects.filter(name='审核组').first()
        user.groups.add(group)

        return HttpResponse('分配组成功')

def user_permission(request):
    if request.method == 'GET':
        user = MyUser.objects.filter(username='admin').first()
        # 查询user的权限
#         1.用户和权限查询
        p1= user.user_permissions.all().values('codename')

#         2.通过用户组查询组，通过组查询权限
        p2 =user.groups.all().permissions.all().values('codename')

        # 通过用户获取组权限
        user.get_group_permissions()

        # 通过用查询所有权限
        user.get_all_permissions()

        return HttpResponse('用户权限查询')

@permission_required('users.change_myuser_username')
def index(request):
    if request.method == "GET":
        logger.info('index方法')
        # change_myuser_username
        # return HttpResponse('我是首页，需要权限才能访问')
        return render(request,'index.html')