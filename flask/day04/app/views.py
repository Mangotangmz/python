from flask import Blueprint, request
from flask import Flask
from flask_mail import Message, Mail
from flask import render_template

from app.model import db, Students, Grade, Course

blue = Blueprint('app', __name__)

mail = Mail()


@blue.route('/')
def hello():
    return 'hello'


@blue.route('/create_db/')
def create_db():
    # 用于初次创建模型
    db.create_all()
    return '创建成功'


@blue.route('/drop_db/')
def drop_db():
    # 删除数据库中所有的表
    db.drop_all()
    return '删除成功'


@blue.route('/create_stu/')
def create_stu():
    # 实现批量创建功能，add_all(), add()
    name = ['小清', '芳芳', '花花', '珂珂', 'Maira', 'Lisa', 'Dain']
    stu_list = []
    for item in name:
        stu = Students()
        stu.s_name = item
        # stu.save()
        stu_list.append(stu)
        # db.session.add(stu)
    db.session.add_all(stu_list)
    db.session.commit()
    return '创建学生信息成功'


@blue.route('/sel_stu/')
def sel_stu():
    #     查询，filter（），filter_by()

    # 返回一个新的数据,querybsae类型   可以继续filter，要获取数据.all()
    stu = Students.query.filter(Students.s_name == '小清')
    stu = Students.query.filter_by(s_name='小红')

    # 查询到的是个列表
    Students.query.all()

    # 执行sql
    # sql = 'select * from students;'
    # stus = db.session.execute(sql)

    '''模糊查询'''
    # select * from students where s_name like '%清%'
    #  select * from students where s_name like '清%'
    stu = Students.query.filter(Students.s_name.contains('清'))
    stu = Students.query.filter(Students.s_name.startswith('清'))
    stu = Students.query.filter(Students.s_name.endswith('清'))

    '''查询id在某个范围之内的学生信息'''
    # select * from students where id in (2,3,4,5)
    stus = Students.query.filter(Students.id.in_([2, 3, 4, 5, 6]))

    '''查询年龄大于19的学生'''
    stus = Students.query.filter(Students.s_age > 19)

    '''查询id=2的学生信息'''
    # get()获取主键对应的行数据
    stu = Students.query.get(2)

    '''分页'''
    # offset + limit
    stus = Students.query.limit(3)
    # 跳过前六条数据，得到第三页的数据
    stus = Students.query.offset(6).limit(3)

    '''升序，降序排列'''
    # order_by
    # 升序
    stus = Students.query.order_by('id')
    # 降序
    stus = Students.query.order_by('-id')

    '''and or not条件'''
    # 查询姓名中包含红的，且年龄等于23
    stus = Students.query.filter(Students.s_name.contains('红'), Students.s_age == 19)

    # 查询姓名中包含红，或者年龄等于23
    from sqlalchemy import or_
    stus = Students.query.filter(or_(Students.s_age == 23), Students.s_name.contains('红'))

    # 查询姓名中不包含红，且年龄等于19的
    from sqlalchemy import not_
    stus = Students.query.filter(not_(Students.s_name.contains('红')), Students.s_age == 19)

    return '查询学生'


@blue.route('/delete_stu/<int:id>/')
def delete_stu(id):
    stu = Students.query.filter(Students.id == id).first()
    db.session.delete(stu)
    db.session.commit()
    return '删除成功'


@blue.route('/update_stu/<int:id>/')
def update_stu(id):
    stu = Students.query.filter_by(id=id).first()
    stu.s_name = '默默'
    stu.save()
    return '修改成功'


@blue.route('/page/')
def page():
    if request.method == "GET":
        '''分页'''
        page = int(request.args.get('page', 1))
        #  1.offsite +limit
        Students.query.offset((page - 1) * 2).limit(2)

        # 2.切片
        stus = Students.query.all()[(page - 1) * 2:page * 2]

        # 3.sql
        sql = 'select * from students limit %s,%s ' % ((page - 1) * 2, 2)

        # 4. paginate()方法
        paginate = Students.query.paginate(page, 2)
        stus = paginate.items

        return render_template('page.html', stus=stus, paginate=paginate)


# 1. 创建班级信息
# 2.指定学生和班级的关联关系
@blue.route('/create_grade/')
def create_grade():
    grade = ['物联网', '互联网', '应数']
    grade_list = []
    for item in grade:
        grade = Grade()
        grade.g_name = item
        grade_list.append(grade)
    db.session.add_all(grade_list)
    db.session.commit()
    return '创建成功'


@blue.route('/rel_stu_grade/')
def rel_stu_grade():
    stus_ids = [2, 3, 4]
    for id in stus_ids:
        stu = Students.query.get(id)
        # 在flask中stu.s_g获取的值为int类型
        # 在django中stu.s_g获取到的是对象，stu.s_g_id获取的为int类型
        stu.s_g = 1
        stu.save()
    return '关联成功'


@blue.route('/sel_stu_by_grade')
def sel_stu_by_grade():
    # 通过班级查找学生
    grade = Grade.query.filter(Grade.g_name == '物联网').frist()
    stus = grade.students
    return '通过班级查找学生信息'


@blue.route('/sel_grade_by_stu/')
def sel_grade_by_stu():
    stu = Students.query.get(5)
    # 获取班级，学生对象.backref
    grade = stu.grade
    return '通过学生获取班级信息'


# 给课程表添加课程
@blue.route('/create_course/')
def create_course():
    cou = ['XML', 'C语言程序设计', '线性代数', 'PHP']

    list = []
    for item in cou:
        course = Course()
        course.c_name = item
        list.append(course)
    db.session.add_all(list)
    db.session.commit()
    return '创建课程成功'



# 添加课程和学生的关联关系

@blue.route('/add_stu_cou/')
def add_stu_cou():
    stu = Students.query.get(3)
#     学生的对象查找课程信息，stu.cou
    cou1 = Course.query.get(1)
    cou2 = Course.query.get(2)
    cou3 = Course.query.get(3)

#     绑定学生和课程的关系
#     stu.cou:拿到的是一个Course对象
    stu.cou.append(cou1)
    stu.cou.append(cou2)
    stu.cou.append(cou3)
    stu.save()
    return '绑定成功'


