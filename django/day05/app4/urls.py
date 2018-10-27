'''Tangzhuzhu'''
from django.conf.urls import url,include
from django.contrib import admin
from app4 import views

urlpatterns = [
    url(r'^stu/',views.index,name='index'),
    url(r'^del_stu/(?P<s_id>\d+)/', views.del_stu,name='del_stu'),
    url(r'^check/(?P<s_id>\d+)/', views.check,name='check')

]
