from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import  HttpResponse
from myapp.models import  Student
from datetime import  datetime
# Create your views here.
def create_stu(request):
    # 创建学生信息
    # 引入ORM概念：对象关系映射
    # 第一种方式
    # Student.objects.create(s_name ="小花")

    # 第二种方式

    stu = Student()
    stu.s_name = '小红'
    stu.save()

    return HttpResponse('创建学生方法')