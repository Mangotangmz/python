import django_filters
from rest_framework import filters

from app.models import Student


class StudentFilter(filters.FilterSet):
    # 定义过滤字段
    # 从url中提取与字段对应的数据，模糊查询
    name = django_filters.CharFilter('s_name',lookup_expr='contains')
    # 开始时间
    sd = django_filters.CharFilter('create_time',lookup_expr='gt')
    # 结束时间
    ed = django_filters.CharFilter('create_time',lookup_expr='lt')

    class Meta:
        # 过滤Student模型
        model = Student
        fields = ['name',]