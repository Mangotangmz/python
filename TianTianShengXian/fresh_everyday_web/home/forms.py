
from django import forms


class UserForm(forms.Form):
    user_name = forms.CharField(required=True, error_messages={'required': '用户名不能为空'})
    pwd = forms.CharField(required=True, error_messages={'required': '密码不能为空'})
    cpwd = forms.CharField(required=True, error_messages={'required': '确认密码不能为空'})
    email = forms.CharField(required=True, error_messages={'required': '邮箱不能为空'})