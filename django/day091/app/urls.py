from django.conf.urls import url
from django.contrib import admin
from rest_framework.routers import SimpleRouter

# 引入路由
from app import views

router = SimpleRouter()
# 使用router注册的地址,不加斜杆
router.register(r'^student',views.StudentView)

urlpatterns = [
 url(r'^index',views.index,name='index'),
    url(r'^add/',views.add,name='add')
]
urlpatterns +=router.urls