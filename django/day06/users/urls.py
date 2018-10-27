from django.conf.urls import url, include
from django.contrib import admin

from users import views

urlpatterns=[
#    注册
    url(r'^register/',views.register,name='register'),
#     登录
    url(r'^login/',views.login,name='login'),
#     首页
    url(r'^index',views.index,name='index'),
#     注销
    url(r'^logout/',views.logout,name='logout'),

    url(r'^users/',views.users,name='users')
]