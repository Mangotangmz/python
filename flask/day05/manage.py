from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.testing import db

from app.views import blue, login_manager


app = Flask(__name__)

app.register_blueprint(blueprint=blue, url_prefix='/app')
app.config['SECRET_KEY'] = '123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login_manager.init_app(app)

# 没有登录跳转到登录
login_manager.login_view = 'app.login'


manager = Manager(app)

if __name__ == '__main__':
    manager.run()
