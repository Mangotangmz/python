from django.shortcuts import render
from django.http import  HttpResponse,HttpResponseRedirect
from app4.models import Student
from django.urls import reverse
# Create your views here.
def index(request):
    if request.method == "GET":
        # return HttpResponse('hello')
        students = Student.objects.all()
        # return render(request,'index.html',{'Students':students})
        return render(request, 'stus.html', {'Students': students})

def del_stu(request,s_id):
    if request.method == "GET":
        # 删除方法
        # 1.获取url的id值
        id = request.GET.get('id')
        #2.获取id对应的学生对象
        stu = Student.objects.get(pk=s_id)

        # 3. 对象。delete（）
        stu.delete()
    # return HttpResponseRedirect('app4/stus')
    return HttpResponseRedirect(reverse('app4:index'))

def check(request,s_id):
    if request.method == "GET":

        stu = Student.objects.get(pk=s_id)

        return render(request,'check.html', {'Students': stu})