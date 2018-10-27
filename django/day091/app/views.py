from django.shortcuts import render
from rest_framework import viewsets, mixins, status
# Create your views here.
from rest_framework.mixins import DestroyModelMixin
from rest_framework.response import Response

from app.filters import StudentFilter
from app.models import Student
from app.serializers import StudentSerializer



class StudentView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  DestroyModelMixin,
                  mixins.RetrieveModelMixin,

                  viewsets.GenericViewSet):

    # 返回数据
    queryset = Student.objects.all().filter(is_delete=0)
    #序列化结果
    serializer_class = StudentSerializer

    def perform_destroy(self, instance):
        instance.is_delete = 1
        instance.save()

    #     过滤
    filter_class = StudentFilter

def index(request):
    if request.method == 'GET':
        return render(request, '../templates/index.html')

def add(request):
    if request.method =="GET":
        return render(request, '../templates/add.html')


'''# 模糊搜索
    def get_queryset(self):
        # 获取学生对象的数据
        queryset = self.queryset
        name = self.request.query_params.get('name')
        # 返回过滤的学生结果
        return queryset.filter(s_name__content='小花4')
'''
