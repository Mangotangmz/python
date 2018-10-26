from flask import Flask
from flask_script import Manager

from app.model import db
from app.views import blue, mail

app = Flask(__name__)

app.register_blueprint(blueprint=blue, url_prefix='/app')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS]'] = False

app.config["MAIL_SERVER"] = "mail.qq.com"
app.config["MAIL_PORT"] = 465  # 设置邮箱端口为465，默认为25，由于阿里云禁止了25端口，所以需要修改
app.config["MAIL_USE_SSL"] = True  # 163邮箱需要开启SSL
app.config["MAIL_USERNAME"] = "1990486426@qq.com"
app.config["MAIL_PASSWORD"] = "lkzoltadebtmcibh"

db.init_app(app)
mail.init_app(app)
manager = Manager(app=app)

if __name__ == '__main__':
    manager.run()
