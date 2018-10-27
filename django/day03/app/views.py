from django.db.models import Q, F, Avg
from django.http import HttpResponse
from django.shortcuts import render

from app.models import Student, StudentInfo, Grade, Course


def create_stu(request):
    # 创建学生信息
    # 引入ORM概念：对象关系映射
    # 第一种方式
    Student.objects.create(s_name='小花11')
    Student.objects.create(s_name='小花4')
    Student.objects.create(s_name='小花5')
    Student.objects.create(s_name='小花6')
    Student.objects.create(s_name='小花7')
    Student.objects.create(s_name='小花8')
    Student.objects.create(s_name='小花9')
    Student.objects.create(s_name='小花10')
    # 第二种
    # stu = Student()
    # stu.s_name = '小龙'
    # stu.save()
    # 第三种
    # stu = Student('小草', 18, 1)
    # stu.save()

    return HttpResponse('创建学生方法')


def select_stu(request):
    """
    all：所有
    filter: 获取的结果为queryset，可以返回空，或一条或多条数据
    get：获取的结果是object对象，如果获取不成功，会报错，如果获取的参数超多一条，也会报错
    exclude：不包含
    """
    # 查询数据
    # select * from app_student;
    # stus = Student.objects.all()

    # select * from xxx where s_name='小花';
    # 返回的是一个queryset(集合)
    stus = Student.objects.filter(s_name='小花11')

    # filter(): 查询年龄等于19的学生
    stus = Student.objects.filter(s_age=28)

    # get(): 查询年龄等于19的学生
    # stus = Student.objects.get(s_age=19)
    stus = Student.objects.filter(id=100)
    stus = Student.objects.all().values('id', 's_name', 's_age')
    
    
    
    
    
    # 多条件查询
    # 年龄等于19，姓名等于小花
    stus = Student.objects.filter(s_age=19).filter(s_name='小花')
    stus = Student.objects.filter(s_age=19, s_name='小花')
    # 查询姓名不等于小花的学生信息
    stus = Student.objects.exclude(s_name='小花')
    # 排序，按照id升序/降序===> asc/desc
    stus = Student.objects.all().order_by('id')
    stus = Student.objects.all().order_by('-id')

    # values()
    stus = Student.objects.all().values('id', 's_name', 's_age')
    # get(),first()
    # stus = Student.objects.get(id=100)
    stus = Student.objects.filter(id=100).first()
    # first()/last()
    stus = Student.objects.all().order_by('id').last()
    stus = Student.objects.all().order_by('-id').first()
    stus = Student.objects.all().order_by('-id')[10:]
    # return HttpResponse(stus.id)
    # 查询名字中带有花的学生的信息
    # select * from xxx where name like '%花%'
    stus = Student.objects.filter(s_name__contains='花')
    # select * from xxx where name like '花%'
    stus = Student.objects.filter(s_name__startswith='花')
    # select * from xxx where name like '%花'
    stus = Student.objects.filter(s_name__endswith='花')
    # in
    stus = Student.objects.filter(id__in=[1,2,3])
    # 年龄大于18
    stus = Student.objects.filter(s_age__gt=18)
    # pk
    stus = Student.objects.filter(id=1)
    stus = Student.objects.filter(pk=1)

    # Q(),查询姓名叫小花的，或者年龄等于18.或使用 |
    stus = Student.objects.filter(Q(s_name='小花') | Q(s_age=18))
    stus = Student.objects.filter(Q(s_name='小花') & Q(s_age=18))
    # 非，姓名不叫小花的，或者年龄等于18的
    stus = Student.objects.filter(~Q(s_name='小花') | Q(s_age=18))

    # 查询语文成绩比数学成绩低10分的学生信息
    # select * from xxx where math - 10 > chinese
    stus = Student.objects.filter(math__gt=F('chinese') + 10)

    # 求平均值：select AVG(math) from app_student;
    avg_math = Student.objects.aggregate(Avg('math'))
    print(avg_math)
    # 获取学生的姓名
    stu_names = [(stu.s_name,stu.id) for stu in stus]
    print(stu_names)
    names = []
    for i in stus:
        names.append(i.s_name)
    print(names)
    return HttpResponse(stu_names)


    names = []
    for i in stus:
        names.append(i)
    print(i)
    return HttpResponse(i)


def delete_stu(request):
    # 删除
    # stu = Student.objects.get(pk=5)
    # stu = Student.objects.filter(pk=3).first()
    # stu.delete()

    Student.objects.filter(id=2).first().delete()
    return HttpResponse('删除')


def update_stu(request):
    # 更新
    # 第一种
    stu = Student.objects.get(pk=1)
    stu.s_name = '帅哥'
    stu.save()
    # 第二种
    Student.objects.filter(id=1).update(s_name='哈哈')
    return HttpResponse('修改')


def create_stu_info(request):
    if request.method == 'GET':
        data = {
            '18200384771': '金牛区',
            '13551677976': '锦江区',
            '13551677975': '锦江区1',
            '13551677977': '锦江区2',
            '13551677978': '锦江区3',
        }
        for k,v in data.items():
            StudentInfo.objects.create(phone=k, address=v)
        return  HttpResponse('创建拓展表数据')


    if request.method == 'POST':
        pass


def stu_add_stuinfo(request):
    if request.method == 'GET':
        # 给id为1的学生添加拓展表中id=2的信息，
        stu = Student.objects.get(id=1)
        # 绑定关系1：
        # stu.stu_info_id = 2
        # 绑定关系2：
        stu.stu_info = StudentInfo.objects.get(id=2)
        stu.save()
        return HttpResponse('绑定学生和拓展表的关联关系')


def sel_phone_by_stu(request):
    if request.method == 'GET':
        # 获取id=2的学生的手机号
        # 方法1：
        stu = Student.objects.filter(id=2).first()
        info_id = stu.stu_info_id
        stu_info = StudentInfo.objects.get(pk=info_id)
        phone = stu_info.phone
        # 方法2：
        stu = Student.objects.get(id=2)
        stu_info = stu.stu_info
        phone = stu_info.phone
        return HttpResponse('通过学生查找手机号')


def sel_stu_by_phone(request):
    if request.method == 'GET':
        stu_info = StudentInfo.objects.get(phone='13551677976')
        # stu_info.student和stu_info.stu只能用一个
        stu = stu_info.student
        s_name = stu.s_name
        return HttpResponse(s_name)


def create_grade(request):
    if request.method == 'GET':
        # 创建班级
        grade_name = ['Python', 'Java', 'Php', 'VHDL']
        for name in grade_name:
            Grade.objects.create(g_name=name)
        return HttpResponse('创建班级成功')


def sel_stu_by_grade(request):
    if request.method == 'GET':
        # 查询叫小花5的学生对于的班级名称
        stu = Student.objects.filter(s_name='小花5').first()
        grade = stu.g
        # 查询java班级下有多少学生，获取学生的姓名
        grade = Grade.objects.filter(g_name='Java').first()
        # stus = grade.student_set.all()
        stus = grade.stu.all()
        pass


def create_course(request):
    if request.method == 'GET':
        # 添加课程
        courses = ['线代', '高数', '大学物理', '概率论']
        for i in courses:
            Course.objects.create(c_name=i)
        return  HttpResponse('添加课程成功')


def create_stu_course(request):
    if request.method == 'GET':
        # 添加学生对于的课程信息
        # 让id=2的学生选择课程(id=1,2)
        stu = Student.objects.get(id=2)
        # 添加add()方法
        # stu.c.add(2)
        # 添加概率论和id=4的学生关联关系
        # cou = Course.objects.get(c_name='概率论')
        # 添加add()
        # cou.student_set.add(4)

        # 删除id=2的学生选的id=2的课程
        stu.c.remove(2)
        return HttpResponse('添加学生课程信息')
