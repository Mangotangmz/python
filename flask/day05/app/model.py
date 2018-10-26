from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy.testing import db

db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    icons = db.Column(db.String(100), nullable=True)

    ___tablename__ = 'user'

