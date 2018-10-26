import redis as redis
from flask import Flask
from flask_script import Manager
from flask_session import Session

from user.model import db
from user.views import blue

app = Flask(__name__)

app.register_blueprint(blueprint=blue, url_prefix='/user')
manager = Manager(app=app)


# session配置
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1', port=6379)

# 数据库配置
#dialect+driver://username:password@host:port/databasename
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



# 初始化session对象并进行绑定
se = Session()
se.init_app(app)

# 绑定app和db
db.init_app(app)


if __name__ == '__main__':
    manager.run()
