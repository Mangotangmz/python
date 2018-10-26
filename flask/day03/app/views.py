from flask import Blueprint
from flask import Flask
from flask_mail import Message, Mail

from app.model import db, Students


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


@blue.route('/email/')
def index():
    msg = Message('hello', sender='from@1990486426@qq.com', recipients=['to@1990486426@qq.com'])
    mail.send(msg)
    return '邮件发送成功'
