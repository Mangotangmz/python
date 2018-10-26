from flask_script import  Manager
from flask import Flask, Blueprint, redirect, url_for, request, make_response, render_template, abort, session

#第一步： 获取蓝图对象，指定蓝图别名为app
from utils.function import is_login

blue = Blueprint('app', __name__)

manager = Manager(app=blue)


@blue.route('/')
def hello_world():
    # 1/0
    return 'Hello World!'


@blue.route('/redirect/')
def redirect_hello():
    # 实现跳转
    # return redirect('/app/')
    # 反向解析redirect(url_for('蓝图名.函数名'))
    return redirect(url_for('app.hello_world'))
    # return redirect(url_for('app.hello_world'))


@blue.route('/request/', methods=['GET', 'POST'])
def get_request():
    # 请求上下文request
    # 获取GET请求传递的参数：request.args.get(key)/request.args.getlist()
    # 获取POST,PUT,PATCH，DELETE请求传递的参数：request.form.get(key)/request.form.getlist()
    # 判断请求方式request.method
    pass


@blue.route('/response/', methods=['GET'])
@is_login
def get_response():
    #创建响应
    # res = make_response('人生苦短，我学python', 200)
    # 响应绑定cookie， setcookie(key,value,max_age,expire)
    # 删除cookies，delete_cookie(key)
    res_index = render_template('index.html')
    res = make_response(res_index, 200)
    return res


@blue.route('/index/', methods=['GET'])

def index():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    try:
        a/b
    except Exception as e:
        print(e)
        abort(500)
    return render_template('index.html')

@blue.errorhandler(500)
def error500(exception):
    return '捕捉异常，错误信息为;%s' % exception


@blue.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')

    if request.method == 'POST':
        #获取页面传来的参数
        username= request.form.get('username')
        password = request.form.get('password')
        # 验证用户名和密码
    if username == 'coco' and password == '123123':
        # 验证成功，向session中存入登录成功的标识符
        session['login_satus'] = 1

        return  redirect(url_for('app.get_response'))
    else:
        return render_template('login.html')


if __name__ == '__main__':
    # 修改启动的ip和窗口，debug模式host = '0.0.0.0', port = 8080,debug=True
    # python hello.py -h 0.0.0.0 -p 8080 -d

    manager.run()