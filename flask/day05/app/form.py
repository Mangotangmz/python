# 导入扩展类
from flask_wtf import FlaskForm
# 导入验证字段
from wtforms import StringField, SubmitField, ValidationError
# 导入表单验证
from wtforms.validators import DataRequired, EqualTo

#
# from user.models import User
from app.model import User


class UserRegisterForm(FlaskForm):
    """
    登录注册表单验证
    """
    username = StringField('用户名', validators=[DataRequired()])
    password = StringField('密码', validators=[DataRequired()])
    password2 = StringField('确认密码', validators=[DataRequired(),
                                                EqualTo('password', '密码不一致')]
                            )
    submit = SubmitField('提交')

    def validate_username(self, field):
        # 验证用户名是否重复
        if User.query.filter(User.username == field.data).first():
            raise ValidationError('用户名已存在')

        # 对用户名的长度进行判断
        if len(field.data) < 3:
            raise ValidationError('用户名长度不能少于3个字符')

        if len(field.data) > 6:
            raise ValidationError('用户名长度不能大于6个字符')
