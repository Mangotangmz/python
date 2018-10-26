from flask_script import Manager

from flask import Blueprint, render_template, request, session, redirect, url_for

from user.model import db, User

blue = Blueprint('user', __name__)


@blue.route('/login/')
def login():
    if request.method == "GET":
        return render_template('login.html')

    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        if not all([username, password]):
            return render_template('login.html')

        user = User.objects.filter(username=username)
        if user:
            # 校验密码

                session['login_status'] = 1
                return redirect(url_for('user.index'))
        else:
            return render_template('login.html')


@blue.route('/index/')
def index():
    if request.method == "GET":
        return render_template('index.html')


@blue.route('/scores/', methods=['GET'])
def scores():
    stu_scores = [80, 56, 31, 98]
    cotent_h2 = '<h2>hello python</h2>'
    return render_template('scores.html', stu_scores=stu_scores, cotent_h2=cotent_h2)


@blue.route('/create_db/')
def create_db():
    db.create_all()
    return '创建成功'


@blue.route('/register/', methods=['GET', "POST"])
def register():
    if request.method == "GET":
        return render_template('register.html')
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get("password")

        if not all([username, password]):
            return render_template('register.html')

    # 保存注册信息
    user = User()
    user.username = username
    user.password = password

    db.session.add(user)
    db.session.commit()
    return render_template('login.html')
