from flask import Flask
from flask_script import Manager

from app.model import db
from app.views import blue, mail

app = Flask(__name__)

app.register_blueprint(blueprint=blue, url_prefix='/app')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS]'] = False

db.init_app(app)
mail.init_app(app)
manager = Manager(app=app)

if __name__ == '__main__':
    manager.run()
