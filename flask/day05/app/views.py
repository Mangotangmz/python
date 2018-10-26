import os

from flask import Blueprint, request, render_template, redirect, url_for
from flask import Flask
from flask_login import login_user, LoginManager, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from app.form import UserRegisterForm
from app.model import db, User
from utils.settings import UPLOAD_DIR

blue = Blueprint('app', __name__)
login_manager = LoginManager()


@blue.route('/register/', methods=['POST', 'GET'])
def register():
    form = UserRegisterForm()
    if request.method == 'GET':
        return render_template('register.html', form=form)
    if request.method == 'POST':
        # 验证提交字段
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            # 实现注册，保存用户信息
            user = User()
            user.username = username
            user.password = generate_password_hash(password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('app.login'))
        else:
            return render_template('register.html', form=form)


@blue.route('/create_db/')
def create_db():
    db.create_all()
    return '创建成功'


@blue.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')

    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

    if not all([username, password]):
        return render_template('login.html')
    user = User.query.filter(User.username == username).first()
    if user:
        # 获取到用户，校验密码
        if check_password_hash(user.password, password):
            # 实现登录，diango中auth.login(request
            login_user(user)
            return redirect(url_for('app.index'))
        else:
            error = '密码错误'
            return render_template('login.html', error=error)
    else:
        # 获取不到用户，返回错误信息给页面
        error = '该用户没有注册，请先去注册'
        return render_template('login.html', error=error)


# 类似中间件，任何请求都要调用该函数
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@blue.route('/index/', methods=['POST', 'GET'])
@login_required
@blue.before_request
def index():
    if request.method == "GET":
        return render_template('index.html')
    if request.method == 'POST':
        # 获取图片
        icons = request.files.get('icons')
        # 保存save（path)
        # 中间件
        file_path = os.path.join(UPLOAD_DIR, icons.filename)
        icons.save(file_path)
        # 保存user对象
        user = current_user
        user.icons = os.path.join('upload', icons.filename)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('app.index'))


# 注销
@blue.route('/logout/')
@login_required
def logout():
    if request.method == 'GET':
        logout_user()
        return render_template('login.html')
