from flask_script import  Manager
from flask import Flask, redirect

from app.views import blue

app = Flask(__name__)

# 将flask对象交给manager去管理，并且启动方式修改为manager.run()
manager = Manager(app=app)

# 第二步：绑定蓝图bule和app的关系
app.register_blueprint(blueprint=blue, url_prefix='/app')

# 设置secret_key
app.config['SECRET_KEY'] = '123'

# 路由匹配规则
# 1.<id>: 默认的接收类型是str
# 2.<string；id>,指定id类型为str
# 3.<int: id>,指定id的类型为int
# 4.<float：id>,指定接收的id类型为浮点型
# 5.<path:path>,指定接收的path为URL的路径

#
# @app.route('/get_id/<id>/')
# def get_id(id):
#     return 'id: %s' % id
#
#
# @app.route('/get_int_id/<int:id>/')
# def get_int_id(id):
#     # 匹配int类型的id值
#     return 'id: %d' % id
#
#
# @blue.route('/get_float/<float:uid>/')
# def get_float(uid):
#     return 'uid: %.2f' % uid
#
# @blue.route('/get_path/<path:upath>')
# def get_path(upath):
#     return 'path: %s' % upath



if __name__ == '__main__':
    # 修改启动的ip和窗口，debug模式host = '0.0.0.0', port = 8080,debug=True
    # python hello.py -h 0.0.0.0 -p 8080 -d
    manager.run()