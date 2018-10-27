from django.db import models

# Create your models here.
from django.shortcuts import render

# Create your views here.
from django.db import  models


class Users(models.Model):
    username = models.CharField(max_length=10,unique=True,verbose_name='姓名')
    password = models.CharField(max_length=220,unique=True,verbose_name='密码')
    icon = models.ImageField(upload_to='upload',null=True,verbose_name='头像')
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    operate_time = models.DateTimeField(auto_now=True,verbose_name='操作时间')

    class Meta:
        db_table = 'users'


class UserTicket(models.Model):
    user = models.ForeignKey(Users)
    ticket = models.CharField(max_length=30)
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')

