from flask_sqlalchemy import SQLAlchemy

# 获取对象
db = SQLAlchemy()


class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_name = db.Column(db.String(10), unique=False, nullable=False)
    s_age = db.Column(db.Integer, default=19)
    s_g = db.Column(db.Integer, db.ForeignKey('grade.id'), nullable=True)
    __tablename__ = 'students'

    def save(self):
        db.session.add(self)
        db.session.commit()


class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    g_name = db.Column(db.Integer, unique=True, nullable=False)
    students = db.relationship('Students', backref='grade')
    __tablename__ = 'grade'


# 中间表
s_c = db.Table('s_c',
               db.Column('s_id', db.Integer, db.ForeignKey('students.id')),
               db.Column('c_id', db.Integer, db.ForeignKey('course.id'))
               )


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    c_name = db.Column(db.String(30), unique=True, nullable=False)
    Students = db.relationship('Students', secondary=s_c, backref='cou', lazy='dynamic')
