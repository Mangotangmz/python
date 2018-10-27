
from datetime import datetime

from django.db import models


class StudentInfo(models.Model):
    phone = models.CharField(max_length=11, null=True, unique=True,  verbose_name='手机号')
    address = models.CharField(max_length=50, null=True, verbose_name='地址')

    class Meta:
        db_table = 'student_info'


class Grade(models.Model):
    g_name = models.CharField(max_length=10, unique=True, verbose_name='班级名称')

    class Meta:
        db_table = 'grade'


class Course(models.Model):
    c_name = models.CharField(max_length=10, null=True)

    class Meta:
        db_table = 'course'


class Student(models.Model):
    s_name = models.CharField(max_length=10, unique=True, verbose_name='姓名')
    s_age = models.IntegerField(default=19, verbose_name='年龄')
    s_sex = models.BooleanField(default=1, verbose_name='性别')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    operate_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    math = models.DecimalField(max_digits=4, decimal_places=2, null=True) # 99.99
    chinese = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    stu_info = models.OneToOneField(StudentInfo, null=True, related_name='stu')
    g = models.ForeignKey(Grade, null=True, related_name='stu')
    c = models.ManyToManyField(Course, null=True)

    class Meta:
        db_table = 'app_student'
    #
    # def __init__(self, name, age=None, sex=None):
    #     super().__init__()
    #     self.s_name = name
    #     self.s_age = age if age else self.s_age
    #     self.s_sex = sex if sex else self.s_sex
    #     self.create_time = datetime.now()
    #     self.operate_time = datetime.now()

