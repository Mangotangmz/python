from django.contrib import admin

# Register your models here.
from app.models import Student

# 定义一个模型
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','s_name','s_age']
    # 过滤
    list_filter = ['s_age']
#     搜索
    list_fields=['s_name']

    list_per_page = 2


# 快捷键alt+enter
admin.site.register(Student,StudentAdmin)