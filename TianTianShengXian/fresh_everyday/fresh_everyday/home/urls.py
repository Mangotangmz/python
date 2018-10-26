
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from home import views

urlpatterns = [
    # 登录
    url(r'^login/', views.login, name='login'),
    # 主页
    url(r'^index', login_required(views.index), name='index'),
    # 注销
    url(r'^logout', login_required(views.logout), name='logout'),

    url(r'^goods_desc', views.goods_desc, name='goods_desc'),
    url(r'^order_list', views.order_list, name='order_list'),
    url(r'^user_list', views.user_list, name='user_list')

]